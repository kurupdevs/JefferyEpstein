"""
JEK Userbot module loader.

Imports and exposes all built-in modules for registration
by the main application.
"""

from . import afk, alive, antipm, extra, fun, help, management
from . import notes, ping, spam, stickers, utility

__all__ = [
    "afk",
    "alive",
    "antipm",
    "extra",
    "fun",
    "help",
    "management",
    "notes",
    "ping",
    "spam",
    "stickers",
    "utility",
]
