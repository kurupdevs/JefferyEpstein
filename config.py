"""
Application configuration loader.

Reads environment variables and provides them as module-level
constants for use throughout the userbot.
"""

import os

# ── Core Credentials ─────────────────────────────────────────
API_ID: int = int(os.getenv("API_ID", "0"))
"""Telegram API ID from https://my.telegram.org/apps."""

API_HASH: str = os.getenv("API_HASH", "")
"""Telegram API hash from https://my.telegram.org/apps."""

STRING_SESSION: str = os.getenv("STRING_SESSION", "")
"""Pyrogram string session for user authentication."""

# ── Optional Settings ────────────────────────────────────────
DATABASE_TYPE: str = os.getenv("DATABASE_TYPE", "sqlite")
"""Database backend type (default: sqlite)."""

DATABASE_NAME: str = os.getenv("DATABASE_NAME", "jeffery_epstein")
"""Database file or schema name."""

PM_LIMIT: int = int(os.getenv("PM_LIMIT", "4"))
"""Maximum private messages before anti-PM blocking kicks in."""

PREFIX: str = os.getenv("PREFIX", ".")
"""Default command prefix for the userbot."""
