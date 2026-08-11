# Extra features module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("extra"))
async def extra_handler(client: Client, message: Message):
    await message.reply("Extra features enabled.")
