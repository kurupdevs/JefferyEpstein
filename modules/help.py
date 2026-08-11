"""Help module."""
from pyrogram import Client,filters

HELP="""**Commands:**
• .afk - AFK
• .alive - Uptime
• .ping - Latency
• .spam - Spam
• .fact - Facts
• .joke - Jokes
• .ban/.mute - Manage
• .help - Menu"""

async def setup(c):c.on_message(filters.command("help",prefixes=".")&filters.me)(h)
async def h(c,m):await m.edit(HELP)
