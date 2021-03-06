from talon import Context, Module, actions, app, ui

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
mode: user.c
mode: command
and code.language: c
"""

ctx.lists["user.snippets"] = {
    "define": "def",
    "if not define": "#ifndef:",
    "main": "main",
    "for loop": "for",
    "for eye loop": "fori",
    "else if": "eli",
    "print": "printf",
    "struct": "st",
    "function": "fun",
    "function declaration": "fund",
    "file header": "head",
    "function header": "func",
}
