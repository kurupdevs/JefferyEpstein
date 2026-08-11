"""
Group management commands for the JEK userbot.

Provides admin-style moderation commands that operate on
users via reply targeting: ban, unban, mute, and unmute.
"""

import logging

from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

logger = logging.getLogger(__name__)


async def setup(c: Client) -> None:
    """Register management command handlers.

    Args:
        c: The Pyrogram :class:`~pyrogram.Client` instance.
    """
    c.on_message(filters.command("ban", prefixes=".") & filters.me)(ban)
    c.on_message(filters.command("unban", prefixes=".") & filters.me)(unban)
    c.on_message(filters.command("mute", prefixes=".") & filters.me)(mute)
    c.on_message(filters.command("unmute", prefixes=".") & filters.me)(unmute)


async def ban(c: Client, m: Message) -> None:
    """Ban a user from the current group.

    Reply to a user's message with ``.ban`` to remove them
    from the group.

    Args:
        c: The Pyrogram client.
        m: The triggering message (must be a reply).
    """
    if not m.reply_to_message:
        await m.edit("Reply to a user.")
        return
    user = m.reply_to_message.from_user
    try:
        await c.ban_chat_member(m.chat.id, user.id)
        await m.edit(f"Banned {user.mention}")
    except Exception as e:
        logger.warning("Ban failed for %s: %s", user.id, e)
        await m.edit(f"Failed: {e}")


async def unban(c: Client, m: Message) -> None:
    """Unban a user from the current group.

    Reply to a previously banned user's message with
    ``.unban`` to lift the ban.

    Args:
        c: The Pyrogram client.
        m: The triggering message (must be a reply).
    """
    if not m.reply_to_message:
        await m.edit("Reply to a user.")
        return
    user = m.reply_to_message.from_user
    try:
        await c.unban_chat_member(m.chat.id, user.id)
        await m.edit(f"Unbanned {user.mention}")
    except Exception as e:
        logger.warning("Unban failed for %s: %s", user.id, e)
        await m.edit(f"Failed: {e}")


async def mute(c: Client, m: Message) -> None:
    """Mute a user by restricting their ability to send messages.

    Reply to a user's message with ``.mute`` to prevent them
    from sending messages in the group.

    Args:
        c: The Pyrogram client.
        m: The triggering message (must be a reply).
    """
    if not m.reply_to_message:
        await m.edit("Reply to a user.")
        return
    user = m.reply_to_message.from_user
    try:
        await c.restrict_chat_member(
            m.chat.id,
            user.id,
            ChatPermissions(can_send_messages=False),
        )
        await m.edit(f"Muted {user.mention}")
    except Exception as e:
        logger.warning("Mute failed for %s: %s", user.id, e)
        await m.edit(f"Failed: {e}")


async def unmute(c: Client, m: Message) -> None:
    """Unmute a user by restoring their ability to send messages.

    Reply to a muted user's message with ``.unmute`` to lift
    the restriction.

    Args:
        c: The Pyrogram client.
        m: The triggering message (must be a reply).
    """
    if not m.reply_to_message:
        await m.edit("Reply to a user.")
        return
    user = m.reply_to_message.from_user
    try:
        await c.restrict_chat_member(
            m.chat.id,
            user.id,
            ChatPermissions(can_send_messages=True),
        )
        await m.edit(f"Unmuted {user.mention}")
    except Exception as e:
        logger.warning("Unmute failed for %s: %s", user.id, e)
        await m.edit(f"Failed: {e}")
