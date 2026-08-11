async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("ping",prefixes=".")&filters.me)(p)

async def p(c,m):
 import time;s=time.time();msg=await m.edit("Pong!");e=time.time()
 await msg.edit(f"Pong! `{round((e-s)*1000)}ms`")
