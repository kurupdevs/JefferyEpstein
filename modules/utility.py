"""
Utility commands for the JEK userbot.

Provides miscellaneous helper commands such as info,
ID lookups, and other convenience wrappers.
"""

import logging

from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)


async def setup(c: Client) -> None:
    """Register utility command handlers.

    Args:
        c: The Pyrogram :class:`~pyrogram.Client` instance.
    """
    c.on_message(filters.command("id", prefixes=".") & filters.me)(get_id)
    c.on_message(filters.command("info", prefixes=".") & filters.me)(get_info)


async def get_id(c: Client, m: Message) -> None:
    """Return the chat and user ID for the current context.

    If replying to a message, shows both the chat ID and
    the replied user's ID. Otherwise shows just the chat ID.

    Args:
        c: The Pyrogram client.
        m: The triggering message.
    """
    text = f"**Chat ID:** `{m.chat.id}`"
    if m.reply_to_message:
        text += f"\n**User ID:** `{m.reply_to_message.from_user.id}`"
    await m.edit(text)


async def get_info(c: Client, m: Message) -> None:
    """Show information about a user or the current chat.

    If replying to a user, shows their profile info.
    Otherwise shows the current chat info.

    Args:
        c: The Pyrogram client.
        m: The triggering message.
    """
    if m.reply_to_message:
        user = m.reply_to_message.from_user
        text = (
            f"**User Info**\n"
            f"Name: {user.first_name}"
        )
        if user.last_name:
            text += f" {user.last_name}"
        text += f"\nID: `{user.id}`"
        if user.username:
            text += f"\nUsername: @{user.username}"
    else:
        text = (
            f"**Chat Info**\n"
            f"Title: {m.chat.title}\n"
            f"ID: `{m.chat.id}`\n"
            f"Type: {m.chat.type}"
        )
    await m.edit(text)
