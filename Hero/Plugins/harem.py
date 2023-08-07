import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.basicdb import info
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(filters.command("team"))
async def harem_grp(client, message):
    user_id = message.from_user.id
    data = info(user_id)
    if data == False:
        await message.reply_text("You havent yet collected any Character!!")
        return
    
    if len(data) == 0:
        await message.reply_text("You havent yet collected any Character!!")
        return
    
    text = f"Hello {message.from_user.first_name},\n\nYour Character's team:\n"
    count = 0
    for hero in data:
        count = count + 1
        hero_id = hero[0]
        hero_name = hero[1]
        text += f"**{count}.** `{hero_id}`\n-> {hero_name}\n"
    
    await message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="add fav", callback_data="add_fav")]
            ]
        )
    )
