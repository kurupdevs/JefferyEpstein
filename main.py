# Jeffery Epstein X Kurup Bot
# All in One Telegram Bot
# Copyright (c) 2024 KurupDevs

import asyncio
import os
from pyrogram import Client

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "jeff_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

async def main():
    """Start the bot and wait forever."""
    await app.start()
    print("JefferyEpstein Bot started!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    app.run(main())
