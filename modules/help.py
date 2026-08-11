# Help Module for JEK Userbot
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def setup(client: Client):
    client.on_message(filters.command("help", prefixes=".") & filters.me)(help_handler)

async def help_handler(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Channel", url="https://t.me/kurupdevs")]
    ])
    help_text = "**JEK Userbot Help**\n\n.ping - Check latency\n.alive - Bot status\n.spam - Spam messages\n.help - This menu"
    await message.edit(help_text, reply_markup=keyboard)  # Process