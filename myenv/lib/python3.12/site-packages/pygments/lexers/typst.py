"""
    pygments.lexers.typst
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for Typst language.

    :copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words, bygroups, include
from pygments.token import Comment, Keyword, Name, String, Punctuation, \
    Whitespace, Generic, Operator, Number, Text

__all__ = ['TypstLexer']


class TypstLexer(RegexLexer):
    """
    For Typst code.
    """

    name = 'Typst'
    aliases = ['typst']
    filenames = ['*.typ']
    mimetypes = ['text/x-typst']
    url = 'https://typst.app'
    version_added = '2.18'

    tokens = {
        'root': [
            include('markup'),
        ],
        'common': [
            (r'[ \t]+', Whitespace),
            (r'((?!=[*_$`\-+0-9/<@\\#\[]|https?://).)+', Text),
        ],
        'markup': [
            include('comment'),
            (r'^\s*=+.*$', Generic.Heading),
            (r'[*][^*]*[*]', Generic.Strong),
            (r'_[^_]*_', Generic.Emph),
            (r'\$', Punctuation, 'maths'),
            (r'`[^`]*`', String.Backtick),  # inline code
            (r'^\s*-', Punctuation),  # unnumbered list
            (r'^\s*\+', Punctuation),  # numbered list
            (r'^\s*[0-9.]+', Punctuation),  # numbered list variant
            (r'^(\s*/\s+)([^:]+)(:)', bygroups(Punctuation, Name.Variable, Punctuation)),  # definitions
            (r'<[a-zA-Z_][a-zA-Z0-9_-]*>', Name.Label),  # label
            (r'@[a-zA-Z_][a-zA-Z0-9_-]*', Name.Label),  # reference
            (r'\\#', Text), # escaped
            (words(('#let', '#set', '#show'), suffix=r'\b'), Keyword.Declaration, 'inline_code'),
            (r'(#[a-zA-Z_][a-zA-Z0-9_]*)(\[)', bygroups(Name.Function, Punctuation), 'markup'),
            (r'(#[a-zA-Z_][a-zA-Z0-9_]*)(\()', bygroups(Name.Function, Punctuation), 'inline_code'),
            (r'#[a-zA-Z_][a-zA-Z0-9_]*', Name.Variable),
            (r'```(?:.|\n)*?```', String.Backtick),  # code block
            (r'https?://[0-9a-zA-Z~/%#&=\',;.+?]*', Generic.Emph),  # links
            (words((r'---', r'\\', r'~', r'--', r'...'), suffix=r'\b'), Punctuation),  # special chars shorthand
            (r'\\\[', Punctuation),  # escaped
            (r'\\\]', Punctuation),  # escaped
            (r'\[', Punctuation, '#push'),
            (r'\]', Punctuation, '#pop'),
            include('common'),
        ],
        'maths': [
            include('comment'),
            (words(('_', '^', '+', '-', '/', '*', '->', '<-', '!=', '=='),
                   suffix=r'\b'), Operator),
            (words((r'\\', '$='), suffix=r'\b'), Operator),  # maths markup operators
            (r'\\\$', Punctuation),  # escaped
            (r'\$', Punctuation, '#pop'),  # end of math mode
            include('code'),
        ],
        'comment': [
            (r'//.*$', Comment.Single),
            (r'/[*](.|\n)*?[*]/', Comment.Multiline),
        ],
        'code': [
            include('comment'),
            (r'\[', Punctuation, 'markup'),
            (r'\(|\{', Punctuation, 'code'),
            (r'\)|\}', Punctuation, '#pop'),
            (r'"[^"]*"', String.Double),
            (r'[=,]', Operator),
            (words(('and', 'or', 'not'), suffix=r'\b'), Operator.Word),
            (r'=>|<=|==|!=|>|<|-=|\+=|\*=|/=|\+|-|\\|\*', Operator), # comparisons
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(:)', bygroups(Name.Variable, Punctuation), '#push'),
            (r'([a-zA-Z_][a-zA-Z0-9_]*)(\()', bygroups(Name.Function, Punctuation), '#push'),
            (words(('as', 'break', 'export', 'continue', 'else', 'for', 'if',
                    'import', 'in', 'include', 'return', 'while'), suffix=r'\b'),
             Keyword.Reserved),
            (words(('auto', 'none', 'true', 'false'), suffix=r'\b'), Keyword.Constant),
            (r'([0-9.]+)(mm|pt|cm|in|em|fr|%)', bygroups(Number, Keyword.Reserved)),
            (words(('let', 'set', 'show'), suffix=r'\b'), Keyword.Declaration),
            # FIXME: make this work
            ## (r'(import|include)( *)(")([^"])(")',
            ##  bygroups(Keyword.Reserved, Text, Punctuation, String.Double, Punctuation)),
            include('common'),
        ],
        'inline_code': [
            (r';$', Punctuation, '#pop'),
            include('code'),
        ],
    }
