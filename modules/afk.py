# AFK Module for JefferyEpsteinXKurup
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("afk"))
async def afk_handler(client: Client, message: Message):
    await message.reply("I am now AFK!")
