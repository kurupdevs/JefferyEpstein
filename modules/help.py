from pyrogram import Client,filters

HELP="""
**Commands:**
• .afk - Set AFK
• .alive - Uptime
• .ping - Latency
• .spam - Spam msg
• .fact - Random fact
• .joke - Random joke
• .ban/.unban - Manage
• .mute/.unmute - Manage
• .help - This menu
"""

async def setup(c):c.on_message(filters.command("help",prefixes=".")&filters.me)(h)
async def h(c,m):await m.edit(HELP)
