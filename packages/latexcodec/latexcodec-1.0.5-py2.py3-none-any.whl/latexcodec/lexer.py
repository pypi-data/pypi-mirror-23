# -*- coding: utf-8 -*-
"""
    LaTeX Lexer
    ~~~~~~~~~~~

    This module contains all classes for lexing LaTeX code, as well as
    general purpose base classes for incremental LaTeX decoders and
    encoders, which could be useful in case you are writing your own
    custom LaTeX codec.

    .. autoclass:: Token(name, text)

    .. autoclass:: LatexLexer
       :show-inheritance:
       :members:

    .. autoclass:: LatexIncrementalLexer
       :show-inheritance:
       :members:

    .. autoclass:: LatexIncrementalDecoder
       :show-inheritance:
       :members:

    .. autoclass:: LatexIncrementalEncoder
       :show-inheritance:
       :members:
"""

# Copyright (c) 2003, 2008 David Eppstein
# Copyright (c) 2011-2014 Matthias C. M. Troffaes
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import codecs
import collections
import re
from six import add_metaclass, binary_type, string_types
import unicodedata


Token = collections.namedtuple("Token", "name text")


# implementation note: we derive from IncrementalDecoder because this
# class serves excellently as a base class for incremental decoders,
# but of course we don't decode yet until later


class MetaLatexCoder(type):

    def __init__(cls, name, bases, dct):
        super(MetaLatexCoder, cls).__init__(name, bases, dct)
        cls.emptytoken = Token(u"unknown", cls._fixit(b""))
        cls.partoken = Token("control_word", cls._fixit(b"\\par"))
        cls.spacetoken = Token("space", cls._fixit(b" "))
        cls.replacetoken = Token(
            "chars", b"?" if cls.binary_mode else u"\ufffd")
        cls.curlylefttoken = Token("chars", cls._fixit(b"{"))
        cls.curlyrighttoken = Token("chars", cls._fixit(b"}"))
        cls.emptychar = cls._fixit(b"")
        cls.spacechar = cls._fixit(b" ")
        cls.controlspacechar = cls._fixit(b"\\ ")

    def _fixit(cls, bytes_):
        return bytes_ if cls.binary_mode else bytes_.decode("ascii")


class MetaRegexpLexer(MetaLatexCoder):

    """Metaclass for :class:`RegexpLexer`. Compiles tokens into a
    regular expression.
    """

    def __init__(cls, name, bases, dct):
        super(MetaRegexpLexer, cls).__init__(name, bases, dct)
        regexp_string = cls._fixit(b"|".join(
            b"(?P<" + name.encode("ascii") + b">" + regexp + b")"
            for name, regexp in cls.tokens))
        cls.regexp = re.compile(regexp_string, re.DOTALL)


@add_metaclass(MetaRegexpLexer)
class RegexpLexer(codecs.IncrementalDecoder):

    """Abstract base class for regexp based lexers."""

    tokens = ()
    """Tuple containing all token regular expressions."""

    binary_mode = True
    """Whether this lexer processes binary data (bytes) or text data
    (unicode).
    """

    def __init__(self, errors='strict'):
        """Initialize the codec."""
        self.errors = errors
        self.reset()

    def reset(self):
        """Reset state."""
        # buffer for storing last (possibly incomplete) token
        self.raw_buffer = self.emptytoken

    def getstate(self):
        """Get state."""
        return (self.raw_buffer.text, 0)

    def setstate(self, state):
        """Set state. The *state* must correspond to the return value
        of a previous :meth:`getstate` call.
        """
        self.raw_buffer = Token('unknown', state[0])

    def get_raw_tokens(self, bytes_, final=False):
        """Yield tokens without any further processing. Tokens are one of:

        - ``\\<word>``: a control word (i.e. a command)
        - ``\\<symbol>``: a control symbol (i.e. \\^ etc.)
        - ``#<n>``: a parameter
        - a series of byte characters
        """
        if self.raw_buffer.text:
            bytes_ = self.raw_buffer.text + bytes_
        self.raw_buffer = self.emptytoken
        for match in self.regexp.finditer(bytes_):
            # yield the buffer token
            if self.raw_buffer.text:
                yield self.raw_buffer
            # fill buffer with next token
            self.raw_buffer = Token(match.lastgroup, match.group(0))
        if final:
            for token in self.flush_raw_tokens():
                yield token

    def flush_raw_tokens(self):
        """Flush the raw token buffer."""
        if self.raw_buffer.text:
            yield self.raw_buffer
            self.raw_buffer = self.emptytoken


class LatexLexer(RegexpLexer):

    """A very simple lexer for tex/latex bytes."""

    # implementation note: every token **must** be decodable by inputenc
    tokens = (
        # comment: for ease, and for speed, we handle it as a token
        (u'comment', br'(?<![\\])%[^\n]*'),
        # control tokens
        # in latex, some control tokens skip following whitespace
        # ('control-word' and 'control-symbol')
        # others do not ('control-symbol-x')
        # XXX TBT says no control symbols skip whitespace (except '\ ')
        # XXX but tests reveal otherwise?
        (u'control_word', br'[\\][a-zA-Z]+'),
        (u'control_symbol', br'[\\][~' br"'" br'"` =^!]'),
        # TODO should only match ascii
        (u'control_symbol_x', br'[\\][^a-zA-Z]'),
        # parameter tokens
        # also support a lone hash so we can lex things like b'#a'
        (u'parameter', br'\#[0-9]|\#'),
        # any remaining characters; for ease we also handle space and
        # newline as tokens
        # XXX TBT does not mention \t to be a space character as well
        # XXX but tests reveal otherwise?
        (u'space', br' |\t'),
        (u'newline', br'\n'),
        (u'mathshift', br'[$][$]|[$]'),
        # note: some chars joined together to make it easier to detect
        # symbols that have a special function (i.e. --, ---, etc.)
        (u'chars',
         br'---|--|-|[`][`]'
         br"|['][']"
         br'|[?][`]|[!][`]'
         # separate chars because brackets are optional
         # e.g. fran\\c cais = fran\\c{c}ais in latex
         # so only way to detect \\c acting on c only is this way
         br'|[0-9a-zA-Z{}]'
         # we have to join everything else together to support
         # multibyte encodings: every token must be decodable!!
         # this means for instance that \\c öké is NOT equivalent to
         # \\c{ö}ké
         br'|[^ %#$\n\\]+'),
        # trailing garbage which we cannot decode otherwise
        # (such as a lone '\' at the end of a buffer)
        # is never emitted, but used internally by the buffer
        (u'unknown', br'.'),
    )
    """List of token names, and the regular expressions they match."""


class LatexIncrementalLexer(LatexLexer):

    """A very simple incremental lexer for tex/latex code. Roughly
    follows the state machine described in Tex By Topic, Chapter 2.

    The generated tokens satisfy:

    * no newline characters: paragraphs are separated by '\\par'
    * spaces following control tokens are compressed
    """

    def reset(self):
        super(LatexIncrementalLexer, self).reset()
        # three possible states:
        # newline (N), skipping spaces (S), and middle of line (M)
        self.state = 'N'
        # inline math mode?
        self.inline_math = False

    def getstate(self):
        # state 'M' is most common, so let that be zero
        return (
            self.raw_buffer,
            {'M': 0, 'N': 1, 'S': 2}[self.state] |
            (4 if self.inline_math else 0)
        )

    def setstate(self, state):
        self.raw_buffer = state[0]
        self.state = {0: 'M', 1: 'N', 2: 'S'}[state[1] & 3]
        self.inline_math = bool(state[1] & 4)

    def get_tokens(self, bytes_, final=False):
        """Yield tokens while maintaining a state. Also skip
        whitespace after control words and (some) control symbols.
        Replaces newlines by spaces and \\par commands depending on
        the context.
        """
        # current position relative to the start of bytes_ in the sequence
        # of bytes that have been decoded
        pos = -len(self.raw_buffer.text)
        for token in self.get_raw_tokens(bytes_, final=final):
            pos = pos + len(token.text)
            assert pos >= 0  # first token includes at least self.raw_buffer
            if token.name == 'newline':
                if self.state == 'N':
                    # if state was 'N', generate new paragraph
                    yield self.partoken
                elif self.state == 'S':
                    # switch to 'N' state, do not generate a space
                    self.state = 'N'
                elif self.state == 'M':
                    # switch to 'N' state, generate a space
                    self.state = 'N'
                    yield self.spacetoken
                else:
                    raise AssertionError(
                        "unknown tex state {0!r}".format(self.state))
            elif token.name == 'space':
                if self.state == 'N':
                    # remain in 'N' state, no space token generated
                    pass
                elif self.state == 'S':
                    # remain in 'S' state, no space token generated
                    pass
                elif self.state == 'M':
                    # in M mode, generate the space,
                    # but switch to space skip mode
                    self.state = 'S'
                    yield token
                else:
                    raise AssertionError(
                        "unknown state {0!r}".format(self.state))
            elif token.name == 'mathshift':
                self.inline_math = not self.inline_math
                self.state = 'M'
                yield token
            elif token.name == 'parameter':
                self.state = 'M'
                yield token
            elif token.name == 'control_word':
                # go to space skip mode
                self.state = 'S'
                yield token
            elif token.name == 'control_symbol':
                # go to space skip mode
                self.state = 'S'
                yield token
            elif token.name == 'control_symbol_x':
                # don't skip following space, so go to M mode
                self.state = 'M'
                yield token
            elif token.name == 'comment':
                # no token is generated
                # note: comment does not include the newline
                self.state = 'S'
            elif token.name == 'chars':
                self.state = 'M'
                yield token
            elif token.name == 'unknown':
                if self.errors == 'strict':
                    # hack around a bug in Python: UnicodeDecodeError
                    # expects binary input
                    if not self.binary_mode:
                        bytes_ = bytes_.encode("utf8")
                    # current position within bytes_
                    # this is the position right after the unknown token
                    raise UnicodeDecodeError(
                        "latex",  # codec
                        bytes_,  # problematic input
                        pos - len(token.text),  # start of problematic token
                        pos,  # end of it
                        "unknown token {0!r}".format(token.text))
                elif self.errors == 'ignore':
                    # do nothing
                    pass
                elif self.errors == 'replace':
                    yield self.replacetoken
                else:
                    raise NotImplementedError(
                        "error mode {0!r} not supported".format(self.errors))
            else:
                raise AssertionError(
                    "unknown token name {0!r}".format(token.name))


class LatexIncrementalDecoder(LatexIncrementalLexer):

    """Simple incremental decoder. Transforms lexed LaTeX tokens into
    unicode.

    To customize decoding, subclass and override
    :meth:`get_unicode_tokens`.
    """

    inputenc = "ascii"
    """Input encoding. **Must** extend ascii."""

    def decode_token(self, token):
        """Returns the decoded token text in :attr:`inputenc` encoding.

        .. note::

           Control words get an extra space added at the back to make
           sure separation from the next token, so that decoded token
           sequences can be :meth:`str.join`\ ed together.

           For example, the tokens ``b'\\hello'`` and ``b'world'``
           will correctly result in ``u'\\hello world'`` (remember
           that LaTeX eats space following control words). If no space
           were added, this would wrongfully result in
           ``u'\\helloworld'``.

        """
        # in python 3, the token text can be a memoryview
        # which do not have a decode method; must cast to bytes explicitly
        if self.binary_mode:
            text = binary_type(token.text).decode(self.inputenc)
        else:
            text = token.text
        return text if token.name != 'control_word' else text + u' '

    def get_unicode_tokens(self, bytes_, final=False):
        """Decode every token in :attr:`inputenc` encoding. Override to
        process the tokens in some other way (for example, for token
        translation).
        """
        for token in self.get_tokens(bytes_, final=final):
            yield self.decode_token(token)

    def decode(self, bytes_, final=False):
        """Decode LaTeX *bytes_* into a unicode string.

        This implementation calls :meth:`get_unicode_tokens` and joins
        the resulting unicode strings together.
        """
        try:
            return u''.join(self.get_unicode_tokens(bytes_, final=final))
        except UnicodeDecodeError as e:
            # API requires that the encode method raises a ValueError
            # in this case
            raise ValueError(e)


@add_metaclass(MetaLatexCoder)
class LatexIncrementalEncoder(codecs.IncrementalEncoder):

    """Simple incremental encoder for LaTeX. Transforms unicode into
    :class:`bytes`.

    To customize decoding, subclass and override
    :meth:`get_latex_bytes`.
    """

    inputenc = "ascii"
    """Input encoding. **Must** extend ascii."""

    binary_mode = True
    """Whether this encoder processes binary data (bytes) or text data
    (unicode).
    """

    def __init__(self, errors='strict'):
        """Initialize the codec."""
        self.errors = errors
        self.reset()

    def reset(self):
        """Reset state."""
        # buffer for storing last (possibly incomplete) token
        self.buffer = u""

    def getstate(self):
        """Get state."""
        return self.buffer

    def setstate(self, state):
        """Set state. The *state* must correspond to the return value
        of a previous :meth:`getstate` call.
        """
        self.buffer = state

    def get_unicode_tokens(self, unicode_, final=False):
        """Split unicode into tokens so that every token starts with a
        non-combining character.
        """
        if not isinstance(unicode_, string_types):
            raise TypeError(
                "expected unicode for encode input, but got {0} instead"
                .format(unicode_.__class__.__name__))
        for c in unicode_:
            if not unicodedata.combining(c):
                for token in self.flush_unicode_tokens():
                    yield token
            self.buffer += c
        if final:
            for token in self.flush_unicode_tokens():
                yield token

    def flush_unicode_tokens(self):
        """Flush the buffer."""
        if self.buffer:
            yield self.buffer
            self.buffer = u""

    def get_latex_bytes(self, unicode_, final=False):
        """Encode every character in :attr:`inputenc` encoding. Override to
        process the unicode in some other way (for example, for character
        translation).
        """
        if self.binary_mode:
            for token in self.get_unicode_tokens(unicode_, final=final):
                yield token.encode(self.inputenc, self.errors)
        else:
            for token in self.get_unicode_tokens(unicode_, final=final):
                yield token

    def encode(self, unicode_, final=False):
        """Encode the *unicode_* string into LaTeX :class:`bytes`.

        This implementation calls :meth:`get_latex_bytes` and joins
        the resulting :class:`bytes` together.
        """
        try:
            return self.emptychar.join(
                self.get_latex_bytes(unicode_, final=final))
        except UnicodeEncodeError as e:
            # API requires that the encode method raises a ValueError
            # in this case
            raise ValueError(e)


class UnicodeLatexLexer(LatexLexer):
    binary_mode = False


class UnicodeLatexIncrementalDecoder(LatexIncrementalDecoder):
    binary_mode = False


class UnicodeLatexIncrementalEncoder(LatexIncrementalEncoder):
    binary_mode = False
