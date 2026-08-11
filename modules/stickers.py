import os
from pyrogram import Client, filters
from pyrogram.types import Message

STICKER_DIR = "stickers"


async def setup(client: Client):
    client.on_message(filters.command("stickers", prefixes=".") & filters.me)(sticker_list)
    client.on_message(filters.command("kang", prefixes=".") & filters.me)(kang_sticker)


async def sticker_list(client: Client, message: Message):
    if not os.path.exists(STICKER_DIR):
        await message.edit("No stickers saved.")
        return
    stickers = os.listdir(STICKER_DIR)
    if not stickers:
        await message.edit("No stickers saved.")
        return
    text = "**Saved Stickers:**\n" + "\n".join(f"• `{s}`" for s in stickers)
    await message.edit(text)


async def kang_sticker(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.sticker:
        await message.edit("Reply to a sticker to kang it.")
        return
    os.makedirs(STICKER_DIR, exist_ok=True)
    sticker = message.reply_to_message.sticker
    path = os.path.join(STICKER_DIR, f"{sticker.file_unique_id}.webp")
    await client.download_media(sticker, file_name=path)
    await message.edit(f"**Kanged!** Saved as `{sticker.file_unique_id}.webp`")
