# -*- coding: utf-8 -*-

__updated__ = "2024-07-21 13:41:39"

# ~~~~~~~~~~~~~~~~~~~~~~~ RoseTagger ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os  # noqa: F401
import asyncio
import datetime
import logging
import random
import shutil
import string
import time
import traceback
from typing import Tuple
from typing import Union
from random import shuffle
import aiofiles

from typing import List, Tuple, Union
import requests
from pymongo import MongoClient
from pyrogram import Client, __version__, filters
from pyrogram.enums import *
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
    UserNotParticipant,
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    User,
    CallbackQuery,
    ChatMember,
    ChatMemberUpdated,
)

from datetime import datetime as dt
from datetime import timedelta, tzinfo, datetime
from AlexaMusic import *
import datetime



rose_tagger = {}

users = []

reloadStatus = []

def is_user_blocked(user_id):
    return blocked_collection.find_one({"user_id": user_id}) is not None


def block_user(user_id):
    blocked_collection.update_one({"user_id": user_id}, {"$set": {"blocked": True}}, upsert=True)


def unblock_user(user_id):
    blocked_collection.delete_one({"user_id": user_id})


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ayaz ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Başlanğıc Mesajı

@app.on_message(filters.command("myt") & filters.private)
async def start(bot: Client, message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.mention
    user_id = message.from_user.id

    
    users_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "user_id": user_id,
                "first_name": first_name,
                "username": message.from_user.username
            }
        },
        upsert=True
    )

    await bot.send_message(LOG_CHANNEL, f"""
#ÖZELDEN START VERDİ#

🤖 **Kullanıcı:** {first_name}
📛 **Kullanıcı Adı:** @{message.from_user.username}
🆔 **Kullanıcı ID:** `{message.from_user.id}`
""")
    msg = await message.reply_text("**Bir saniye, Komut Panelini Getiriyorum...✅**")
    await asyncio.sleep(2)
    await msg.delete()
    await bot.send_message(
        chat_id,
        start_message.format(message.from_user.mention, BOT_USERNAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Komutlar", callback_data="cvv"),
                ],
                [
                    InlineKeyboardButton("🗯 Destek", url=f"https://t.me/DelularSohbet"),
                    InlineKeyboardButton("➕ Beni Grubuna Ekle", url=f"https://t.me/{app.me.username}?startgroup=a"),
                ],
                [
                    InlineKeyboardButton("❤️‍🔥 Geliştirici", user_id=OWNER_ID),
                ]
            ]
        ),
        disable_web_page_preview=True,
    )   



@app.on_callback_query(filters.regex("cvv"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        "✨ **Hadi komutlarımı görelim! Merak ettiğin butona tıkla ve komutları öğren.**👇",
        reply_markup=InlineKeyboardMarkup(
            [
                [    
                    InlineKeyboardButton(
                        "🏷️ Tag Komutları", callback_data="tagger"),
                    InlineKeyboardButton(
                       "🎮 Eğlence Komutları", callback_data="eglence")
                ],
                [
                    InlineKeyboardButton(
                        "⚙️ Extra Komutlar", callback_data="extra"),

                       
                    InlineKeyboardButton(
                        "❤️‍🔥 Geliştirici Komutları", callback_data="sahip"),
                        
                ],
                [
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                        
                ]
            ]
        )
    )
    


@app.on_callback_query(filters.regex("tagger"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        tagger_commands,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cvv"),
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                        
                ],
            ],
        ),
    )




@app.on_callback_query(filters.regex("eglence"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        eglence,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cvv"),
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                        
                ],
            ],
        ),
    )
   


@app.on_callback_query(filters.regex("extra"))
async def handler(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        extra,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Geri", callback_data="cvv"),
                    InlineKeyboardButton(
                        "🏠 Ana Menü", callback_data="start"
                    )
                ],
            ],
        ),
    )
    

@app.on_callback_query(filters.regex("sahip"))
async def handler(client: Client, query: CallbackQuery):
    if query.from_user.id != OWNER_ID:
        await query.answer("Sen Sahibim degilsin!!", show_alert=True)
        return
    else:
        await query.edit_message_text(
            adminkom,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔙 Geri", callback_data="cvv"
                            ),
                        InlineKeyboardButton(
                            "🏠 Ana Menü", callback_data="start"
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )


# Başlanğıc Button
@app.on_callback_query(filters.regex("meyit"))
async def _start(bot: Client, query: CallbackQuery):
    await query.edit_message_text(
        start_message.format(query.from_user.mention, BOT_USERNAME),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Komutlar", callback_data="cvv"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🗯 Kanal", url=f"https://t.me/MytDuyuru"
                    ),

                    InlineKeyboardButton(
                        "➕ Beni Grubuna Ekle" , url=f"https://t.me/{app.me.username}?startgroup=a"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "❤️‍🔥 Geliştirici", user_id=OWNER_ID
                    ),
                ]
            ],
        ),
    )   



#--------------------------------------------------------------------------

chatMode = []

chat_mode_users = {}

@app.on_message(filters.command("chatmode") & filters.group)
async def chat_mode_controller(bot: Client, msg: Message):
    if is_user_blocked(msg.from_user.id):
        await msg.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return

    admins = []
    async for member in bot.get_chat_members(msg.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if msg.from_user.id not in admins:
        await msg.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return
        
    chat_id = msg.chat.id
    chat = msg.chat
    commands = msg.command
    chat_mode_users[chat_id] = msg.from_user.id  # Komutu gönderen kullanıcıyı kaydet

    await bot.send_message(LOG_CHANNEL, f"""
#CHATMODE KULLANILDI
👤 Kullanan : [{msg.from_user.first_name}](tg://user?id={msg.from_user.id})
💥 Kullanıcı Id : {msg.from_user.id}
🪐 Kullanılan Grup : {chat.title}
💡 Grup ID : {chat.id}
◀️ Grup Link : @{chat.username}
""")
    
    if len(commands) == 1:
        status = "✅ Açık" if chat_id in chatMode else "❌ Kapalı"
        return await msg.reply(
            f"Durum : {status}\n\nSohbet modu kullanıcıların mesajlarına cevap verir.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Aç", callback_data="on"),
                        InlineKeyboardButton("Kapat", callback_data="off"),
                    ]
                ]
            ),
        )

@app.on_callback_query(filters.regex("^(on|off)$"))
async def chat_mode_callback(bot: Client, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    user_id = cb.from_user.id
    cmd = cb.data

    if chat_id not in chat_mode_users or chat_mode_users[chat_id] != user_id:
        await cb.answer("Bu işlemi yapma yetkiniz yok.", show_alert=True)
        return

    if cmd == "on":
        if chat_id in chatMode:
            await cb.edit_message_text("Sohbet modu zaten açık.")
        else:
            chatMode.append(chat_id)
            await cb.edit_message_text("Sohbet modu açıldı.")
    elif cmd == "off":
        if chat_id not in chatMode:
            await cb.edit_message_text("Sohbet modu zaten kapalı.")
        else:
            chatMode.remove(chat_id)
            await cb.edit_message_text("Sohbet modu kapatıldı.")

    await cb.answer()  



@app.on_message(filters.group & filters.text & ~filters.command("chatmode"), group=10)
async def chatModeHandler(bot: Client, msg: Message):
    def lower(text):
        return str(text.translate({ord("I"): ord("ı"), ord("İ"): ord("i")})).lower()

    def kontrol(query: Union[str, list], text: str) -> bool:
        if isinstance(query, str):
            return query in text.split()
        elif isinstance(query, list):
            for q in query:
                if q in text.split():
                    return True
            return False
        else:
            return False

    if msg.chat.id not in chatMode or msg.from_user.is_self:
        return

    text = lower(msg.text)  # * Mesajı küçük harfe çeviriyoruz

    reply = None

    if text.startswith("Aynur"): # * Mesaj buse ile başlıyorsa cevap veriyoruz
        reply = random.choice(Aynur)
        await asyncio.sleep(0.06)
    
    elif kontrol(["selam", "slm", "sa", "selamlar", "selamm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(slm)
        await asyncio.sleep(0.06)   
        #Bot chatmode komutları
    elif kontrol(["sahip"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sahip)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["naber"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(naber)
        await asyncio.sleep(0.06)  
         
    elif kontrol(["pelin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(pelin)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["nasılsın"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nasılsın)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["tm","tamam","tmm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tm)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["sus","suuss","suss"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sus)
        await asyncio.sleep(0.06)  
    
    elif kontrol(["merhaba","mrb","meraba"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(merhaba)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["yok"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yok)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["dur"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(dur)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["bot", "botu"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bot)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["napıyorsun"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(napıyorsun)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["takılıyorum","takılıyom"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(takılıyorum)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["he"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(he)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["hayır"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayır)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["tm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tm)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["nerdesin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nerdesin)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["özledim"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(özledim)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["bekle"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bekle)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["tünaydın"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tünaydın)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["günaydın"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(günaydın)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["sohbetler"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sohbetler)
        await asyncio.sleep(0.06)        
               
    elif kontrol(["konuşalım","konusalım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(konuşalım)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["saat"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(saat)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["geceler"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(geceler)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["şaka"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(şaka)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["kimsin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(kimsin)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["günler"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(günler)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["tanımıyorum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(tanımıyorum)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["konuşma"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(konuşma)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["teşekkürler","tesekkürler","tşkr"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(teşekkürler)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["eyvallah","eywl"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(eyvallah)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["sağol"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sağol)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["amk","aq","mg","mk"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(amk)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["yoruldum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yoruldum)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["yaş"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yaş)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["eşşek","eşek"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(eşek)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["canım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(canım)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["aşkım","askım","ask"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aşkım)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["uyu"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(uyu)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["nereye","nere"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nereye)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["naber"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(naber)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["küstüm","küsüm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(küstüm)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["peki"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(peki)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["ne","nee","neee","ney"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ne)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["takım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(takım)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["benimle","bnmle"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(benimle)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["seviyormusun","seviyomusun"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(seviyormusun)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["nediyon"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nediyon)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["özür"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(özür)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["niye"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(niye)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["bilmiyorum","bilmiyom","bilmiyos"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bilmiyorum)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["küsme"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(küsme)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["meyit"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(meyit)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["nerelisin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nerelisin)
        await asyncio.sleep(0.06)  
    
    elif kontrol(["sevgilin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sevgilin)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["olur"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(olur)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["olmas","olmaz"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(olmaz)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["nasıl"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nasıl)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["hayatım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayatım)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["cus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(cus)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["vallaha","valla","vallahi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(vallaha)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["yo"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yo)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["hayırdır"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayırdır)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["of"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(of)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["aynen"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aynen)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["ağla"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ağla)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["ağlama"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ağlama)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["sex","seks"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sex)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["evet"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(evet)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["hmm","hm","hımm","hmmm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hmm)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["hıhım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hıhım)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["git"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(git)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["komedi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(komedi)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["knka","kanka"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(knka)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["ban"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ban)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["sen"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sen)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["hiç"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hiç)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["aç","ac","açç"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aç)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["barışalım","batısalım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(barışalım)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["şimdi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(şimdi)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["varoş"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(varoş)
        await asyncio.sleep(0.06)        
                 
    elif kontrol(["arkadaş","arkadas"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(arkadaş)
        await asyncio.sleep(0.06)         
         
    elif kontrol(["sus","suss","suus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sus)
        await asyncio.sleep(0.06)          
         
    elif kontrol(["üzüldüm","üşüldüm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(üzüldüm)
        await asyncio.sleep(0.06)  
        
    elif kontrol(["kötü"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(kötü)
        await asyncio.sleep(0.06)   
    
    elif kontrol(["akşamlar"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(akşamlar)
        await asyncio.sleep(0.06)   
        
    try:
        await msg.reply(reply)
    except Exception as e:
        print(e)

    msg.continue_propagation()  #! BURAYA DOKUNMA


#-------------------------------------------------------------------


@app.on_message(filters.command(["slap", "sille"]) & filters.group)
async def slap(bot: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    chat = message.chat
    if not message.reply_to_message:
        await message.reply_text("🚫 **Bir kullanıcıya cevap verin!**")
        return
    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(f"{random.choice(dontslapown)}")
        return
    if message.reply_to_message.from_user.id == BOT_ID:
        await message.reply_text(f"{random.choice(dontslapme)}")
        return
    

    atan = message.from_user
    yiyen = message.reply_to_message.from_user

    atan_mesaj = f"[{atan.first_name}](tg://user?id={atan.id})"
    yiyen_mesaj = f"[{yiyen.first_name}](tg://user?id={yiyen.id})"

    goktug = random.choice(slapmessage)
    await message.reply_text(
        goktug.format(atan_mesaj, yiyen_mesaj),
    )

    await bot.send_message(
        LOG_CHANNEL,
        f"""
👤 Kullanan : [{atan.first_name}](tg://user?id={atan.id})
💥 Kullanıcı Id : {atan.id}
🪐 Kullanılan Grup : {chat.title}
💡 Grup ID : {chat.id}
◀️ Grup Link : @{chat.username}
📚 Kullanılan Modül : {message.text}
"""
    )

#-----------------------------------------------------------------------------#

@app.on_message(filters.command(["oner"]) & filters.group)
async def oner(bot: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("Üzgünüm, bu komutu kullanma yetkiniz engellendi. 🚫")
        return
        
    chat = message.chat
    if not message.reply_to_message:
        await message.reply_text("🚫 Bir kullanıcıya cevap verin!")
        return
    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(f"{random.choice(sarki1)}")
        return
    if message.reply_to_message.from_user.id == BOT_ID:
        await message.reply_text(f"{random.choice(sarki2)}")
        return
    

    atan = message.from_user
    yiyen = message.reply_to_message.from_user

    atan_mesaj = f"[{atan.first_name}](tg://user?id={atan.id})"
    yiyen_mesaj = f"[{yiyen.first_name}](tg://user?id={yiyen.id})"

    goktug = random.choice(sarkilar)
    await message.reply_text(
        goktug.format(atan_mesaj, yiyen_mesaj),
    )

    await bot.send_message(
        LOG_CHANNEL,
        f"""
👤 Kullanan : [{atan.first_name}](tg://user?id={atan.id})
💥 Kullanıcı Id : {atan.id}
🪐 Kullanılan Grup : {chat.title}
💡 Grup ID : {chat.id}
◀️ Grup Link : @{chat.username}
📚 Kullanılan Modül : Şarkı Öneri
"""
    )

#-----------------------------------------------------------------------------


@app.on_message(filters.command("tag") & filters.group)
async def tag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command

    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Tekli Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    
    num = 1
    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
**Üye etiketleme işlemi başlıyor.**

**Silinen hesapları ve botları atlayacak**

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"• [{user.first_name}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f" **{msg_content}**\n\n{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
**Üye etiketleme işlemi tamamlandı** ✅

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")

#--------------------------------------------------------------------------------------

@app.on_message(filters.command("utag") & filters.group)
async def utag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command

    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Çoklu Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    
    num = 5
    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
**Üye etiketleme işlemi başlıyor.**

**Silinen hesapları ve botları atlayacak**

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 5
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"• [{user.first_name}](tg://user?id={user.id})\n"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f" **{msg_content}**\n\n{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
**Üye etiketleme işlemi tamamlandı** ✅

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")

#---------------------------------------------------------------------------------------

@app.on_message(filters.command("stag") & filters.group)
async def stag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Söz Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 1

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"[{random.choice(soz)}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")
    
#-----------------------------------------------------------------------------------------    

@app.on_message(filters.command("igtag") & filters.group)
async def igtag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : iyigeceler Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 1

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"[{random.choice(iyigeceler)}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")


#------------------------------------------------------------------------------------------

@app.on_message(filters.command("anonimtag") & filters.group)
async def anonimtag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Anonim Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 1

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"[{random.choice(anonim)}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")

#-----------------------------------------------------------------------------------------


@app.on_message(filters.command("sorutag") & filters.group)
async def sorutag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Soru Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 1

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"[{random.choice(soru)}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")
 #-------------Unotag---------------------------------------------------------------------------


@app.on_message(filters.command("unotag") & filters.group)
async def unotag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Uno Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 1

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"[{random.choice(unotag)}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")

#-----------------------------------------------------------------------------------------#

@app.on_message(filters.command("gtag") & filters.group)
async def gtag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Günaydın Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 1

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 1
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"[{random.choice(gunaydin)}](tg://user?id={user.id})"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")
    
#-----------------------------------------------------------------------------------------


@app.on_message(filters.command("etag") & filters.group)
async def etag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Emoji Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 4

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 4
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"• [{random.choice(emoji)}](tg://user?id={user.id})\n"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f" **{msg_content}**\n\n{usrtxt} ")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")

#----------------------------------------------------------------------------------------------

@app.on_message(filters.command("ktag") & filters.group)
async def ktag(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    if message.chat.type == 'private':
        await message.reply("❗ Bu komutu sadece gruplarda kullanabilirsiniz!")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗ Eski mesajı göremiyorum!")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1
    user = message.from_user
    chat = message.chat
    
    await client.send_message(LOG_CHANNEL, f"""

Etiket işlemi bildirimi.

Kullanan : {user.mention} [`{user.id}`]
Etiket Tipi : Karakter Tag

Grup : {chat.title}
Grup İD : `{chat.id}`

Sebep : {message.text}
"""
 )
    num = 3

    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🏷️ __Üye etiketleme işlemi başlıyor.__

🎉 __Silinen hesapları ve botları atlayacak.__

👥 __Toplam Etiketlenecek Üye Sayısı: {total_members}__
⏳ __Tahmini Süre: {estimated_time // 60} dakika__
""")
    
    rose_tagger[message.chat.id] = start_msg.id
    nums = 3
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"• [{random.choice(karakter)}](tg://user?id={user.id})\n"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"**{msg_content}**\n\n{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
🏷️ __Üye etiketleme işlemi tamamlandı.__

👥 __Etiketlenen üye: {total_tagged}__
🤖 __Atlanılan Bot Sayısı: {skipped_bots}__
💣 __Atlanılan Silinen Hesap Sayısı: {skipped_deleted}__
""")

#--------------------------------------------------------------------------------------------------------------------


# .stop komutu
@app.on_message(filters.command("cancel") & filters.group)
async def stop(client, message):
    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ Bu komutu kullanmak için yönetici olmalısınız!")
        return
        
    if message.chat.id in rose_tagger:
        del rose_tagger[message.chat.id]
        await message.reply("⛔ __Etiketleme işlemi durduruldu!__")
    else:
        await message.reply("❗ __Etiketleme işlemi şu anda aktif değil.__")

#--------------------------------------------------------------------------------------------------
        
@app.on_message(filters.command(["help", "yardim", "yardım"]) & filters.group)
async def help(bot: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    await message.reply_text(
        "**📚 Komutlar Hakkında Bilgi Almak İçin alttaki butona tıklayın**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yardım ", url=f"https://t.me/{app.me.username}?cvv"
                    ),
                ],
            ],
        ),
    )
    
        

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Gruba giriş mesajı `~~


@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f"""**📖 Hey , {msg.from_user.mention}\nBeni Gruba Eklediğin İçin Teşekkürler .\n\n/chatmode on Sohbet Modunu Aktif Eder.**""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "⚙️ Daha Fazla Bilgi",
                                url=f"https://t.me/{app.me.username}?cvv",
                            )
                        ]
                    ]
                ),
            )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply("🇹🇷 ⚙️ ʙᴏᴛᴜɴ sᴀʜɪʙɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴋᴀᴛɪʟᴅɪ !")


# ^~~~~~~~~~~~~~~~~~'Eros'~~~~~~~~~~~~~~~~~~#

members = {}


@app.on_message(filters.command("eros", ["/", ""]) & filters.group)
async def _eros(client: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    chatID = message.chat.id
    statu = []
    if chatID in statu:
        return await message.reply("Aşıklar listesi güncelleniyor. Lütfen bekleyiniz..")

    async def scrapper(bot: Client, msg: Message):
        chat_id = msg.chat.id
        temp = {}
        try:
            statu.append(chat_id)
            async for member in bot.get_chat_members(chat_id, limit=200):
                member: ChatMember

                if member.user.is_bot:
                    continue
                if member.user.is_deleted:
                    continue

                temp[member.user.id] = member.user
                await asyncio.sleep(0.05)

            members[chat_id]["members"] = temp
            members[chat_id]["lastUpdate"] = dt.now()
            statu.remove(chat_id)
            return True
        except Exception as e:
            print(e)
            return False

    async def ship_(users: dict):
        list_ = list(users.keys())
        random.shuffle(list_)

        member1ID = random.choice(list_)
        member2ID = random.choice(list_)

        while member1ID == member2ID:
            member2ID = random.choice(list_)

        member1: User = users[member1ID]
        member2: User = users[member2ID]

        mention1 = member1.mention if not member1.username else f"@{member1.username}"
        mention2 = member2.mention if not member2.username else f"@{member2.username}"

        text = f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜ ᴀᴛɪʟᴅɪ.\n• ᴀsɪᴋʟᴀʀ  :\n\n{mention1} {random.choice(galp)} {mention2}**\n\n`ᴜʏᴜᴍʟᴜʟᴜᴋ ᴏʀᴀɴɪ: %{random.randint(0, 100)}`"
        return text

    if chatID not in members:
        members[chatID] = {}

    lastUpdate: dt = members[chatID].get("lastUpdate")
    if lastUpdate:
        now = dt.now()
        diff = now - lastUpdate
        if diff.seconds > 3600 * 4:
            msg = await message.reply(
                "Aşıklar listesi güncelleniyor, lütfen bekleyiniz..."
            )
            status = await scrapper(client, message)
            if status:
                await msg.delete()
                text = await ship_(members[chatID]["members"])
                return await message.reply(text)
            else:
                return await msg.edit(
                    "Bir hata oluştu, lütfen daha sonra tekrar deneyiniz."
                )
        else:
            text = await ship_(members[chatID]["members"])
            return await message.reply(text)

    else:
        msg = await message.reply("Aşıklar listesi güncelleniyor, lütfen bekleyiniz...")
        status = await scrapper(client, message)
        if status:
            await msg.delete()
            text = await ship_(members[chatID]["members"])
            return await message.reply(text)
        else:
            return await msg.edit(
                "Bir hata oluştu, lütfen daha sonra tekrar deneyiniz."
            )





# ••••••••••••••••••••••••••••"Meyit*••••••••••••••••••••••••••

# Kısa Filtreleme `~|


@app.on_message(filters.command(commandList))
async def games(c: Client, m: Message):
    if is_user_blocked(m.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    "🎲", "🎯", "🏀", "⚽", "🎳", "🎰"

    command = m.command[0]

    if command == "zar":
        return await c.send_dice(m.chat.id, emoji="🎲",
                                 reply_markup=InlineKeyboardMarkup(
                                        [
                                            [
                                                InlineKeyboardButton(
                                                    "Tekrar Oyna ♻️", callback_data="zar"
                                                ),
                                            ]
                                        ]
                                    )
                                )

    elif command == "dart":
        return await c.send_dice(m.chat.id, emoji="🎯",
                                    reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                    InlineKeyboardButton(
                                                        "Tekrar Oyna ♻️", callback_data="dart"
                                                    ),
                                                ]
                                            ]
                                        )
                                    )

    elif command == "basket":
        return await c.send_dice(m.chat.id, emoji="🏀",
                                    reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                    InlineKeyboardButton(
                                                        "Tekrar Oyna ♻️", callback_data="basket"
                                                    ),
                                                ]
                                            ]
                                        )
                                    )

    elif command == "futbol":
        return await c.send_dice(m.chat.id, emoji="⚽",
                                    reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                    InlineKeyboardButton(
                                                        "Tekrar Oyna ♻️", callback_data="futbol"
                                                    ),
                                                ]
                                            ]
                                        )
                                    )

    elif command == "bowling":
        return await c.send_dice(m.chat.id, emoji="🎳",
                                    reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                    InlineKeyboardButton(
                                                        "Tekrar Oyna ♻️", callback_data="bowling"
                                                    ),
                                                ]
                                            ]
                                        )
                                    )

    elif command == "slot":
        return await c.send_dice(m.chat.id, emoji="🎰",
                                    reply_markup=InlineKeyboardMarkup(
                                            [
                                                [
                                                    InlineKeyboardButton(
                                                        "Tekrar Oyna ♻️", callback_data="slot"
                                                    ),
                                                ]
                                            ]
                                        )
                                    )

    elif command == "para":
        return await m.reply(
            "**Yazı 🪙**" if random.randint(0, 1) == 0 else "**Tura 🪙**"
        )

    elif command == "mani":
        return await m.reply_text(random.choice(mani))

    elif command == "saka":
        return await m.reply_text(f"**{random.choice(espri)}**")

    elif command == "d":
        return await m.reply_text(
            f"**✅ Doğruluk mu ? 🔪 Cesaret mi ? \n\n{m.from_user.mention} Doğruluk sorusu seçti !\n\n{random.choice(D_LİST)}**"
        )

    elif command == "c":
        return await m.reply_text(
            f"**✅ Doğruluk mu ? 🔪 Cesaret mi ? \n\n{m.from_user.mention} Cesaret sorusu seçti !\n\n{random.choice(C_LİST)}**"
        )


    return
# * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.on_callback_query(filters.regex("zar"))
async def zar(client: Client, query: CallbackQuery):
    await client.send_dice(query.message.chat.id, emoji="🎲",
                           reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Tekrar Oyna ♻️", callback_data="zar"
                                        ),
                                    ]
                                ]
                            )
                        )

@app.on_callback_query(filters.regex("dart"))
async def dart(client: Client, query: CallbackQuery):
    await client.send_dice(query.message.chat.id, emoji="🎯",
                           reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Tekrar Oyna ♻️", callback_data="dart"
                                        ),
                                    ]
                                ]
                            )
                        )

@app.on_callback_query(filters.regex("basket"))
async def basket(client: Client, query: CallbackQuery):
    await client.send_dice(query.message.chat.id, emoji="🏀",
                           reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Tekrar Oyna ♻️", callback_data="basket"
                                        ),
                                    ]
                                ]
                            )
                        )

@app.on_callback_query(filters.regex("futbol"))
async def futbol(client: Client, query: CallbackQuery):
    await client.send_dice(query.message.chat.id, emoji="⚽",
                           reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Tekrar Oyna ♻️", callback_data="futbol"
                                        ),
                                    ]
                                ]
                            )
                        )

@app.on_callback_query(filters.regex("bowling"))
async def bowling(client: Client, query: CallbackQuery):
    await client.send_dice(query.message.chat.id, emoji="🎳",
                           reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Tekrar Oyna ♻️", callback_data="bowling"
                                        ),
                                    ]
                                ]
                            )
                        )

@app.on_callback_query(filters.regex("slot"))
async def slot(client: Client, query: CallbackQuery):
    await client.send_dice(query.message.chat.id, emoji="🎰",
                           reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            "Tekrar Oyna ♻️", callback_data="slot"
                                        ),
                                    ]
                                ]
                            )
                        )



#-----------------------------------------------------------------------------------#


@app.on_message(filters.command("pings"))
async def pingy(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    start = dt.now()
    hmm = await message.reply("`Pong!`")
    end = dt.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(f"Ping!: {round(ms)}ms", callback_data="ping")],
            ],
        ),
    )

@app.on_callback_query(filters.regex("ping"))
async def ping(bot, query):
    start = dt.now()
    chat_id = query.message.chat.id
    await bot.answer_callback_query(
        callback_query_id=query.id, text="Şimdi Kontrol Et ^^", show_alert=True
    )
    end = dt.now()
    ms = (end - start).microseconds / 1000
    await query.edit_message_text(
        f"""**
█▀█ █▀█ █▄░█ █▀▀ █ 
█▀▀ █▄█ █░▀█ █▄█ ▄**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"Ping!: {round(ms)}ms", callback_data="ping")]]
        ),
    )

#-----------------------------------------------------------------------------------#
@app.on_message(filters.command("ids"))
async def _id(bot: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    mesaj = message.reply_to_message or message
    text = f"""
**👤 Kullanıcı Adı:** {mesaj.from_user.mention if mesaj.from_user else None}
**🆔 Kullanıcı ID:** `{mesaj.from_user.id if mesaj.from_user else None}`
**📚 Kullanıcı Adı:** @{mesaj.from_user.username if mesaj.from_user else None}
"""
    await message.reply(text)

  
@app.on_message(filters.command("infon"))
async def info(client: Client, message: Message):
    mesaj = message.reply_to_message or message
    chat = message.chat
    text = f"""
**👤 Kullanıcı Adı:** {mesaj.from_user.mention if mesaj.from_user else None}
**🆔 Kullanıcı ID:** `{mesaj.from_user.id if mesaj.from_user else None}`
**📚 Kullanıcı Adı:** @{mesaj.from_user.username if mesaj.from_user else None}

**👥 Grup Adı:** `{chat.title if chat else None}`
**🆔 Grup ID:** `{chat.id if chat else None}`
"""
    await message.reply(text)
    
#-----------------------------------------------------------------------------------#

@app.on_message(filters.command(["burc", "burç"]) & filters.group)
async def burc(bot: Client, message: Message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    chat_id = message.chat.id
    command = message.command
    if len(command) == 1:
        await message.reply_text("Yanlış format kullanımı.  /burc 'burç ismi' şeklinde kullanın.")
        return
    
    elif len(command) == 2:
        if command[1] == "kova":
            await message.reply_text(f"**Kova ♒ Burcunuzun Yorumu** :\n\n**{random.choice(kova)}**")
            return
        elif command[1] == "balık":
            await message.reply_text(f"**Balık ♓ Burcunuzun Yorumu** :\n\n**{random.choice(balık)}**")
            return
        elif command[1] == "koç":
            await message.reply_text(f"**Koç ♈ Burcunuzun Yorumu** :\n\n**{random.choice(koc)}**")
            return
        elif command[1] == "boğa":
            await message.reply_text(f"**Boğa ♉ Burcunuzun Yorumu** :\n\n**{random.choice(boga)}**")
            return
        elif command[1] == "ikizler":
            await message.reply_text(f"**İkizler ♊ Burcunuzun Yorumu** :\n\n**{random.choice(ikizler)}**")
            return
        elif command[1] == "yengeç":
            await message.reply_text(f"**Yengeç ♋ Burcunuzun Yorumu** :\n\n**{random.choice(yengec)}**")
            return
        elif command[1] == "aslan":
            await message.reply_text(f"**Aslan ♌ Burcunuzun Yorumu** :\n\n**{random.choice(aslan)}**")
            return
        elif command[1] == "başak":
            await message.reply_text(f"**Başak ♍ Burcunuzun Yorumu** :\n\n**{random.choice(basak)}**")
            return
        elif command[1] == "terazi":
            await message.reply_text(f"**Terazi ♎ Burcunuzun Yorumu** :\n\n**{random.choice(terazi)}**")
            return
        elif command[1] == "akrep":
            await message.reply_text(f"**Akrep ♏ Burcunuzun Yorumu** :\n\n**{random.choice(akrep)}**")
            return
        elif command[1] == "yay":
            await message.reply_text(f"**Yay ♐ Burcunuzun Yorumu** :\n\n**{random.choice(yay)}**")
            return
        elif command[1] == "oğlak":
            await message.reply_text(f"**Oğlak ♑ Burcunuzun Yorumu** :\n\n**{random.choice(oglak)}**")
            return
        else:
            await message.reply_text("Lütfen geçerli bir burç girin.")
            return
    else:
        await message.reply_text("Lütfen geçerli bir burç girin.")
        return


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return

    text = ""

    
    if message.reply_to_message:
        text = message.reply_to_message.text

    
    else:
         
        text_parts = message.text.split(maxsplit=1)
        if len(text_parts) < 2:
            await message.reply("__🔊 Metin sese çevriliyor...__ Lütfen bekleyin.")
            return

        text = text_parts[1]

    
    res_message = await message.reply("__🔊 Metin sese çevriliyor...__ Lütfen bekleyin.")

    
    await asyncio.sleep(2)

    
    tts = gTTS(text=text, lang='tr')  
    tts.save("output.mp3") 

    
    await client.send_voice(message.chat.id, voice="output.mp3")

    # Geçici dosyayı silme
    os.remove("output.mp3")

    
    await message.delete()
    await res_message.delete()



#-----------------------------------------OWNER---------------------------------------------#

@app.on_message(filters.new_chat_members)
async def welcome(client: Client, message: Message):
    for member in message.new_chat_members:
        if member.is_self:
            
            groups_collection.update_one(
                {"chat_id": message.chat.id},
                {
                    "$set": {
                        "chat_id": message.chat.id,
                        "chat_name": message.chat.title
                    }
                },
                upsert=True
            )

            
            await bot(client.send_message(LOG_CHANNEL, f"""
#YENİ GRUBA KATILDIM#

🤖 **Grup Adı:** {message.chat.title}
◀️ Grup Link : @{chat.username}
🆔 **Grup ID:** `{message.chat.id}`
"""))






@app.on_message(filters.command("stat") & filters.user(OWNER_ID))
async def stat(client: Client, message: Message):
    user_count = users_collection.count_documents({})
    group_count = groups_collection.count_documents({})
    await message.reply(f"📊 **İstatistikler**\n\n👤 **Kullanıcı Sayısı:** `{user_count}`\n👥 **Grup Sayısı:** `{group_count}`")






@app.on_message(filters.command("duyuru") & filters.user(OWNER_ID))
async def duyuru(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply("Lütfen bir mesajı yanıtlayarak komutu kullanın.")
        return

    duyuru_mesaji = message.reply_to_message
    gruplar = groups_collection.find({})
    kullanicilar = users_collection.find({})
    
    basarili_grup = 0
    basarisiz_grup = 0
    basarili_kullanici = 0
    basarisiz_kullanici = 0

    
    for grup in gruplar:
        try:
            await client.forward_messages(grup["chat_id"], duyuru_mesaji.chat.id, duyuru_mesaji.id)
            basarili_grup += 1
        except Exception as e:
            basarisiz_grup += 1

    
    for kullanici in kullanicilar:
        try:
            await client.forward_messages(kullanici["user_id"], duyuru_mesaji.chat.id, duyuru_mesaji.id)
            basarili_kullanici += 1
        except Exception as e:
            basarisiz_kullanici += 1

    
    await message.reply(f"""**Duyuru başarıyla iletildi:** 📢
    
**Toplam Başarılı Grup:** `{basarili_grup}` - ✅
**Toplam Başarısız Grup:** `{basarisiz_grup}` - ❌
    
**Başarılı Kullanıcılar:** `{basarili_kullanici}` - ✅
**Başarısız Kullanıcılar:** `{basarisiz_kullanici}` - ❌
    """)






@app.on_message(filters.command("blockgrup") & filters.user(OWNER_ID))
async def block_group(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text("__Kullanım: /blockgrup <grup_id>__")
        return

    try:
        chat_id = int(message.command[1])
    except ValueError:
        await message.reply_text("__Geçerli bir grup ID'si girin.__")
        return

    # Grubu banla
    groups_collection.update_one({"group_id": chat_id}, {"$set": {"blocked": True}}, upsert=True)
    await message.reply_text(f"__Grup `{chat_id}` banlandı.__")
    
    try:
        await client.leave_chat(chat_id)
    except Exception as e:
        await message.reply_text(f"__Grubu terk ederken hata: {str(e)}__")





@app.on_message(filters.command("unblockgrup") & filters.user(OWNER_ID))
async def unblock_group(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text("__Kullanım: /unblockgrup <grup_id>__")
        return

    try:
        chat_id = int(message.command[1])
    except ValueError:
        await message.reply_text("__Geçerli bir grup ID'si girin.__")
        return

    # Grubun banını kaldır
    groups_collection.update_one({"group_id": chat_id}, {"$set": {"blocked": False}}, upsert=True)
    await message.reply_text(f"__Grup `{chat_id}` banı kaldırıldı.__")


@app.on_message(filters.new_chat_members)
async def welcome_new_group(client: Client, message: Message):
    chat_id = message.chat.id
    if groups_collection.find_one({"group_id": chat_id, "blocked": True}):
        await message.reply_text("Bu grup banlandı. Bot gruptan ayrılıyor.")
        await client.leave_chat(chat_id)
    else:
        await message.reply_text("__Merhaba! RoseTagger botunu grubunuza eklediğiniz için teşekkürler. Komutlar için /komutlar yazabilirsiniz.__ 💫")
        

@app.on_chat_member_updated()
async def monitor_group(client: Client, chat_member_updated: ChatMemberUpdated):
    if chat_member_updated.new_chat_member and chat_member_updated.new_chat_member.user.id == client.me.id:
        chat_id = chat_member_updated.chat.id
        if groups_collection.find_one({"group_id": chat_id, "blocked": True}):
            await client.send_message(chat_id, "__ℹ️ Bu grup banlandı. Eğer bunun bir hata olduğunu düşünüyorsanız t.me/blayzen 'e bildirin.__")
            await client.leave_chat(chat_id)
            

# Kullanıcıyı engelleme komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def block_user_cmd(client: Client, message: Message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            user_id = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply("__Geçersiz komut kullanımı. Örnek: /block [Kullanıcı İD] veya yanıtla.__")
        return

    block_user(user_id)
    await message.reply(f"**Kullanıcı `{user_id}` başarıyla engellendi. 🚫**")







# Kullanıcının engelini kaldırma komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unblock_user_cmd(client: Client, message: Message):
    try:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            user_id = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply("__Geçersiz komut kullanımı. Örnek: /unblock [Kullanıcı İD] veya yanıtla.__")
        return

    unblock_user(user_id)
    await message.reply(f"**Kullanıcı `{user_id}` başarıyla engeli kaldırıldı. ✅**")


#----------------------------------------------------------

app.run()
print(" Bot çalışıyor :)")
