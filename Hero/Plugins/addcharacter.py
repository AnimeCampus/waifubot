
import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.uploaddb import upload_waifu
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("addwaifu"))
async def add_waifu_characater(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        url = splitted[0]
        name = splitted[1]
        waifu_id = splitted[2]
        anime_id = splitted[3]
    except:
        return await message.reply_text()