import asyncio,logging
from pyrogram import Client,filters
from pyrogram.types import Message,ChatPermissions

logger=logging.getLogger(__name__)

async def setup(c):
 c.on_message(filters.command("ban",prefixes=".")&filters.me)(ban)
 c.on_message(filters.command("unban",prefixes=".")&filters.me)(unban)
 c.on_message(filters.command("mute",prefixes=".")&filters.me)(mute)
 c.on_message(filters.command("unmute",prefixes=".")&filters.me)(unmute)

async def ban(c,m):
 if not m.reply_to_message:await m.edit("Reply to a user.");return
 u=m.reply_to_message.from_user
 try:await c.ban_chat_member(m.chat.id,u.id);await m.edit(f"Banned {u.mention}")
 except Exception as e:await m.edit(f"Failed: {e}")

async def unban(c,m):
 if not m.reply_to_message:await m.edit("Reply to a user.");return
 u=m.reply_to_message.from_user
 try:await c.unban_chat_member(m.chat.id,u.id);await m.edit(f"Unbanned {u.mention}")
 except Exception as e:await m.edit(f"Failed: {e}")

async def mute(c,m):
 if not m.reply_to_message:await m.edit("Reply to a user.");return
 u=m.reply_to_message.from_user
 try:await c.restrict_chat_member(m.chat.id,u.id,ChatPermissions(can_send_messages=False));await m.edit(f"Muted {u.mention}")
 except Exception as e:await m.edit(f"Failed: {e}")

async def unmute(c,m):
 if not m.reply_to_message:await m.edit("Reply to a user.");return
 u=m.reply_to_message.from_user
 try:await c.restrict_chat_member(m.chat.id,u.id,ChatPermissions(can_send_messages=True));await m.edit(f"Unmuted {u.mention}")
 except Exception as e:await m.edit(f"Failed: {e}")
