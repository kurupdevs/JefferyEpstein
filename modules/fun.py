# Jeffery Epstein x Kurup - Fun Module

import asyncio, random
from datetime import datetime
import aiohttp
from pyrogram import Client, filters
from utils import modules_help, prefix
from utils.scripts import get_text, with_reply

@Client.on_message(filters.command(["ping","p"],prefix)&filters.me)
async def ping(client,msg):
    s=datetime.now();m=await msg.edit("<b>Pong!</b>");e=datetime.now()
    await m.edit(f"<b>Pong!</b> <code>{(e-s).total_seconds()*1000:.0f}ms</code>")

@Client.on_message(filters.command(["alive"],prefix)&filters.me)
async def alive(client,msg):
    me=await client.get_me()
    await msg.edit(f"<b>Jeffery Epstein x Kurup v1.0</b>\n{me.mention}\nPrefix: <code>{prefix}</code>")

@Client.on_message(filters.command(["couples","couple"],prefix)&filters.me)
async def couples(client,msg):
    if msg.chat.type=="private":return await msg.edit("<b>Group only!</b>")
    await msg.edit("<b>Finding...</b>")
    members=[m.user async for m in client.get_chat_members(msg.chat.id,limit=50) if not m.user.is_bot]
    if len(members)<2:return await msg.edit("<b>Not enough!</b>")
    u1,u2=random.sample(members,2);love=random.randint(40,100)
    await msg.edit(f"<b>Couple:</b> {u1.mention} + {u2.mention}\n<b>Love:</b> {love}%")

@Client.on_message(filters.command(["dice"],prefix)&filters.me)
async def dice(client,msg):
    await client.send_dice(msg.chat.id,"🎲");await msg.delete()

@Client.on_message(filters.command(["truth"],prefix)&filters.me)
async def truth(_,msg):
    q=["Biggest fear?","First crush?","Last lie?","Embarrassing moment?","Secret talent?"]
    await msg.edit(f"<b>TRUTH:</b>\n<i>{random.choice(q)}</i>")

@Client.on_message(filters.command(["dare"],prefix)&filters.me)
async def dare(_,msg):
    d=["Send voice note singing!","Change name for 1hr!","Post selfie!","Send last 5 emojis!","No emojis for 1hr!"]
    await msg.edit(f"<b>DARE:</b>\n<i>{random.choice(d)}</i>")

@Client.on_message(filters.command(["joke"],prefix)&filters.me)
async def joke(_,msg):
    j=["Why don't scientists trust atoms? They make up everything!","Parallel lines have so much in common. Shame they'll never meet.","I told my wife she drew eyebrows too high. She looked surprised."]
    await msg.edit(f"<b>Joke:</b>\n<i>{random.choice(j)}</i>")

@Client.on_message(filters.command(["shayari"],prefix)&filters.me)
async def shayari(_,msg):
    s=["Zindagi ek kitaab hai ❤️","Mohabbat mein haar kar bhi jeetne ka maza 🌹"]
    await msg.edit(f"<b>Shayari:</b>\n<i>{random.choice(s)}</i>")

@Client.on_message(filters.command(["figlet"],prefix)&filters.me)
async def figlet(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}figlet [text]")
    try:import pyfiglet;r=pyfiglet.figlet_format(" ".join(msg.command[1:]));await msg.edit(f"<pre>{r}</pre>")
    except:await msg.edit("<b>Install pyfiglet!</b>")

@Client.on_message(filters.command(["hug"],prefix)&filters.me)
@with_reply
async def hug(_,msg):
    u=msg.reply_to_message.from_user;await msg.edit(f"{msg.from_user.mention} hugs {u.mention} 🤗")

@Client.on_message(filters.command(["slap"],prefix)&filters.me)
@with_reply
async def slap(_,msg):
    u=msg.reply_to_message.from_user;await msg.edit(f"{msg.from_user.mention} slaps {u.mention} 👋")

@Client.on_message(filters.command(["kiss"],prefix)&filters.me)
@with_reply
async def kiss(_,msg):
    u=msg.reply_to_message.from_user;await msg.edit(f"{msg.from_user.mention} kisses {u.mention} 😘")

@Client.on_message(filters.command(["fakeinfo"],prefix)&filters.me)
async def fakeinfo(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}fakeinfo [country]")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://randomuser.me/api/?nat={msg.command[1].upper()}") as r:d=(await r.json())["results"][0]
        await msg.edit(f"<b>ID:</b> {d['name']['first']} {d['name']['last']}\n<b>Email:</b> {d['email']}\n<b>Phone:</b> {d['phone']}")
    except Exception as e:await msg.edit(f"<b>Error:</b> {e}")

modules_help["fun"]={
    "ping":"Check latency","alive":"Bot status","couples":"Find couples","dice":"Roll dice",
    "truth":"Truth","dare":"Dare","joke":"Joke","shayari":"Shayari",
    "figlet [text]*":"ASCII","hug/slap/kiss [reply]*":"Actions","fakeinfo [country]*":"Fake ID",
}
