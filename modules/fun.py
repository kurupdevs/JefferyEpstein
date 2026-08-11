# Fun module
from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("joke"))
async def joke_handler(client: Client, message: Message):
    jokes = ["Why did the bot cross the road?", "Knock knock!"]
    await message.reply(random.choice(jokes))
