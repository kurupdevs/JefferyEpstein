import random
from pyrogram import Client,filters

FACTS=["Honey never spoils.","A day on Venus > a year on Venus.","Octopuses have 3 hearts.","Bananas are berries."]
JOKES=["Why don't scientists trust atoms? They make up everything!","What do you call fake spaghetti? An impasta!","Why did the scarecrow win? He was outstanding!"]

async def setup(c):
 c.on_message(filters.command("fact",prefixes=".")&filters.me)(fa)
 c.on_message(filters.command("joke",prefixes=".")&filters.me)(jo)

async def fa(c,m):await m.edit(f"**Fact:** {random.choice(FACTS)}")
async def jo(c,m):await m.edit(f"**Joke:** {random.choice(JOKES)}")
