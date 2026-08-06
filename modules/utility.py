# Jeffery Epstein x Kurup - Utility
import asyncio,string,random
from io import StringIO
from contextlib import redirect_stdout
import aiohttp
from pyrogram import Client,filters
from utils import modules_help,prefix
from utils.scripts import format_exc

@Client.on_message(filters.command(["sh","shell"],prefix)&filters.me)
async def sh(_,msg):
    if len(msg.command)<2:return await msg.edit("<b>Specify command!</b>")
    c=msg.text.split(maxsplit=1)[1]
    await msg.edit(f"<b>$</b> <code>{c[:300]}</code>\n<b>Running...</b>")
    try:
        p=await asyncio.create_subprocess_shell(c,stdout=-1,stderr=-1)
        o,e=await asyncio.wait_for(p.communicate(),timeout=60)
        r=""
        if o:r+=f"<b>Out:</b>\n<code>{o.decode()[:2000]}</code>\n"
        if e:r+=f"<b>Err:</b>\n<code>{e.decode()[:500]}</code>\n"
        r+=f"<b>Exit:</b> <code>{p.returncode}</code>"
        await msg.edit(f"<b>$</b> <code>{c[:300]}</code>\n{r[:3900]}")
    except asyncio.TimeoutError:await msg.edit("<b>Timeout!</b>")
    except Exception as ex:await msg.edit(format_exc(ex))

@Client.on_message(filters.command(["eval"],prefix)&filters.me)
async def evl(_,msg):
    if len(msg.command)<2:return await msg.edit("<b>No code!</b>")
    try:r=eval(msg.text.split(maxsplit=1)[1]);await msg.edit(f"<b>Result:</b>\n<code>{str(r)[:3000]}</code>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["exec","ex"],prefix)&filters.me)
async def exc(_,msg):
    if len(msg.command)<2:return await msg.edit("<b>No code!</b>")
    code=msg.text.split(maxsplit=1)[1];o=StringIO()
    try:
        with redirect_stdout(o):exec(code)
        await msg.edit(f"<b>Output:</b>\n<code>{o.getvalue()[:3000]}</code>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["whois","info","id"],prefix)&filters.me)
async def whois(client,msg):
    if msg.reply_to_message:u=msg.reply_to_message.from_user or msg.reply_to_message.sender_chat
    elif len(msg.command)>1:
        try:u=await client.get_users(msg.command[1])
        except:
            try:u=await client.get_chat(msg.command[1])
            except:return await msg.edit("<b>Not found!</b>")
    else:u=msg.from_user
    if hasattr(u,'first_name'):t=f"<b>User:</b> {u.first_name} {u.last_name or ''}\n<b>ID:</b> <code>{u.id}</code>\n<b>@:</b> @{u.username or 'N/A'}"
    else:t=f"<b>Chat:</b> {u.title}\n<b>ID:</b> <code>{u.id}</code>"
    await msg.edit(t)

@Client.on_message(filters.command(["tr","translate"],prefix)&filters.me)
async def tr(_,msg):
    if len(msg.command)<3 and not msg.reply_to_message:return await msg.edit(f"{prefix}tr [lang] [text]")
    lang=msg.command[1];txt=msg.reply_to_message.text if msg.reply_to_message else " ".join(msg.command[2:])
    if not txt:return await msg.edit("<b>No text!</b>")
    await msg.edit("<b>Translating...</b>")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={lang}&dt=t&q={txt}") as r:d=await r.json()
        result="".join(i[0] for i in d[0] if i[0])
        await msg.edit(f"<b>Result:</b>\n<code>{result[:3000]}</code>")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["weather"],prefix)&filters.me)
async def weather(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}weather [city]")
    city=" ".join(msg.command[1:]);await msg.edit("<b>Fetching...</b>")
    try:
        from utils.config import weather_api_key
        async with aiohttp.ClientSession() as s:
            async with s.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric") as r:d=await r.json()
        if d.get("cod")!=200:return await msg.edit("<b>City not found!</b>")
        await msg.edit(f"<b>{d['name']}:</b> {d['main']['temp']}C, {d['weather'][0]['description']}")
    except:await msg.edit("<b>No API key!</b>")

@Client.on_message(filters.command(["currency"],prefix)&filters.me)
async def curr(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}currency [code]")
    await msg.edit("<b>Fetching...</b>")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://api.exchangerate-api.com/v4/latest/{msg.command[1].upper()}") as r:d=await r.json()
        rates={k:v for k,v in d.get("rates",{}).items() if k in["USD","EUR","GBP","INR","JPY","PKR","BDT"] and k!=msg.command[1].upper()}
        txt=f"<b>{msg.command[1].upper()}:</b>\n"+"\n".join(f"{k}: {v}" for k,v in rates.items())
        await msg.edit(txt)
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["qr"],prefix)&filters.me)
async def qr(client,msg):
    txt=" ".join(msg.command[1:]) if len(msg.command)>1 else (msg.reply_to_message.text if msg.reply_to_message else None)
    if not txt:return await msg.edit(f"{prefix}qr [text]")
    try:await client.send_photo(msg.chat.id,f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={txt}",caption="<b>QR</b>");await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["password","passgen"],prefix)&filters.me)
async def pwd(_,msg):
    l=int(msg.command[1]) if len(msg.command)>1 and msg.command[1].isdigit() else 16
    p="".join(random.choice(string.ascii_letters+string.digits+"!@#$%&") for _ in range(l))
    await msg.edit(f"<b>Password:</b>\n<code>{p}</code>")

@Client.on_message(filters.command(["ip"],prefix)&filters.me)
async def ip(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}ip [addr]")
    await msg.edit("<b>Looking up...</b>")
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(f"http://ip-api.com/json/{msg.command[1]}") as r:d=await r.json()
        await msg.edit(f"<b>IP:</b> {d['query']}\n<b>Country:</b> {d['country']}\n<b>City:</b> {d['city']}\n<b>ISP:</b> {d['isp']}")
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["google","g"],prefix)&filters.me)
async def google(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}google [query]")
    await msg.edit(f"<b>Search:</b> https://www.google.com/search?q={'+'.join(msg.command[1:])}")

@Client.on_message(filters.command(["speedtest","speed"],prefix)&filters.me)
async def speedtest(_,msg):
    await msg.edit("<b>Running speedtest...</b>")
    try:
        import speedtest as st
        s=st.Speedtest();s.get_best_server()
        d=s.download()/1_000_000;u=s.upload()/1_000_000;p=s.results.ping
        await msg.edit(f"<b>Speed:</b> {d:.1f}Mbps / {u:.1f}Mbps / {p:.0f}ms")
    except ImportError:await msg.edit("<b>speedtest-cli not installed!</b>")
    except Exception as e:await msg.edit(format_exc(e))

modules_help["utility"]={"sh [cmd]*":"Shell","eval [code]*":"Python eval","exec [code]*":"Python exec","whois [user]":"User info","id":"IDs","tr [lang] [text]":"Translate","weather [city]*":"Weather","currency [code]*":"Rates","qr [text]*":"QR","password [len]":"Passgen","ip [addr]*":"IP lookup","google [query]*":"Search","speedtest":"Speed test"}
