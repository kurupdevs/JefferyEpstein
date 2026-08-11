import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

AFK_USERS = {}


async def setup(client: Client):
    client.on_message(filters.command("afk", prefixes=".") & filters.me)(afk_handler)


async def afk_handler(client: Client, message: Message):
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK"
    AFK_USERS[message.from_user.id] = reason
    await message.edit(f"**I'm AFK now:** {reason}")
