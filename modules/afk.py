# AFK Module for JEK Userbot
import time
from pyrogram import Client, filters
from pyrogram.types import Message

AFK_DB = {}

async def setup(client: Client):
    client.on_message(filters.command("afk", prefixes=".") & filters.me)(afk_handler)

async def afk_handler(client: Client, message: Message):
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "Away"
    AFK_DB[message.from_user.id] = {"reason": reason, "time": time.time()}
    await message.edit(f"**AFK Mode Active!**\nReason: {reason}")  # Handle