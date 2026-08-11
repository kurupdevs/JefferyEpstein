"""
Jeffery Epstein x Kurup Bot — All-in-One Telegram Userbot.

A fast, lightweight userbot built with Pyrogram that provides management,
fun commands, anti-PM protection, notes, and more.

Copyright (c) 2024-2026 KurupDevs
"""

import asyncio
import logging
import os

from pyrogram import Client

# ── Configuration ────────────────────────────────────────────
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# ── Logging ──────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("jeff_epstein")

# ── Client ───────────────────────────────────────────────────
app = Client(
    "jeff_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


async def main() -> None:
    """Start the userbot and wait indefinitely.

    Initialises the Pyrogram client connection and enters an
    infinite wait loop, keeping the bot alive until a signal
    is received.
    """
    await app.start()
    logger.info("JefferyEpstein Bot started!")
    await asyncio.Event().wait()


if __name__ == "__main__":
    app.run(main())
