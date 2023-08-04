
import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.uploaddb import upload_waifu, upload_anime, upload_husbando
from Hero.database import cwdb, chdb, adb, get_list

import requests
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("addw"))
async def add_waifu_characater(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        url = splitted[0]
        name = splitted[1]
        waifu_id = splitted[2]
        anime_id = text.split(None, 1)[1].split(None, 1)[1].split(None, 1)[1]
    except:
        return await message.reply_text("format:\n`/addw (waifu id) (anime id) (url) (name)`")
    
    upload_waifu(url, waifu_id, name, anime_id)
    await message.reply_text(f"Done!!\nID: {waifu_id}\nName: {waifu_name}\nUrl: `{url}`\nAnime ID: {anime_id}")


@Client.on_message(filters.command("addh"))
async def add_husbando_characater(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        url = splitted[0]
        name = splitted[1]
        waifu_id = splitted[2]
        anime_id = splitted[3]
    except:
        return await message.reply_text("format:\n`/addh (url) (name) (waifu id) (anime id)`")
    
    upload_husbando(url, waifu_id, name, anime_id)
    await message.reply_text(f"Done!!\nID: {waifu_id}\nName: {waifu_name}\nUrl: `{url}`\nAnime ID: {anime_id}")


@Client.on_message(filters.command("addanime"))
async def add_anime_characater(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        anime_id = splitted[0]
        name = splitted[1]
    except:
        return await message.reply_text("format:\n`/addanime (anime id) (name)`")
    
    upload_anime(anime_id, name)
    await message.reply_text(f"Done!!\nID: {anime_id}\nName: {name}")



@Client.on_message(filters.command("animelist"))
async def animelist(client, message):

    listt = get_list(adb)
    
    if not listt:
        await message.reply_text(
            "ɴᴏʙᴏᴅʏ ɪs ʀᴇɢɪsᴛᴇʀᴇᴅ ɪɴ ʏᴏᴜʀ ʙᴏᴛ\n(⁠⌐⁠■⁠-⁠■⁠)"
        )
        return

    ffile = "Anime\n"
    ffile = "[x] - ɪᴅ - ɴᴀᴍᴇ\n"
    x = 0
    for obj in listt:
        x = x + 1
        ffile += f"[{x}] {obj['_id']} - {obj['name']}\n"

    with BytesIO(str.encode(ffile)) as output:
        output.name = "animelist.txt"
        await message.reply_document(
            document=output,
            file_name="animelist.txt",
            caption="ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪsᴛ",
        )


@Client.on_message(filters.command("waifulist"))
async def waifulist(client, message):

    listt = get_list(cwdb)
    
    if not listt:
        await message.reply_text(
            "ɴᴏʙᴏᴅʏ ɪs ʀᴇɢɪsᴛᴇʀᴇᴅ ɪɴ ʏᴏᴜʀ ʙᴏᴛ\n(⁠⌐⁠■⁠-⁠■⁠)"
        )
        return

    ffile = "Waifu\n"
    ffile = "[x] - ɪᴅ - ɴᴀᴍᴇ - anime id - waifu url\n"
    x = 0
    for obj in listt:
        x = x + 1
        ffile += f"[{x}] {obj['_id']} - {obj['name']} - {obj['anime_id']} - {obj['img']}\n"

    with BytesIO(str.encode(ffile)) as output:
        output.name = "waifulist.txt"
        await message.reply_document(
            document=output,
            file_name="waifulist.txt",
            caption="ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪsᴛ",
        )


@Client.on_message(filters.command("husbandolist"))
async def husbandolist(client, message):

    listt = get_list(chdb)
    
    if not listt:
        await message.reply_text(
            "ɴᴏʙᴏᴅʏ ɪs ʀᴇɢɪsᴛᴇʀᴇᴅ ɪɴ ʏᴏᴜʀ ʙᴏᴛ\n(⁠⌐⁠■⁠-⁠■⁠)"
        )
        return

    ffile = "Husbando\n"
    ffile = "[x] - ɪᴅ - ɴᴀᴍᴇ - anime id - husbando url\n"
    x = 0
    for obj in listt:
        x = x + 1
        ffile += f"[{x}] {obj['_id']} - {obj['name']} - {obj['anime_id']} - {obj['img']}\n"

    with BytesIO(str.encode(ffile)) as output:
        output.name = "husbandolist.txt"
        await message.reply_document(
            document=output,
            file_name="husbandolist.txt",
            caption="ʜᴇʀᴇ ɪs ᴛʜᴇ ʟɪsᴛ",
        )

