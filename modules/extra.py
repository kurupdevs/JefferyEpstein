# Jeffery Epstein x Kurup - Extra
import aiohttp
from io import BytesIO
from pyrogram import Client,filters
from utils import modules_help,prefix
from utils.scripts import format_exc,with_reply,resize_image

@Client.on_message(filters.command(["reply","r"],prefix)&filters.me)
async def reply(_,msg):
    if not msg.reply_to_message or len(msg.command)<2:return await msg.edit("<b>Reply + text!</b>")
    await msg.delete();await msg.reply_to_message.reply(" ".join(msg.command[1:]))

@Client.on_message(filters.command(["copy"],prefix)&filters.me)
@with_reply
async def copy(client,msg):await msg.delete();await msg.reply_to_message.copy(msg.chat.id)

@Client.on_message(filters.command(["fwd","forward"],prefix)&filters.me)
@with_reply
async def fwd(client,msg):
    target=msg.command[1] if len(msg.command)>1 else None
    if not target:return await msg.edit(f"{prefix}fwd [chat] (reply)")
    try:await msg.reply_to_message.forward(int(target) if target.lstrip("-").isdigit() else target);await msg.edit("<b>Done!</b>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["whisper","wspr"],prefix)&filters.me)
async def whisper(client,msg):
    if len(msg.command)<3:return await msg.edit(f"{prefix}whisper [user] [text]")
    try:
        t=int(msg.command[1]) if msg.command[1].lstrip("-").isdigit() else msg.command[1]
        await client.send_message(t,f"<b>Whisper:</b>\n<i>{' '.join(msg.command[2:])}</i>");await msg.edit("<b>Sent!</b>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["groupdata","gpdata"],prefix)&filters.me)
async def gpdata(client,msg):
    if msg.chat.type=="private":return await msg.edit("<b>Private chat!</b>")
    c=msg.chat
    try:cnt=await client.get_chat_members_count(c.id)
    except:cnt="?"
    await msg.edit(f"<b>{c.title}</b>\n<b>ID:</b> <code>{c.id}</code>\n<b>Members:</b> {cnt}")

@Client.on_message(filters.command(["members"],prefix)&filters.me)
async def members(client,msg):
    if msg.chat.type=="private":return await msg.edit("<b>Private!</b>")
    try:cnt=await client.get_chat_members_count(msg.chat.id);await msg.edit(f"<b>Members:</b> {cnt}")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["q","quote"],prefix)&filters.me)
@with_reply
async def quote(client,msg):
    await msg.edit("<b>Generating...</b>")
    try:
        q=msg.reply_to_message
        u=q.from_user or q.sender_chat
        name=u.first_name if hasattr(u,'first_name') else u.title
        txt=q.text or q.caption or "Media"
        from utils.config import quotes_api
        async with aiohttp.ClientSession() as s:
            async with s.post(quotes_api,json={"messages":[{"text":txt,"author":{"id":u.id,"name":name,"rank":"","avatar":"","via_bot":""},"reply":{},"media":"","entities":[]}],"quote_color":"#162330","text_color":"#fff"}) as r:c=await r.read()
        img=resize_image(BytesIO(c),img_type="WEBP")
        await client.send_sticker(msg.chat.id,img);await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["webss","ss"],prefix)&filters.me)
async def webss(client,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}webss [url]")
    url=msg.command[1]
    if not url.startswith("http"):url="https://"+url
    await msg.edit("<b>Taking screenshot...</b>")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://image.thum.io/get/{url}") as r:img=BytesIO(await r.read());img.name="ss.jpg"
        await client.send_photo(msg.chat.id,img,caption=f"<b>{url}</b>");await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["carbon"],prefix)&filters.me)
async def carbon(client,msg):
    code=msg.reply_to_message.text if msg.reply_to_message else " ".join(msg.command[1:])
    if not code:return await msg.edit(f"{prefix}carbon [code/reply]")
    await msg.edit("<b>Generating...</b>")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.post("https://carbonara.solopov.dev/api/cook",json={"code":code,"backgroundColor":"#1F1F1F"}) as r:img=BytesIO(await r.read());img.name="carbon.png"
        await client.send_photo(msg.chat.id,img,caption="<b>Jeffery Epstein x Kurup</b>");await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["shorten","short"],prefix)&filters.me)
async def shorten(_,msg):
    url=msg.command[1] if len(msg.command)>1 else (msg.reply_to_message.text if msg.reply_to_message else None)
    if not url:return await msg.edit(f"{prefix}shorten [url]")
    await msg.edit("<b>Shortening...</b>")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://tinyurl.com/api-create.php?url={url}") as r:short=await r.text()
        await msg.edit(f"<b>{short}</b>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["edit","e"],prefix)&filters.me)
async def edit(_,msg):
    if not msg.reply_to_message or not msg.reply_to_message.outgoing:return await msg.edit("<b>Reply to YOUR msg!</b>")
    if len(msg.command)<2:return await msg.edit(f"{prefix}edit [text]")
    try:await msg.reply_to_message.edit(" ".join(msg.command[1:]));await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

modules_help["extra"]={"reply [text] [reply]*":"Quick reply","copy [reply]*":"Copy","fwd [chat] [reply]*":"Forward","whisper [user] [text]*":"Whisper","groupdata":"Group info","members":"Count","q [reply]*":"Quote","webss [url]*":"Screenshot","carbon [code]*":"Carbon","shorten [url]*":"Shorten","edit [text] [reply]*":"Edit"}
