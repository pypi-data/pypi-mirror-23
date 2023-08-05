# coding: utf-8

from __future__ import print_function, absolute_import, division, unicode_literals

# Scanner produces tokens of the following types:
# STREAM-START
# STREAM-END
# DIRECTIVE(name, value)
# DOCUMENT-START
# DOCUMENT-END
# BLOCK-SEQUENCE-START
# BLOCK-MAPPING-START
# BLOCK-END
# FLOW-SEQUENCE-START
# FLOW-MAPPING-START
# FLOW-SEQUENCE-END
# FLOW-MAPPING-END
# BLOCK-ENTRY
# FLOW-ENTRY
# KEY
# VALUE
# ALIAS(value)
# ANCHOR(value)
# TAG(value)
# SCALAR(value, plain, style)
#
# RoundTripScanner
# COMMENT(value)
#
# Read comments in the Scanner code for more details.
#

from ruamel.yaml.error import MarkedYAMLError
from ruamel.yaml.tokens import *                # NOQA
from ruamel.yaml.compat import utf8, unichr, PY3, check_anchorname_char

if False:  # MYPY
    from typing import Any, Dict, Optional, List, Union, Text  # NOQA
    from ruamel.yaml.compat import VersionType  # NOQA

__all__ = ['Scanner', 'RoundTripScanner', 'ScannerError']


class ScannerError(MarkedYAMLError):
    pass


class SimpleKey(object):
    # See below simple keys treatment.

    def __init__(self, token_number, required, index, line, column, mark):
        # type: (Any, Any, int, int, int, Any) -> None
        self.token_number = token_number
        self.required = required
        self.index = index
        self.line = line
        self.column = column
        self.mark = mark


class Scanner(object):

    def __init__(self, loader=None):
        # type: (Any) -> None
        """Initialize the scanner."""
        # It is assumed that Scanner and Reader will have a common descendant.
        # Reader do the dirty work of checking for BOM and converting the
        # input data to Unicode. It also adds NUL to the end.
        #
        # Reader supports the following methods
        #   self.peek(i=0)    # peek the next i-th character
        #   self.prefix(l=1)  # peek the next l characters
        #   self.forward(l=1) # read the next l characters and move the pointer

        self.loader = loader
        if self.loader is not None and getattr(self.loader, '_scanner', None) is None:
            self.loader._scanner = self
        self.reset_scanner()

    def reset_scanner(self):
        # type: () -> None
        # Had we reached the end of the stream?
        self.done = False

        # The number of unclosed '{' and '['. `flow_level == 0` means block
        # context.
        self.flow_level = 0

        # List of processed tokens that are not yet emitted.
        self.tokens = []  # type: List[Any]

        # Add the STREAM-START token.
        self.fetch_stream_start()

        # Number of tokens that were emitted through the `get_token` method.
        self.tokens_taken = 0

        # The current indentation level.
        self.indent = -1

        # Past indentation levels.
        self.indents = []  # type: List[int]

        # Variables related to simple keys treatment.

        # A simple key is a key that is not denoted by the '?' indicator.
        # Example of simple keys:
        #   ---
        #   block simple key: value
        #   ? not a simple key:
        #   : { flow simple key: value }
        # We emit the KEY token before all keys, so when we find a potential
        # simple key, we try to locate the corresponding ':' indicator.
        # Simple keys should be limited to a single line and 1024 characters.

        # Can a simple key start at the current position? A simple key may
        # start:
        # - at the beginning of the line, not counting indentation spaces
        #       (in block context),
        # - after '{', '[', ',' (in the flow context),
        # - after '?', ':', '-' (in the block context).
        # In the block context, this flag also signifies if a block collection
        # may start at the current position.
        self.allow_simple_key = True

        # Keep track of possible simple keys. This is a dictionary. The key
        # is `flow_level`; there can be no more that one possible simple key
        # for each level. The value is a SimpleKey record:
        #   (token_number, required, index, line, column, mark)
        # A simple key may start with ALIAS, ANCHOR, TAG, SCALAR(flow),
        # '[', or '{' tokens.
        self.possible_simple_keys = {}  # type: Dict[Any, Any]

    @property
    def reader(self):
        # type: () -> Any
        if hasattr(self.loader, 'typ'):
            self.loader.reader  # type: ignore
        return self.loader._reader  # type: ignore

    @property
    def scanner_processing_version(self):  # prefix until un-composited
        # type: () -> VersionType
        if hasattr(self.loader, 'typ'):
            return self.loader.resolver.processing_version  # type: ignore
        return self.loader.processing_version

    # Public methods.

    def check_token(self, *choices):
        # type: (Any) -> bool
        # Check if the next token is one of the given types.
        while self.need_more_tokens():
            self.fetch_more_tokens()
        if bool(self.tokens):
            if not choices:
                return True
            for choice in choices:
                if isinstance(self.tokens[0], choice):
                    return True
        return False

    def peek_token(self):
        # type: () -> Any
        # Return the next token, but do not delete if from the queue.
        while self.need_more_tokens():
            self.fetch_more_tokens()
        if bool(self.tokens):
            return self.tokens[0]

    def get_token(self):
        # type: () -> Any
        # Return the next token.
        while self.need_more_tokens():
            self.fetch_more_tokens()
        if bool(self.tokens):
            self.tokens_taken += 1
            return self.tokens.pop(0)

    # Private methods.

    def need_more_tokens(self):
        # type: () -> bool
        if self.done:
            return False
        if not self.tokens:
            return True
        # The current token may be a potential simple key, so we
        # need to look further.
        self.stale_possible_simple_keys()
        if self.next_possible_simple_key() == self.tokens_taken:
            return True
        return False

    def fetch_comment(self, comment):
        # type: (Any) -> None
        raise NotImplementedError

    def fetch_more_tokens(self):
        # type: () -> Any
        # Eat whitespaces and comments until we reach the next token.
        comment = self.scan_to_next_token()
        if comment is not None:  # never happens for base scanner
            return self.fetch_comment(comment)
        # Remove obsolete possible simple keys.
        self.stale_possible_simple_keys()

        # Compare the current indentation and column. It may add some tokens
        # and decrease the current indentation level.
        self.unwind_indent(self.reader.column)

        # Peek the next character.
        ch = self.reader.peek()

        # Is it the end of stream?
        if ch == u'\0':
            return self.fetch_stream_end()

        # Is it a directive?
        if ch == u'%' and self.check_directive():
            return self.fetch_directive()

        # Is it the document start?
        if ch == u'-' and self.check_document_start():
            return self.fetch_document_start()

        # Is it the document end?
        if ch == u'.' and self.check_document_end():
            return self.fetch_document_end()

        # TODO: support for BOM within a stream.
        # if ch == u'\uFEFF':
        #     return self.fetch_bom()    <-- issue BOMToken

        # Note: the order of the following checks is NOT significant.

        # Is it the flow sequence start indicator?
        if ch == u'[':
            return self.fetch_flow_sequence_start()

        # Is it the flow mapping start indicator?
        if ch == u'{':
            return self.fetch_flow_mapping_start()

        # Is it the flow sequence end indicator?
        if ch == u']':
            return self.fetch_flow_sequence_end()

        # Is it the flow mapping end indicator?
        if ch == u'}':
            return self.fetch_flow_mapping_end()

        # Is it the flow entry indicator?
        if ch == u',':
            return self.fetch_flow_entry()

        # Is it the block entry indicator?
        if ch == u'-' and self.check_block_entry():
            return self.fetch_block_entry()

        # Is it the key indicator?
        if ch == u'?' and self.check_key():
            return self.fetch_key()

        # Is it the value indicator?
        if ch == u':' and self.check_value():
            return self.fetch_value()

        # Is it an alias?
        if ch == u'*':
            return self.fetch_alias()

        # Is it an anchor?
        if ch == u'&':
            return self.fetch_anchor()

        # Is it a tag?
        if ch == u'!':
            return self.fetch_tag()

        # Is it a literal scalar?
        if ch == u'|' and not self.flow_level:
            return self.fetch_literal()

        # Is it a folded scalar?
        if ch == u'>' and not self.flow_level:
            return self.fetch_folded()

        # Is it a single quoted scalar?
        if ch == u'\'':
            return self.fetch_single()

        # Is it a double quoted scalar?
        if ch == u'\"':
            return self.fetch_double()

        # It must be a plain scalar then.
        if self.check_plain():
            return self.fetch_plain()

        # No? It's an error. Let's produce a nice error message.
        raise ScannerError("while scanning for the next token", None,
                           "found character %r that cannot start any token"
                           % utf8(ch), self.reader.get_mark())

    # Simple keys treatment.

    def next_possible_simple_key(self):
        # type: () -> Any
        # Return the number of the nearest possible simple key. Actually we
        # don't need to loop through the whole dictionary. We may replace it
        # with the following code:
        #   if not self.possible_simple_keys:
        #       return None
        #   return self.possible_simple_keys[
        #           min(self.possible_simple_keys.keys())].token_number
        min_token_number = None
        for level in self.possible_simple_keys:
            key = self.possible_simple_keys[level]
            if min_token_number is None or key.token_number < min_token_number:
                min_token_number = key.token_number
        return min_token_number

    def stale_possible_simple_keys(self):
        # type: () -> None
        # Remove entries that are no longer possible simple keys. According to
        # the YAML specification, simple keys
        # - should be limited to a single line,
        # - should be no longer than 1024 characters.
        # Disabling this procedure will allow simple keys of any length and
        # height (may cause problems if indentation is broken though).
        for level in list(self.possible_simple_keys):
            key = self.possible_simple_keys[level]
            if key.line != self.reader.line  \
                    or self.reader.index - key.index > 1024:
                if key.required:
                    raise ScannerError(
                        "while scanning a simple key", key.mark,
                        "could not find expected ':'", self.reader.get_mark())
                del self.possible_simple_keys[level]

    def save_possible_simple_key(self):
        # type: () -> None
        # The next token may start a simple key. We check if it's possible
        # and save its position. This function is called for
        #   ALIAS, ANCHOR, TAG, SCALAR(flow), '[', and '{'.

        # Check if a simple key is required at the current position.
        required = not self.flow_level and self.indent == self.reader.column

        # The next token might be a simple key. Let's save it's number and
        # position.
        if self.allow_simple_key:
            self.remove_possible_simple_key()
            token_number = self.tokens_taken+len(self.tokens)
            key = SimpleKey(
                token_number, required,
                self.reader.index, self.reader.line, self.reader.column,
                self.reader.get_mark())
            self.possible_simple_keys[self.flow_level] = key

    def remove_possible_simple_key(self):
        # type: () -> None
        # Remove the saved possible key position at the current flow level.
        if self.flow_level in self.possible_simple_keys:
            key = self.possible_simple_keys[self.flow_level]

            if key.required:
                raise ScannerError(
                    "while scanning a simple key", key.mark,
                    "could not find expected ':'", self.reader.get_mark())

            del self.possible_simple_keys[self.flow_level]

    # Indentation functions.

    def unwind_indent(self, column):
        # type: (Any) -> None
        # In flow context, tokens should respect indentation.
        # Actually the condition should be `self.indent >= column` according to
        # the spec. But this condition will prohibit intuitively correct
        # constructions such as
        # key : {
        # }
        # ####
        # if self.flow_level and self.indent > column:
        #     raise ScannerError(None, None,
        #             "invalid intendation or unclosed '[' or '{'",
        #             self.reader.get_mark())

        # In the flow context, indentation is ignored. We make the scanner less
        # restrictive then specification requires.
        if bool(self.flow_level):
            return

        # In block context, we may need to issue the BLOCK-END tokens.
        while self.indent > column:
            mark = self.reader.get_mark()
            self.indent = self.indents.pop()
            self.tokens.append(BlockEndToken(mark, mark))

    def add_indent(self, column):
        # type: (int) -> bool
        # Check if we need to increase indentation.
        if self.indent < column:
            self.indents.append(self.indent)
            self.indent = column
            return True
        return False

    # Fetchers.

    def fetch_stream_start(self):
        # type: () -> None
        # We always add STREAM-START as the first token and STREAM-END as the
        # last token.
        # Read the token.
        mark = self.reader.get_mark()
        # Add STREAM-START.
        self.tokens.append(StreamStartToken(mark, mark,
                                            encoding=self.reader.encoding))

    def fetch_stream_end(self):
        # type: () -> None
        # Set the current intendation to -1.
        self.unwind_indent(-1)
        # Reset simple keys.
        self.remove_possible_simple_key()
        self.allow_simple_key = False
        self.possible_simple_keys = {}  # type: Dict[Any, Any]
        # Read the token.
        mark = self.reader.get_mark()
        # Add STREAM-END.
        self.tokens.append(StreamEndToken(mark, mark))
        # The steam is finished.
        self.done = True

    def fetch_directive(self):
        # type: () -> None
        # Set the current intendation to -1.
        self.unwind_indent(-1)

        # Reset simple keys.
        self.remove_possible_simple_key()
        self.allow_simple_key = False

        # Scan and add DIRECTIVE.
        self.tokens.append(self.scan_directive())

    def fetch_document_start(self):
        # type: () -> None
        self.fetch_document_indicator(DocumentStartToken)

    def fetch_document_end(self):
        # type: () -> None
        self.fetch_document_indicator(DocumentEndToken)

    def fetch_document_indicator(self, TokenClass):
        # type: (Any) -> None
        # Set the current intendation to -1.
        self.unwind_indent(-1)

        # Reset simple keys. Note that there could not be a block collection
        # after '---'.
        self.remove_possible_simple_key()
        self.allow_simple_key = False

        # Add DOCUMENT-START or DOCUMENT-END.
        start_mark = self.reader.get_mark()
        self.reader.forward(3)
        end_mark = self.reader.get_mark()
        self.tokens.append(TokenClass(start_mark, end_mark))

    def fetch_flow_sequence_start(self):
        # type: () -> None
        self.fetch_flow_collection_start(FlowSequenceStartToken)

    def fetch_flow_mapping_start(self):
        # type: () -> None
        self.fetch_flow_collection_start(FlowMappingStartToken)

    def fetch_flow_collection_start(self, TokenClass):
        # type: (Any) -> None
        # '[' and '{' may start a simple key.
        self.save_possible_simple_key()
        # Increase the flow level.
        self.flow_level += 1
        # Simple keys are allowed after '[' and '{'.
        self.allow_simple_key = True
        # Add FLOW-SEQUENCE-START or FLOW-MAPPING-START.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        end_mark = self.reader.get_mark()
        self.tokens.append(TokenClass(start_mark, end_mark))

    def fetch_flow_sequence_end(self):
        # type: () -> None
        self.fetch_flow_collection_end(FlowSequenceEndToken)

    def fetch_flow_mapping_end(self):
        # type: () -> None
        self.fetch_flow_collection_end(FlowMappingEndToken)

    def fetch_flow_collection_end(self, TokenClass):
        # type: (Any) -> None
        # Reset possible simple key on the current level.
        self.remove_possible_simple_key()
        # Decrease the flow level.
        self.flow_level -= 1
        # No simple keys after ']' or '}'.
        self.allow_simple_key = False
        # Add FLOW-SEQUENCE-END or FLOW-MAPPING-END.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        end_mark = self.reader.get_mark()
        self.tokens.append(TokenClass(start_mark, end_mark))

    def fetch_flow_entry(self):
        # type: () -> None
        # Simple keys are allowed after ','.
        self.allow_simple_key = True
        # Reset possible simple key on the current level.
        self.remove_possible_simple_key()
        # Add FLOW-ENTRY.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        end_mark = self.reader.get_mark()
        self.tokens.append(FlowEntryToken(start_mark, end_mark))

    def fetch_block_entry(self):
        # type: () -> None
        # Block context needs additional checks.
        if not self.flow_level:
            # Are we allowed to start a new entry?
            if not self.allow_simple_key:
                raise ScannerError(None, None,
                                   "sequence entries are not allowed here",
                                   self.reader.get_mark())
            # We may need to add BLOCK-SEQUENCE-START.
            if self.add_indent(self.reader.column):
                mark = self.reader.get_mark()
                self.tokens.append(BlockSequenceStartToken(mark, mark))
        # It's an error for the block entry to occur in the flow context,
        # but we let the parser detect this.
        else:
            pass
        # Simple keys are allowed after '-'.
        self.allow_simple_key = True
        # Reset possible simple key on the current level.
        self.remove_possible_simple_key()

        # Add BLOCK-ENTRY.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        end_mark = self.reader.get_mark()
        self.tokens.append(BlockEntryToken(start_mark, end_mark))

    def fetch_key(self):
        # type: () -> None
        # Block context needs additional checks.
        if not self.flow_level:

            # Are we allowed to start a key (not nessesary a simple)?
            if not self.allow_simple_key:
                raise ScannerError(None, None,
                                   "mapping keys are not allowed here",
                                   self.reader.get_mark())

            # We may need to add BLOCK-MAPPING-START.
            if self.add_indent(self.reader.column):
                mark = self.reader.get_mark()
                self.tokens.append(BlockMappingStartToken(mark, mark))

        # Simple keys are allowed after '?' in the block context.
        self.allow_simple_key = not self.flow_level

        # Reset possible simple key on the current level.
        self.remove_possible_simple_key()

        # Add KEY.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        end_mark = self.reader.get_mark()
        self.tokens.append(KeyToken(start_mark, end_mark))

    def fetch_value(self):
        # type: () -> None
        # Do we determine a simple key?
        if self.flow_level in self.possible_simple_keys:
            # Add KEY.
            key = self.possible_simple_keys[self.flow_level]
            del self.possible_simple_keys[self.flow_level]
            self.tokens.insert(key.token_number-self.tokens_taken,
                               KeyToken(key.mark, key.mark))

            # If this key starts a new block mapping, we need to add
            # BLOCK-MAPPING-START.
            if not self.flow_level:
                if self.add_indent(key.column):
                    self.tokens.insert(
                        key.token_number-self.tokens_taken,
                        BlockMappingStartToken(key.mark, key.mark))

            # There cannot be two simple keys one after another.
            self.allow_simple_key = False

        # It must be a part of a complex key.
        else:

            # Block context needs additional checks.
            # (Do we really need them? They will be catched by the parser
            # anyway.)
            if not self.flow_level:

                # We are allowed to start a complex value if and only if
                # we can start a simple key.
                if not self.allow_simple_key:
                    raise ScannerError(None, None,
                                       "mapping values are not allowed here",
                                       self.reader.get_mark())

            # If this value starts a new block mapping, we need to add
            # BLOCK-MAPPING-START.  It will be detected as an error later by
            # the parser.
            if not self.flow_level:
                if self.add_indent(self.reader.column):
                    mark = self.reader.get_mark()
                    self.tokens.append(BlockMappingStartToken(mark, mark))

            # Simple keys are allowed after ':' in the block context.
            self.allow_simple_key = not self.flow_level

            # Reset possible simple key on the current level.
            self.remove_possible_simple_key()

        # Add VALUE.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        end_mark = self.reader.get_mark()
        self.tokens.append(ValueToken(start_mark, end_mark))

    def fetch_alias(self):
        # type: () -> None
        # ALIAS could be a simple key.
        self.save_possible_simple_key()
        # No simple keys after ALIAS.
        self.allow_simple_key = False
        # Scan and add ALIAS.
        self.tokens.append(self.scan_anchor(AliasToken))

    def fetch_anchor(self):
        # type: () -> None
        # ANCHOR could start a simple key.
        self.save_possible_simple_key()
        # No simple keys after ANCHOR.
        self.allow_simple_key = False
        # Scan and add ANCHOR.
        self.tokens.append(self.scan_anchor(AnchorToken))

    def fetch_tag(self):
        # type: () -> None
        # TAG could start a simple key.
        self.save_possible_simple_key()
        # No simple keys after TAG.
        self.allow_simple_key = False
        # Scan and add TAG.
        self.tokens.append(self.scan_tag())

    def fetch_literal(self):
        # type: () -> None
        self.fetch_block_scalar(style='|')

    def fetch_folded(self):
        # type: () -> None
        self.fetch_block_scalar(style='>')

    def fetch_block_scalar(self, style):
        # type: (Any) -> None
        # A simple key may follow a block scalar.
        self.allow_simple_key = True
        # Reset possible simple key on the current level.
        self.remove_possible_simple_key()
        # Scan and add SCALAR.
        self.tokens.append(self.scan_block_scalar(style))

    def fetch_single(self):
        # type: () -> None
        self.fetch_flow_scalar(style='\'')

    def fetch_double(self):
        # type: () -> None
        self.fetch_flow_scalar(style='"')

    def fetch_flow_scalar(self, style):
        # type: (Any) -> None
        # A flow scalar could be a simple key.
        self.save_possible_simple_key()
        # No simple keys after flow scalars.
        self.allow_simple_key = False
        # Scan and add SCALAR.
        self.tokens.append(self.scan_flow_scalar(style))

    def fetch_plain(self):
        # type: () -> None
        # A plain scalar could be a simple key.
        self.save_possible_simple_key()
        # No simple keys after plain scalars. But note that `scan_plain` will
        # change this flag if the scan is finished at the beginning of the
        # line.
        self.allow_simple_key = False
        # Scan and add SCALAR. May change `allow_simple_key`.
        self.tokens.append(self.scan_plain())

    # Checkers.

    def check_directive(self):
        # type: () -> Any
        # DIRECTIVE:        ^ '%' ...
        # The '%' indicator is already checked.
        if self.reader.column == 0:
            return True
        return None

    def check_document_start(self):
        # type: () -> Any
        # DOCUMENT-START:   ^ '---' (' '|'\n')
        if self.reader.column == 0:
            if self.reader.prefix(3) == u'---'  \
                    and self.reader.peek(3) in u'\0 \t\r\n\x85\u2028\u2029':
                return True
        return None

    def check_document_end(self):
        # type: () -> Any
        # DOCUMENT-END:     ^ '...' (' '|'\n')
        if self.reader.column == 0:
            if self.reader.prefix(3) == u'...'  \
                    and self.reader.peek(3) in u'\0 \t\r\n\x85\u2028\u2029':
                return True
        return None

    def check_block_entry(self):
        # type: () -> Any
        # BLOCK-ENTRY:      '-' (' '|'\n')
        return self.reader.peek(1) in u'\0 \t\r\n\x85\u2028\u2029'

    def check_key(self):
        # type: () -> Any
        # KEY(flow context):    '?'
        if bool(self.flow_level):
            return True
        # KEY(block context):   '?' (' '|'\n')
        return self.reader.peek(1) in u'\0 \t\r\n\x85\u2028\u2029'

    def check_value(self):
        # type: () -> Any
        # VALUE(flow context):  ':'
        if bool(self.flow_level):
            return True
        # VALUE(block context): ':' (' '|'\n')
        return self.reader.peek(1) in u'\0 \t\r\n\x85\u2028\u2029'

    def check_plain(self):
        # type: () -> Any
        # A plain scalar may start with any non-space character except:
        #   '-', '?', ':', ',', '[', ']', '{', '}',
        #   '#', '&', '*', '!', '|', '>', '\'', '\"',
        #   '%', '@', '`'.
        #
        # It may also start with
        #   '-', '?', ':'
        # if it is followed by a non-space character.
        #
        # Note that we limit the last rule to the block context (except the
        # '-' character) because we want the flow context to be space
        # independent.
        ch = self.reader.peek()
        return ch not in u'\0 \t\r\n\x85\u2028\u2029-?:,[]{}#&*!|>\'\"%@`' or \
            (self.reader.peek(1) not in u'\0 \t\r\n\x85\u2028\u2029' and
             (ch == u'-' or (not self.flow_level and ch in u'?:')))

    # Scanners.

    def scan_to_next_token(self):
        # type: () -> Any
        # We ignore spaces, line breaks and comments.
        # If we find a line break in the block context, we set the flag
        # `allow_simple_key` on.
        # The byte order mark is stripped if it's the first character in the
        # stream. We do not yet support BOM inside the stream as the
        # specification requires. Any such mark will be considered as a part
        # of the document.
        #
        # TODO: We need to make tab handling rules more sane. A good rule is
        #   Tabs cannot precede tokens
        #   BLOCK-SEQUENCE-START, BLOCK-MAPPING-START, BLOCK-END,
        #   KEY(block), VALUE(block), BLOCK-ENTRY
        # So the checking code is
        #   if <TAB>:
        #       self.allow_simple_keys = False
        # We also need to add the check for `allow_simple_keys == True` to
        # `unwind_indent` before issuing BLOCK-END.
        # Scanners for block, flow, and plain scalars need to be modified.

        if self.reader.index == 0 and self.reader.peek() == u'\uFEFF':
            self.reader.forward()
        found = False
        while not found:
            while self.reader.peek() == u' ':
                self.reader.forward()
            if self.reader.peek() == u'#':
                while self.reader.peek() not in u'\0\r\n\x85\u2028\u2029':
                    self.reader.forward()
            if self.scan_line_break():
                if not self.flow_level:
                    self.allow_simple_key = True
            else:
                found = True
        return None

    def scan_directive(self):
        # type: () -> Any
        # See the specification for details.
        start_mark = self.reader.get_mark()
        self.reader.forward()
        name = self.scan_directive_name(start_mark)
        value = None
        if name == u'YAML':
            value = self.scan_yaml_directive_value(start_mark)
            end_mark = self.reader.get_mark()
        elif name == u'TAG':
            value = self.scan_tag_directive_value(start_mark)
            end_mark = self.reader.get_mark()
        else:
            end_mark = self.reader.get_mark()
            while self.reader.peek() not in u'\0\r\n\x85\u2028\u2029':
                self.reader.forward()
        self.scan_directive_ignored_line(start_mark)
        return DirectiveToken(name, value, start_mark, end_mark)

    def scan_directive_name(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        length = 0
        ch = self.reader.peek(length)
        while u'0' <= ch <= u'9' or u'A' <= ch <= u'Z' or u'a' <= ch <= u'z' \
                or ch in u'-_:.':
            length += 1
            ch = self.reader.peek(length)
        if not length:
            raise ScannerError(
                "while scanning a directive", start_mark,
                "expected alphabetic or numeric character, but found %r"
                % utf8(ch), self.reader.get_mark())
        value = self.reader.prefix(length)
        self.reader.forward(length)
        ch = self.reader.peek()
        if ch not in u'\0 \r\n\x85\u2028\u2029':
            raise ScannerError(
                "while scanning a directive", start_mark,
                "expected alphabetic or numeric character, but found %r"
                % utf8(ch), self.reader.get_mark())
        return value

    def scan_yaml_directive_value(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        while self.reader.peek() == u' ':
            self.reader.forward()
        major = self.scan_yaml_directive_number(start_mark)
        if self.reader.peek() != '.':
            raise ScannerError(
                "while scanning a directive", start_mark,
                "expected a digit or '.', but found %r"
                % utf8(self.reader.peek()),
                self.reader.get_mark())
        self.reader.forward()
        minor = self.scan_yaml_directive_number(start_mark)
        if self.reader.peek() not in u'\0 \r\n\x85\u2028\u2029':
            raise ScannerError(
                "while scanning a directive", start_mark,
                "expected a digit or ' ', but found %r"
                % utf8(self.reader.peek()),
                self.reader.get_mark())
        return (major, minor)

    def scan_yaml_directive_number(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        ch = self.reader.peek()
        if not (u'0' <= ch <= u'9'):
            raise ScannerError(
                "while scanning a directive", start_mark,
                "expected a digit, but found %r" % utf8(ch),
                self.reader.get_mark())
        length = 0
        while u'0' <= self.reader.peek(length) <= u'9':
            length += 1
        value = int(self.reader.prefix(length))
        self.reader.forward(length)
        return value

    def scan_tag_directive_value(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        while self.reader.peek() == u' ':
            self.reader.forward()
        handle = self.scan_tag_directive_handle(start_mark)
        while self.reader.peek() == u' ':
            self.reader.forward()
        prefix = self.scan_tag_directive_prefix(start_mark)
        return (handle, prefix)

    def scan_tag_directive_handle(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        value = self.scan_tag_handle('directive', start_mark)
        ch = self.reader.peek()
        if ch != u' ':
            raise ScannerError("while scanning a directive", start_mark,
                               "expected ' ', but found %r" % utf8(ch),
                               self.reader.get_mark())
        return value

    def scan_tag_directive_prefix(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        value = self.scan_tag_uri('directive', start_mark)
        ch = self.reader.peek()
        if ch not in u'\0 \r\n\x85\u2028\u2029':
            raise ScannerError("while scanning a directive", start_mark,
                               "expected ' ', but found %r" % utf8(ch),
                               self.reader.get_mark())
        return value

    def scan_directive_ignored_line(self, start_mark):
        # type: (Any) -> None
        # See the specification for details.
        while self.reader.peek() == u' ':
            self.reader.forward()
        if self.reader.peek() == u'#':
            while self.reader.peek() not in u'\0\r\n\x85\u2028\u2029':
                self.reader.forward()
        ch = self.reader.peek()
        if ch not in u'\0\r\n\x85\u2028\u2029':
            raise ScannerError(
                "while scanning a directive", start_mark,
                "expected a comment or a line break, but found %r"
                % utf8(ch), self.reader.get_mark())
        self.scan_line_break()

    def scan_anchor(self, TokenClass):
        # type: (Any) -> Any
        # The specification does not restrict characters for anchors and
        # aliases. This may lead to problems, for instance, the document:
        #   [ *alias, value ]
        # can be interpteted in two ways, as
        #   [ "value" ]
        # and
        #   [ *alias , "value" ]
        # Therefore we restrict aliases to numbers and ASCII letters.
        start_mark = self.reader.get_mark()
        indicator = self.reader.peek()
        if indicator == u'*':
            name = 'alias'
        else:
            name = 'anchor'
        self.reader.forward()
        length = 0
        ch = self.reader.peek(length)
        # while u'0' <= ch <= u'9' or u'A' <= ch <= u'Z' or u'a' <= ch <= u'z' \
        #         or ch in u'-_':
        while check_anchorname_char(ch):
            length += 1
            ch = self.reader.peek(length)
        if not length:
            raise ScannerError(
                "while scanning an %s" % name, start_mark,
                "expected alphabetic or numeric character, but found %r"
                % utf8(ch), self.reader.get_mark())
        value = self.reader.prefix(length)
        self.reader.forward(length)
        # ch1 = ch
        # ch = self.reader.peek()   # no need to peek, ch is already set
        # assert ch1 == ch
        if ch not in u'\0 \t\r\n\x85\u2028\u2029?:,[]{}%@`':
            raise ScannerError(
                "while scanning an %s" % name, start_mark,
                "expected alphabetic or numeric character, but found %r"
                % utf8(ch), self.reader.get_mark())
        end_mark = self.reader.get_mark()
        return TokenClass(value, start_mark, end_mark)

    def scan_tag(self):
        # type: () -> Any
        # See the specification for details.
        start_mark = self.reader.get_mark()
        ch = self.reader.peek(1)
        if ch == u'<':
            handle = None
            self.reader.forward(2)
            suffix = self.scan_tag_uri('tag', start_mark)
            if self.reader.peek() != u'>':
                raise ScannerError(
                    "while parsing a tag", start_mark,
                    "expected '>', but found %r" % utf8(self.reader.peek()),
                    self.reader.get_mark())
            self.reader.forward()
        elif ch in u'\0 \t\r\n\x85\u2028\u2029':
            handle = None
            suffix = u'!'
            self.reader.forward()
        else:
            length = 1
            use_handle = False
            while ch not in u'\0 \r\n\x85\u2028\u2029':
                if ch == u'!':
                    use_handle = True
                    break
                length += 1
                ch = self.reader.peek(length)
            handle = u'!'
            if use_handle:
                handle = self.scan_tag_handle('tag', start_mark)
            else:
                handle = u'!'
                self.reader.forward()
            suffix = self.scan_tag_uri('tag', start_mark)
        ch = self.reader.peek()
        if ch not in u'\0 \r\n\x85\u2028\u2029':
            raise ScannerError("while scanning a tag", start_mark,
                               "expected ' ', but found %r" % utf8(ch),
                               self.reader.get_mark())
        value = (handle, suffix)
        end_mark = self.reader.get_mark()
        return TagToken(value, start_mark, end_mark)

    def scan_block_scalar(self, style):
        # type: (Any) -> Any
        # See the specification for details.
        if style == '>':
            folded = True
        else:
            folded = False

        chunks = []  # type: List[Any]
        start_mark = self.reader.get_mark()

        # Scan the header.
        self.reader.forward()
        chomping, increment = self.scan_block_scalar_indicators(start_mark)
        self.scan_block_scalar_ignored_line(start_mark)

        # Determine the indentation level and go to the first non-empty line.
        min_indent = self.indent+1
        if increment is None:
            # no increment and top level, min_indent could be 0
            if min_indent < 1 and \
               (style not in '|>' or (
                   self.scanner_processing_version == (1, 1)) and
                   getattr(self.loader,
                           'top_level_block_style_scalar_no_indent_error_1_1', False)):
                min_indent = 1
            breaks, max_indent, end_mark = self.scan_block_scalar_indentation()
            indent = max(min_indent, max_indent)
        else:
            if min_indent < 1:
                min_indent = 1
            indent = min_indent+increment-1
            breaks, end_mark = self.scan_block_scalar_breaks(indent)
        line_break = u''

        # Scan the inner part of the block scalar.
        while self.reader.column == indent and self.reader.peek() != u'\0':
            chunks.extend(breaks)
            leading_non_space = self.reader.peek() not in u' \t'
            length = 0
            while self.reader.peek(length) not in u'\0\r\n\x85\u2028\u2029':
                length += 1
            chunks.append(self.reader.prefix(length))
            self.reader.forward(length)
            line_break = self.scan_line_break()
            breaks, end_mark = self.scan_block_scalar_breaks(indent)
            if self.reader.column == indent and self.reader.peek() != u'\0':

                # Unfortunately, folding rules are ambiguous.
                #
                # This is the folding according to the specification:

                if folded and line_break == u'\n'   \
                        and leading_non_space and self.reader.peek() not in u' \t':
                    if not breaks:
                        chunks.append(u' ')
                else:
                    chunks.append(line_break)

                # This is Clark Evans's interpretation (also in the spec
                # examples):
                #
                # if folded and line_break == u'\n':
                #     if not breaks:
                #         if self.reader.peek() not in ' \t':
                #             chunks.append(u' ')
                #         else:
                #             chunks.append(line_break)
                # else:
                #     chunks.append(line_break)
            else:
                break

        # Process trailing line breaks. The 'chomping' setting determines
        # whether they are included in the value.
        trailing = []  # type: List[Any]
        if chomping in [None, True]:
            chunks.append(line_break)
        if chomping is True:
            chunks.extend(breaks)
        elif chomping in [None, False]:
            trailing.extend(breaks)

        # We are done.
        token = ScalarToken(u''.join(chunks), False, start_mark, end_mark, style)
        if len(trailing) > 0:
            # print('trailing 1', trailing)  # XXXXX
            # Eat whitespaces and comments until we reach the next token.
            comment = self.scan_to_next_token()
            while comment:
                trailing.append(comment[0])
                comment = self.scan_to_next_token()

            # Keep track of the trailing whitespace and following comments
            # as a comment token, if isn't all included in the actual value.
            comment_end_mark = self.reader.get_mark()
            comment = CommentToken(''.join(trailing), end_mark,
                                   comment_end_mark)
            token.add_post_comment(comment)
        return token

    def scan_block_scalar_indicators(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        chomping = None
        increment = None
        ch = self.reader.peek()
        if ch in u'+-':
            if ch == '+':
                chomping = True
            else:
                chomping = False
            self.reader.forward()
            ch = self.reader.peek()
            if ch in u'0123456789':
                increment = int(ch)
                if increment == 0:
                    raise ScannerError(
                        "while scanning a block scalar", start_mark,
                        "expected indentation indicator in the range 1-9, "
                        "but found 0", self.reader.get_mark())
                self.reader.forward()
        elif ch in u'0123456789':
            increment = int(ch)
            if increment == 0:
                raise ScannerError(
                    "while scanning a block scalar", start_mark,
                    "expected indentation indicator in the range 1-9, "
                    "but found 0",
                    self.reader.get_mark())
            self.reader.forward()
            ch = self.reader.peek()
            if ch in u'+-':
                if ch == '+':
                    chomping = True
                else:
                    chomping = False
                self.reader.forward()
        ch = self.reader.peek()
        if ch not in u'\0 \r\n\x85\u2028\u2029':
            raise ScannerError(
                "while scanning a block scalar", start_mark,
                "expected chomping or indentation indicators, but found %r"
                % utf8(ch), self.reader.get_mark())
        return chomping, increment

    def scan_block_scalar_ignored_line(self, start_mark):
        # type: (Any) -> Any
        # See the specification for details.
        while self.reader.peek() == u' ':
            self.reader.forward()
        if self.reader.peek() == u'#':
            while self.reader.peek() not in u'\0\r\n\x85\u2028\u2029':
                self.reader.forward()
        ch = self.reader.peek()
        if ch not in u'\0\r\n\x85\u2028\u2029':
            raise ScannerError(
                "while scanning a block scalar", start_mark,
                "expected a comment or a line break, but found %r"
                % utf8(ch), self.reader.get_mark())
        self.scan_line_break()

    def scan_block_scalar_indentation(self):
        # type: () -> Any
        # See the specification for details.
        chunks = []
        max_indent = 0
        end_mark = self.reader.get_mark()
        while self.reader.peek() in u' \r\n\x85\u2028\u2029':
            if self.reader.peek() != u' ':
                chunks.append(self.scan_line_break())
                end_mark = self.reader.get_mark()
            else:
                self.reader.forward()
                if self.reader.column > max_indent:
                    max_indent = self.reader.column
        return chunks, max_indent, end_mark

    def scan_block_scalar_breaks(self, indent):
        # type: (int) -> Any
        # See the specification for details.
        chunks = []
        end_mark = self.reader.get_mark()
        while self.reader.column < indent and self.reader.peek() == u' ':
            self.reader.forward()
        while self.reader.peek() in u'\r\n\x85\u2028\u2029':
            chunks.append(self.scan_line_break())
            end_mark = self.reader.get_mark()
            while self.reader.column < indent and self.reader.peek() == u' ':
                self.reader.forward()
        return chunks, end_mark

    def scan_flow_scalar(self, style):
        # type: (Any) -> Any
        # See the specification for details.
        # Note that we loose indentation rules for quoted scalars. Quoted
        # scalars don't need to adhere indentation because " and ' clearly
        # mark the beginning and the end of them. Therefore we are less
        # restrictive then the specification requires. We only need to check
        # that document separators are not included in scalars.
        if style == '"':
            double = True
        else:
            double = False
        chunks = []  # type: List[Any]
        start_mark = self.reader.get_mark()
        quote = self.reader.peek()
        self.reader.forward()
        chunks.extend(self.scan_flow_scalar_non_spaces(double, start_mark))
        while self.reader.peek() != quote:
            chunks.extend(self.scan_flow_scalar_spaces(double, start_mark))
            chunks.extend(self.scan_flow_scalar_non_spaces(double, start_mark))
        self.reader.forward()
        end_mark = self.reader.get_mark()
        return ScalarToken(u''.join(chunks), False, start_mark, end_mark,
                           style)

    ESCAPE_REPLACEMENTS = {
        u'0':   u'\0',
        u'a':   u'\x07',
        u'b':   u'\x08',
        u't':   u'\x09',
        u'\t':  u'\x09',
        u'n':   u'\x0A',
        u'v':   u'\x0B',
        u'f':   u'\x0C',
        u'r':   u'\x0D',
        u'e':   u'\x1B',
        u' ':   u'\x20',
        u'\"':  u'\"',
        u'/':   u'/',  # as per http://www.json.org/
        u'\\':  u'\\',
        u'N':   u'\x85',
        u'_':   u'\xA0',
        u'L':   u'\u2028',
        u'P':   u'\u2029',
    }

    ESCAPE_CODES = {
        u'x':   2,
        u'u':   4,
        u'U':   8,
    }

    def scan_flow_scalar_non_spaces(self, double, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        chunks = []  # type: List[Any]
        while True:
            length = 0
            while self.reader.peek(length) not in u'\'\"\\\0 \t\r\n\x85\u2028\u2029':
                length += 1
            if length != 0:
                chunks.append(self.reader.prefix(length))
                self.reader.forward(length)
            ch = self.reader.peek()
            if not double and ch == u'\'' and self.reader.peek(1) == u'\'':
                chunks.append(u'\'')
                self.reader.forward(2)
            elif (double and ch == u'\'') or (not double and ch in u'\"\\'):
                chunks.append(ch)
                self.reader.forward()
            elif double and ch == u'\\':
                self.reader.forward()
                ch = self.reader.peek()
                if ch in self.ESCAPE_REPLACEMENTS:
                    chunks.append(self.ESCAPE_REPLACEMENTS[ch])
                    self.reader.forward()
                elif ch in self.ESCAPE_CODES:
                    length = self.ESCAPE_CODES[ch]
                    self.reader.forward()
                    for k in range(length):
                        if self.reader.peek(k) not in u'0123456789ABCDEFabcdef':
                            raise ScannerError(
                                "while scanning a double-quoted scalar",
                                start_mark,
                                "expected escape sequence of %d hexdecimal "
                                "numbers, but found %r" %
                                (length, utf8(self.reader.peek(k))), self.reader.get_mark())
                    code = int(self.reader.prefix(length), 16)
                    chunks.append(unichr(code))
                    self.reader.forward(length)
                elif ch in u'\r\n\x85\u2028\u2029':
                    self.scan_line_break()
                    chunks.extend(self.scan_flow_scalar_breaks(
                        double, start_mark))
                else:
                    raise ScannerError(
                        "while scanning a double-quoted scalar", start_mark,
                        "found unknown escape character %r" % utf8(ch),
                        self.reader.get_mark())
            else:
                return chunks

    def scan_flow_scalar_spaces(self, double, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        chunks = []
        length = 0
        while self.reader.peek(length) in u' \t':
            length += 1
        whitespaces = self.reader.prefix(length)
        self.reader.forward(length)
        ch = self.reader.peek()
        if ch == u'\0':
            raise ScannerError(
                "while scanning a quoted scalar", start_mark,
                "found unexpected end of stream", self.reader.get_mark())
        elif ch in u'\r\n\x85\u2028\u2029':
            line_break = self.scan_line_break()
            breaks = self.scan_flow_scalar_breaks(double, start_mark)
            if line_break != u'\n':
                chunks.append(line_break)
            elif not breaks:
                chunks.append(u' ')
            chunks.extend(breaks)
        else:
            chunks.append(whitespaces)
        return chunks

    def scan_flow_scalar_breaks(self, double, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        chunks = []  # type: List[Any]
        while True:
            # Instead of checking indentation, we check for document
            # separators.
            prefix = self.reader.prefix(3)
            if (prefix == u'---' or prefix == u'...')   \
                    and self.reader.peek(3) in u'\0 \t\r\n\x85\u2028\u2029':
                raise ScannerError("while scanning a quoted scalar",
                                   start_mark,
                                   "found unexpected document separator",
                                   self.reader.get_mark())
            while self.reader.peek() in u' \t':
                self.reader.forward()
            if self.reader.peek() in u'\r\n\x85\u2028\u2029':
                chunks.append(self.scan_line_break())
            else:
                return chunks

    def scan_plain(self):
        # type: () -> Any
        # See the specification for details.
        # We add an additional restriction for the flow context:
        #   plain scalars in the flow context cannot contain ',', ': '  and '?'.
        # We also keep track of the `allow_simple_key` flag here.
        # Indentation rules are loosed for the flow context.
        chunks = []  # type: List[Any]
        start_mark = self.reader.get_mark()
        end_mark = start_mark
        indent = self.indent+1
        # We allow zero indentation for scalars, but then we need to check for
        # document separators at the beginning of the line.
        # if indent == 0:
        #     indent = 1
        spaces = []  # type: List[Any]
        while True:
            length = 0
            if self.reader.peek() == u'#':
                break
            while True:
                ch = self.reader.peek(length)
                if (ch == u':' and
                   self.reader.peek(length+1) not in u'\0 \t\r\n\x85\u2028\u2029'):
                    pass
                elif (ch in u'\0 \t\r\n\x85\u2028\u2029' or
                      (not self.flow_level and ch == u':' and
                          self.reader.peek(length+1) in u'\0 \t\r\n\x85\u2028\u2029') or
                      (self.flow_level and ch in u',:?[]{}')):
                    break
                length += 1
            # It's not clear what we should do with ':' in the flow context.
            if (self.flow_level and ch == u':' and
               self.reader.peek(length+1) not in u'\0 \t\r\n\x85\u2028\u2029,[]{}'):
                self.reader.forward(length)
                raise ScannerError(
                    "while scanning a plain scalar", start_mark,
                    "found unexpected ':'", self.reader.get_mark(),
                    "Please check "
                    "http://pyyaml.org/wiki/YAMLColonInFlowContext "
                    "for details.")
            if length == 0:
                break
            self.allow_simple_key = False
            chunks.extend(spaces)
            chunks.append(self.reader.prefix(length))
            self.reader.forward(length)
            end_mark = self.reader.get_mark()
            spaces = self.scan_plain_spaces(indent, start_mark)
            if not spaces or self.reader.peek() == u'#' \
                    or (not self.flow_level and self.reader.column < indent):
                break

        token = ScalarToken(u''.join(chunks), True, start_mark, end_mark)
        if spaces and spaces[0] == '\n':
            # Create a comment token to preserve the trailing line breaks.
            comment = CommentToken(''.join(spaces) + '\n', start_mark, end_mark)
            token.add_post_comment(comment)
        return token

    def scan_plain_spaces(self, indent, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        # The specification is really confusing about tabs in plain scalars.
        # We just forbid them completely. Do not use tabs in YAML!
        chunks = []
        length = 0
        while self.reader.peek(length) in u' ':
            length += 1
        whitespaces = self.reader.prefix(length)
        self.reader.forward(length)
        ch = self.reader.peek()
        if ch in u'\r\n\x85\u2028\u2029':
            line_break = self.scan_line_break()
            self.allow_simple_key = True
            prefix = self.reader.prefix(3)
            if (prefix == u'---' or prefix == u'...')   \
                    and self.reader.peek(3) in u'\0 \t\r\n\x85\u2028\u2029':
                return
            breaks = []
            while self.reader.peek() in u' \r\n\x85\u2028\u2029':
                if self.reader.peek() == ' ':
                    self.reader.forward()
                else:
                    breaks.append(self.scan_line_break())
                    prefix = self.reader.prefix(3)
                    if (prefix == u'---' or prefix == u'...')   \
                       and self.reader.peek(3) in u'\0 \t\r\n\x85\u2028\u2029':
                        return
            if line_break != u'\n':
                chunks.append(line_break)
            elif not breaks:
                chunks.append(u' ')
            chunks.extend(breaks)
        elif whitespaces:
            chunks.append(whitespaces)
        return chunks

    def scan_tag_handle(self, name, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        # For some strange reasons, the specification does not allow '_' in
        # tag handles. I have allowed it anyway.
        ch = self.reader.peek()
        if ch != u'!':
            raise ScannerError("while scanning a %s" % name, start_mark,
                               "expected '!', but found %r" % utf8(ch),
                               self.reader.get_mark())
        length = 1
        ch = self.reader.peek(length)
        if ch != u' ':
            while u'0' <= ch <= u'9' or u'A' <= ch <= u'Z' \
                  or u'a' <= ch <= u'z' \
                  or ch in u'-_':
                length += 1
                ch = self.reader.peek(length)
            if ch != u'!':
                self.reader.forward(length)
                raise ScannerError("while scanning a %s" % name, start_mark,
                                   "expected '!', but found %r" % utf8(ch),
                                   self.reader.get_mark())
            length += 1
        value = self.reader.prefix(length)
        self.reader.forward(length)
        return value

    def scan_tag_uri(self, name, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        # Note: we do not check if URI is well-formed.
        chunks = []
        length = 0
        ch = self.reader.peek(length)
        while u'0' <= ch <= u'9' or u'A' <= ch <= u'Z' or u'a' <= ch <= u'z'    \
                or ch in u'-;/?:@&=+$,_.!~*\'()[]%':
            if ch == u'%':
                chunks.append(self.reader.prefix(length))
                self.reader.forward(length)
                length = 0
                chunks.append(self.scan_uri_escapes(name, start_mark))
            else:
                length += 1
            ch = self.reader.peek(length)
        if length != 0:
            chunks.append(self.reader.prefix(length))
            self.reader.forward(length)
            length = 0
        if not chunks:
            raise ScannerError("while parsing a %s" % name, start_mark,
                               "expected URI, but found %r" % utf8(ch),
                               self.reader.get_mark())
        return u''.join(chunks)

    def scan_uri_escapes(self, name, start_mark):
        # type: (Any, Any) -> Any
        # See the specification for details.
        code_bytes = []  # type: List[Any]
        mark = self.reader.get_mark()
        while self.reader.peek() == u'%':
            self.reader.forward()
            for k in range(2):
                if self.reader.peek(k) not in u'0123456789ABCDEFabcdef':
                    raise ScannerError(
                        "while scanning a %s" % name, start_mark,
                        "expected URI escape sequence of 2 hexdecimal numbers,"
                        " but found %r"
                        % utf8(self.reader.peek(k)), self.reader.get_mark())
            if PY3:
                code_bytes.append(int(self.reader.prefix(2), 16))
            else:
                code_bytes.append(chr(int(self.reader.prefix(2), 16)))
            self.reader.forward(2)
        try:
            if PY3:
                value = bytes(code_bytes).decode('utf-8')
            else:
                value = unicode(''.join(code_bytes), 'utf-8')  # type: ignore
        except UnicodeDecodeError as exc:
            raise ScannerError("while scanning a %s" % name, start_mark,
                               str(exc), mark)
        return value

    def scan_line_break(self):
        # type: () -> Any
        # Transforms:
        #   '\r\n'      :   '\n'
        #   '\r'        :   '\n'
        #   '\n'        :   '\n'
        #   '\x85'      :   '\n'
        #   '\u2028'    :   '\u2028'
        #   '\u2029     :   '\u2029'
        #   default     :   ''
        ch = self.reader.peek()
        if ch in u'\r\n\x85':
            if self.reader.prefix(2) == u'\r\n':
                self.reader.forward(2)
            else:
                self.reader.forward()
            return u'\n'
        elif ch in u'\u2028\u2029':
            self.reader.forward()
            return ch
        return u''


class RoundTripScanner(Scanner):
    def check_token(self, *choices):
        # type: (Any) -> bool
        # Check if the next token is one of the given types.
        while self.need_more_tokens():
            self.fetch_more_tokens()
        self._gather_comments()
        if bool(self.tokens):
            if not choices:
                return True
            for choice in choices:
                if isinstance(self.tokens[0], choice):
                    return True
        return False

    def peek_token(self):
        # type: () -> Any
        # Return the next token, but do not delete if from the queue.
        while self.need_more_tokens():
            self.fetch_more_tokens()
        self._gather_comments()
        if bool(self.tokens):
            return self.tokens[0]
        return None

    def _gather_comments(self):
        # type: () -> Any
        """combine multiple comment lines"""
        comments = []  # type: List[Any]
        if not self.tokens:
            return comments
        if isinstance(self.tokens[0], CommentToken):
            comment = self.tokens.pop(0)
            self.tokens_taken += 1
            # print('################ dropping', comment)
            comments.append(comment)
        while self.need_more_tokens():
            self.fetch_more_tokens()
            if not self.tokens:
                return comments
            if isinstance(self.tokens[0], CommentToken):
                self.tokens_taken += 1
                comment = self.tokens.pop(0)
                # print 'dropping2', comment
                comments.append(comment)
        if len(comments) >= 1:
            # print('  len', len(comments), comments)
            # print('  com', comments[0], comments[0].start_mark.line)
            # print('  tok', self.tokens[0].end_mark.line)
            self.tokens[0].add_pre_comments(comments)
        # pull in post comment on e.g. ':'
        if not self.done and len(self.tokens) < 2:
            self.fetch_more_tokens()

    def get_token(self):
        # type: () -> Any
        # Return the next token.
        while self.need_more_tokens():
            self.fetch_more_tokens()
        self._gather_comments()
        if bool(self.tokens):
            # only add post comment to single line tokens:
            # scalar, value token. FlowXEndToken, otherwise
            # hidden streamtokens could get them (leave them and they will be
            # pre comments for the next map/seq
            if len(self.tokens) > 1 and \
               isinstance(self.tokens[0], (
                   ScalarToken,
                   ValueToken,
                   FlowSequenceEndToken,
                   FlowMappingEndToken,
                   )) and \
               isinstance(self.tokens[1], CommentToken) and \
               self.tokens[0].end_mark.line == self.tokens[1].start_mark.line:
                self.tokens_taken += 1
                self.tokens[0].add_post_comment(self.tokens.pop(1))
            self.tokens_taken += 1
            return self.tokens.pop(0)
        return None

    def fetch_comment(self, comment):
        # type: (Any) -> None
        value, start_mark, end_mark = comment
        while value and value[-1] == u' ':
            # empty line within indented key context
            # no need to update end-mark, that is not used
            value = value[:-1]
        self.tokens.append(CommentToken(value, start_mark, end_mark))

    # scanner

    def scan_to_next_token(self):
        # type: () -> Any
        # We ignore spaces, line breaks and comments.
        # If we find a line break in the block context, we set the flag
        # `allow_simple_key` on.
        # The byte order mark is stripped if it's the first character in the
        # stream. We do not yet support BOM inside the stream as the
        # specification requires. Any such mark will be considered as a part
        # of the document.
        #
        # TODO: We need to make tab handling rules more sane. A good rule is
        #   Tabs cannot precede tokens
        #   BLOCK-SEQUENCE-START, BLOCK-MAPPING-START, BLOCK-END,
        #   KEY(block), VALUE(block), BLOCK-ENTRY
        # So the checking code is
        #   if <TAB>:
        #       self.allow_simple_keys = False
        # We also need to add the check for `allow_simple_keys == True` to
        # `unwind_indent` before issuing BLOCK-END.
        # Scanners for block, flow, and plain scalars need to be modified.

        if self.reader.index == 0 and self.reader.peek() == u'\uFEFF':
            self.reader.forward()
        found = False
        while not found:
            while self.reader.peek() == u' ':
                self.reader.forward()
            ch = self.reader.peek()
            if ch == u'#':
                start_mark = self.reader.get_mark()
                comment = ch
                self.reader.forward()
                while ch not in u'\0\r\n\x85\u2028\u2029':
                    ch = self.reader.peek()
                    if ch == u'\0':  # don't gobble the end-of-stream character
                        break
                    comment += ch
                    self.reader.forward()
                # gather any blank lines following the comment too
                ch = self.scan_line_break()
                while len(ch) > 0:
                    comment += ch
                    ch = self.scan_line_break()
                end_mark = self.reader.get_mark()
                if not self.flow_level:
                    self.allow_simple_key = True
                return comment, start_mark, end_mark
            if bool(self.scan_line_break()):
                start_mark = self.reader.get_mark()
                if not self.flow_level:
                    self.allow_simple_key = True
                ch = self.reader.peek()
                if ch == '\n':    # empty toplevel lines
                    start_mark = self.reader.get_mark()
                    comment = ''
                    while ch:
                        ch = self.scan_line_break(empty_line=True)
                        comment += ch
                    if self.reader.peek() == '#':
                        # empty line followed by indented real comment
                        comment = comment.rsplit('\n', 1)[0] + '\n'
                    end_mark = self.reader.get_mark()
                    return comment, start_mark, end_mark
            else:
                found = True
        return None

    def scan_line_break(self, empty_line=False):
        # type: (bool) -> Text
        # Transforms:
        #   '\r\n'      :   '\n'
        #   '\r'        :   '\n'
        #   '\n'        :   '\n'
        #   '\x85'      :   '\n'
        #   '\u2028'    :   '\u2028'
        #   '\u2029     :   '\u2029'
        #   default     :   ''
        ch = self.reader.peek()  # type: Text
        if ch in u'\r\n\x85':
            if self.reader.prefix(2) == u'\r\n':
                self.reader.forward(2)
            else:
                self.reader.forward()
            return u'\n'
        elif ch in u'\u2028\u2029':
            self.reader.forward()
            return ch
        elif empty_line and ch in '\t ':
            self.reader.forward()
            return ch
        return u''

# try:
#     import psyco
#     psyco.bind(Scanner)
# except ImportError:
#     pass
