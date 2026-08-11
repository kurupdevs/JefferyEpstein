"""
Userbot helper scripts and utility functions.

Provides common helpers used across modules, including
progress callbacks, formatting utilities, and helper
wrappers around Pyrogram types.
"""

import asyncio
import time
from typing import Optional


async def progress_bar(
    current: int,
    total: int,
    message,
    start_time: float,
    prefix: str = "",
) -> None:
    """Update a Telegram message with an animated progress bar.

    Args:
        current: Bytes transferred so far.
        total: Total bytes to transfer.
        message: Pyrogram :class:`Message` object to edit.
        start_time: ``time.time()`` from when the transfer began.
        prefix: Optional label shown before the progress bar.
    """
    now = time.time()
    elapsed = now - start_time
    percent = current / total * 100
    speed = current / elapsed if elapsed > 0 else 0
    eta = (total - current) / speed if speed > 0 else 0

    bar_length = 10
    filled = int(bar_length * current / total)
    bar = "█" * filled + "░" * (bar_length - filled)

    text = (
        f"{prefix}\n"
        f"[{bar}] {percent:.1f}%\n"
        f"{_human_size(current)} / {_human_size(total)} @ {_human_size(speed)}/s\n"
        f"ETA: {_format_time(eta)}"
    )
    try:
        await message.edit(text)
    except Exception:
        pass


def _human_size(size: float) -> str:
    """Convert a byte count to a human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def _format_time(seconds: float) -> str:
    """Format seconds into ``MM:SS`` or ``HH:MM:SS``."""
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"
