# Ping Module for JEK Userbot
import time, logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

async def setup(client: Client):
    client.on_message(filters.command("ping", prefixes=".") & filters.me)(ping_handler)

async def ping_handler(client: Client, message: Message):
    start = time.perf_counter()
    msg = await message.edit("**Pong!** 🏓")
    elapsed = (time.perf_counter() - start) * 1000
    await msg.edit(f"**Pong!** 🏓\nLatency: `{elapsed:.1f}ms`")  # Handle