import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)


async def setup(client: Client):
    """Register extra commands."""
    client.on_message(filters.command("echo", prefixes=".") & filters.me)(echo_handler)
    client.on_message(filters.command("del", prefixes=".") & filters.me)(del_handler)
    client.on_message(filters.command("pin", prefixes=".") & filters.me)(pin_handler)
    client.on_message(filters.command("unpin", prefixes=".") & filters.me)(unpin_handler)


async def echo_handler(client: Client, message: Message):
    """Echo back the message text."""
    text = message.text.split(None, 1)
    if len(text) < 2:
        await message.edit("**Usage:** `.echo <text>`")
        return
    await message.edit(text[1])


async def del_handler(client: Client, message: Message):
    """Delete the replied message."""
    if message.reply_to_message:
        await message.reply_to_message.delete()
    await message.delete()


async def pin_handler(client: Client, message: Message):
    """Pin the replied message."""
    if not message.reply_to_message:
        await message.edit("Reply to a message to pin.")
        return
    await message.reply_to_message.pin()
    await message.edit("**Pinned!**")


async def unpin_handler(client: Client, message: Message):
    """Unpin all messages."""
    await client.unpin_all_chat_messages(message.chat.id)
    await message.edit("**Unpinned all!**")
