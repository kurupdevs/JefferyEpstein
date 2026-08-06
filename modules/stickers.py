# Jeffery Epstein x Kurup - Stickers
import os
from io import BytesIO
from pyrogram import Client,filters
from utils import modules_help,prefix
from utils.scripts import format_exc,with_reply,resize_image

@Client.on_message(filters.command(["kang"],prefix)&filters.me)
@with_reply
async def kang(client,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}kang [pack] [emoji]")
    await msg.edit("<b>Kanging...</b>")
    try:
        path=await msg.reply_to_message.download()
        img=resize_image(path)
        if os.path.exists(path):os.remove(path)
        await client.send_document("me",img,caption=f"<b>Pack: {msg.command[1]}</b>")
        await msg.edit("<b>Sticker saved! Add manually via @Stickers</b>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["stp","sticker2png"],prefix)&filters.me)
@with_reply
async def stp(client,msg):
    try:
        await msg.edit("<b>Converting...</b>")
        path=await msg.reply_to_message.download()
        with open(path,"rb") as f:content=f.read()
        if os.path.exists(path):os.remove(path)
        img=BytesIO(content);img.name="sticker.png"
        await client.send_document(msg.chat.id,img,caption="<b>Jeffery Epstein x Kurup</b>")
        await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["resize"],prefix)&filters.me)
@with_reply
async def resize_cmd(client,msg):
    try:
        await msg.edit("<b>Resizing...</b>")
        path=await msg.reply_to_message.download()
        img=resize_image(path);img.name="resized.png"
        if os.path.exists(path):os.remove(path)
        await client.send_document(msg.chat.id,img,caption="<b>Jeffery Epstein x Kurup</b>")
        await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

modules_help["stickers"]={"kang [reply]* [pack]*":"Steal sticker","stp [reply]*":"Sticker to PNG","resize [reply]*":"Resize"}
