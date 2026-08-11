# Spam module for JefferyEpstein bot
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("spam"))
async def spam_handler(client: Client, message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.reply("Usage: /spam <count> <message>")
        return
    count = int(args[1])
    text = " ".join(args[2:])
    for _ in range(count):
        await message.reply(text)
