import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)


async def setup(client: Client):
    """Register utility commands."""
    client.on_message(filters.command("id", prefixes=".") & filters.me)(id_handler)
    client.on_message(filters.command("info", prefixes=".") & filters.me)(info_handler)
    client.on_message(filters.command("json", prefixes=".") & filters.me)(json_handler)


async def id_handler(client: Client, message: Message):
    """Get chat/user ID."""
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else message.from_user.id
    await message.edit(f"**Chat ID:** `{chat_id}`\n**User ID:** `{user_id}`")


async def info_handler(client: Client, message: Message):
    """Get user info."""
    user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    text = (
        f"**User Info:**\n"
        f"• Name: {user.first_name}\n"
        f"• ID: `{user.id}`\n"
        f"• Username: @{user.username or 'None'}\n"
        f"• Is Bot: {user.is_bot}"
    )
    await message.edit(text)


async def json_handler(client: Client, message: Message):
    """Show message JSON."""
    msg = message.reply_to_message or message
    await message.edit(f"```json\n{str(msg)}\n```")
