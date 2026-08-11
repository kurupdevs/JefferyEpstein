# JefferyEpsteinXKurup - Telegram Userbot
# A powerful all-in-one userbot

import os, sys, logging, time, asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", "0"))  # type: int
API_HASH = os.getenv("API_HASH", "")  # type: str

app = Client("jek_userbot", api_id=API_ID, api_hash=API_HASH)

async def main():
    """Main entry point."""
    await app.start()
    logger.info("JEK Userbot started!")  # Log
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
