# Jeffery Epstein x Kurup - Group Management
import asyncio
from datetime import datetime, timedelta
from contextlib import suppress
from pyrogram import Client, ContinuePropagation, filters
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid, RPCError
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from utils import modules_help, prefix
from utils.db import db
from utils.scripts import format_exc, text, with_reply

@Client.on_message(filters.command(["ban"], prefix) & filters.me)
async def ban_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]:
        return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message:
        u = message.reply_to_message.from_user or message.reply_to_message.sender_chat
        if u: user_id, name = u.id, (u.first_name if hasattr(u, 'first_name') else u.title)
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except:
            return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.edit(f"<b>{name}</b> banned!")
    except (UserAdminInvalid, ChatAdminRequired): await message.edit("<b>No admin rights!</b>")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["unban"], prefix) & filters.me)
async def unban_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id, name = message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except: return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.unban_chat_member(message.chat.id, user_id)
        await message.edit(f"<b>{name}</b> unbanned!")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["kick"], prefix) & filters.me)
async def kick_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id, name = message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except: return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.ban_chat_member(message.chat.id, user_id, datetime.now() + timedelta(seconds=31))
        await client.unban_chat_member(message.chat.id, user_id)
        await message.edit(f"<b>{name}</b> kicked!")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["mute"], prefix) & filters.me)
async def mute_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id, name = message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except: return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions())
        await message.edit(f"<b>{name}</b> muted!")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["unmute"], prefix) & filters.me)
async def unmute_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id, name = message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except: return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True))
        await message.edit(f"<b>{name}</b> unmuted!")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["promote"], prefix) & filters.me)
async def promote_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id, name = message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except: return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.promote_chat_member(message.chat.id, user_id, privileges=ChatPrivileges(can_manage_chat=True, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True, can_manage_video_chats=True))
        await message.edit(f"<b>{name}</b> promoted!")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["demote"], prefix) & filters.me)
async def demote_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    cause = text(message)
    user_id = name = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id, name = message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name
    elif len(cause.split()) > 1:
        try:
            u = await client.get_users(cause.split()[1])
            user_id, name = u.id, u.first_name
        except: return await message.edit("<b>User not found!</b>")
    if not user_id: return await message.edit("<b>Reply to user or provide ID!</b>")
    try:
        await client.promote_chat_member(message.chat.id, user_id, privileges=ChatPrivileges())
        await message.edit(f"<b>{name}</b> demoted!")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["pin"], prefix) & filters.me)
@with_reply
async def pin_cmd(_, message):
    try: await message.reply_to_message.pin(); await message.edit("<b>Pinned!</b>")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["unpin"], prefix) & filters.me)
@with_reply
async def unpin_cmd(_, message):
    try: await message.reply_to_message.unpin(); await message.edit("<b>Unpinned!</b>")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["unpinall"], prefix) & filters.me)
async def unpin_all(client, message):
    try: await client.unpin_all_chat_messages(message.chat.id); await message.edit("<b>Done!</b>")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["purge"], prefix) & filters.me)
@with_reply
async def purge_cmd(client, message):
    chunk = []
    async for msg in client.get_chat_history(chat_id=message.chat.id, limit=message.id - message.reply_to_message.id + 1):
        if msg.id < message.reply_to_message.id: break
        chunk.append(msg.id)
        if len(chunk) >= 100: await client.delete_messages(message.chat.id, chunk); chunk.clear(); await asyncio.sleep(1)
    if chunk: await client.delete_messages(message.chat.id, chunk)
    await message.delete()

@Client.on_message(filters.command(["del", "d"], prefix) & filters.me)
@with_reply
async def del_cmd(_, message): await message.delete(); await message.reply_to_message.delete()

@Client.on_message(filters.command(["ro"], prefix) & filters.me)
async def ro_cmd(client, message):
    if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]: return await message.edit("<b>Not supported!</b>")
    try: await client.set_chat_permissions(message.chat.id, ChatPermissions()); await message.edit(f"<b>RO ON! {prefix}unro to disable</b>")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["unro"], prefix) & filters.me)
async def unro_cmd(client, message):
    if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]: return await message.edit("<b>Not supported!</b>")
    try: await client.set_chat_permissions(message.chat.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)); await message.edit("<b>RO OFF!</b>")
    except Exception as e: await message.edit(format_exc(e))

@Client.on_message(filters.command(["antich"], prefix) & filters.me)
async def antich_cmd(_, message):
    cur = db.get("core.management", f"antich{message.chat.id}", False); db.set("core.management", f"antich{message.chat.id}", not cur)
    await message.edit(f"<b>Anti-channel {'ON' if not cur else 'OFF'}!</b>")

@Client.on_message(filters.command(["antiraid"], prefix) & filters.me)
async def antiraid_cmd(_, message):
    cur = db.get("core.management", f"antiraid{message.chat.id}", False); db.set("core.management", f"antiraid{message.chat.id}", not cur)
    await message.edit(f"<b>Anti-raid {'ON' if not cur else 'OFF'}!</b>")

@Client.on_message(filters.command(["kickdel"], prefix) & filters.me)
async def kickdel_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    await message.edit("<b>Scanning...</b>"); count = 0
    async for m in client.get_chat_members(message.chat.id):
        if m.user.is_deleted:
            try: await client.ban_chat_member(message.chat.id, m.user.id, datetime.now() + timedelta(seconds=31)); await client.unban_chat_member(message.chat.id, m.user.id); count += 1
            except: pass
    await message.edit(f"<b>Kicked {count} deleted!</b>")

@Client.on_message(filters.command(["zombies"], prefix) & filters.me)
async def zombies_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    await message.edit("<b>Scanning...</b>"); z = []
    async for m in client.get_chat_members(message.chat.id):
        if m.user.is_deleted: z.append(m.user.id)
    await message.edit(f"<b>{len(z)} zombie(s)!</b>" if z else "<b>No zombies!</b>")

@Client.on_message(filters.command(["tagall", "all"], prefix) & filters.me)
async def tagall_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    txt = " ".join(message.command[1:]) if len(message.command) > 1 else "Attention!"
    await message.edit("<b>Tagging...</b>"); mentions = []
    async for m in client.get_chat_members(message.chat.id):
        if m.user.is_bot: continue
        mentions.append(f"<a href='tg://user?id={m.user.id}'>\u200b</a>")
        if len(mentions) == 5:
            try: await client.send_message(message.chat.id, txt + " " + "".join(mentions))
            except: pass
            mentions.clear(); await asyncio.sleep(1)
    if mentions:
        try: await client.send_message(message.chat.id, txt + " " + "".join(mentions))
        except: pass
    await message.delete()

@Client.on_message(filters.command(["unbanall"], prefix) & filters.me)
async def unbanall_cmd(client, message):
    if message.chat.type in [ChatType.PRIVATE, ChatType.CHANNEL]: return await message.edit("<b>Not supported!</b>")
    await message.edit("<b>Unbanning...</b>"); count = 0
    async for m in client.get_chat_members(message.chat.id, filter="banned"):
        try: await client.unban_chat_member(message.chat.id, m.user.id); count += 1
        except: pass
    await message.edit(f"<b>Unbanned {count}!</b>")

modules_help["management"] = {
    "ban [reply/id]*": "Ban", "unban [reply/id]*": "Unban", "kick [reply/id]*": "Kick",
    "mute [reply/id]*": "Mute", "unmute [reply/id]*": "Unmute",
    "promote [reply/id]*": "Promote", "demote [reply/id]*": "Demote",
    "pin [reply]*": "Pin", "unpin [reply]*": "Unpin", "unpinall": "Unpin all",
    "purge [reply]*": "Delete to reply", "del [reply]*": "Delete msg",
    "ro": "Read-only ON", "unro": "Read-only OFF",
    "antich": "Anti-channel", "antiraid": "Anti-raid",
    "kickdel": "Kick deleted", "zombies": "List zombies",
    "tagall [msg]": "Tag all", "unbanall": "Unban all",
}
