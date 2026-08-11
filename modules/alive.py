# Alive status module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("alive"))
async def alive_handler(client: Client, message: Message):
    await message.reply("I am alive! JEK Userbot running.")
