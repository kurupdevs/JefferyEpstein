# Stickers module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("sticker"))
async def sticker_handler(client: Client, message: Message):
    await message.reply("Sticker module active.")
