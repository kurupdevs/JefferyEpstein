# Utility functions module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ping"))
async def ping_handler(client: Client, message: Message):
    await message.reply("Pong!")

@Client.on_message(filters.command("echo"))
async def echo_handler(client: Client, message: Message):
    text = " ".join(message.command[1:])
    if text:
        await message.reply(text)
