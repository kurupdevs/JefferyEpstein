# Help module for command listing
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("help"))
async def help_handler(client: Client, message: Message):
    await message.reply("Commands: /ping, /afk, /alive, /help, /spam")
