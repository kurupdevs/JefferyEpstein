# Ping module
from pyrogram import Client, filters
from pyrogram.types import Message
import time

@Client.on_message(filters.command("ping"))
async def ping_handler(client: Client, message: Message):
    start = time.time()
    msg = await message.reply("Pong!")
    end = time.time()
    await msg.edit(f"Pong! `{round((end - start) * 1000, 2)}ms`")
