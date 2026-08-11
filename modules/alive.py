# Alive Module for JEK Userbot
import time, platform, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)
START_TIME = time.time()

async def setup(client: Client):
    client.on_message(filters.command("alive", prefixes=".") & filters.me)(alive_handler)

async def alive_handler(client: Client, message: Message):
    uptime = int(time.time() - START_TIME)
    h, r = divmod(uptime, 3600)
    m, s = divmod(r, 60)
    await message.edit(f"**JEK Userbot Alive!** ✅\nUptime: `{h}h {m}m {s}s`\nPlatform: `{platform.system()}`")  # Process