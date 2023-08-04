
import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.uploaddb import upload_waifu, upload_anime, upload_husbando
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("addw"))
async def add_waifu_characater(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        url = splitted[0]
        name = splitted[1]
        waifu_id = splitted[2]
        anime_id = splitted[3]
    except:
        return await message.reply_text("format:\n`/addw (url) (name) (waifu id) (anime id)`")
    
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
    await message.reply_text(f"Done!!\nID: {waifu_id}\nName: {waifu_name}\nUrl: `{url}`\nAnime ID: {anime_id}")