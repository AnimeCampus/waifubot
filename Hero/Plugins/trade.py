import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.basicdb import checktrade, trade
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@pbot.on_message(filters.command("trade"))
async def trade_grp(client, message):
    user_id = message.from_user.id
    reply = message.reply_to_message

    if not reply:
        return await message.reply_text("reply to someone")

    try:
        heroes = message.split(None, 1)[1]
        hero1 = heroes.split(" ")[0]
        hero2 = heroes.split(" ")[1]
    except:
        return await message.reply_text(
            "Wrong format!!\n: /trade (hero id that you want to give) (hero id that you want to get)"
        )

    trade_partner_id = reply.from_user.id
    valid1, heroname1 = checktrade(hero1, user_id)
    if valid == False:
        return await message.reply_text("You dont have that hero to trade!!")
    valid2, heroname2 = checktrade(hero2, trade_partner_id)
    if valid2 == False:
        return await message.reply_text("Your trade partner dont have that hero to trade!!")

    await message.reply_text(
        f"Are you sure you want to trade:\n{heroname1} for {heroname2}",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Yes", callback_data=f"yess={hero1}={heroname1}={user_id}={hero2}={heroname2}={trade_partner_id}")],
                [InlineKeyboardButton(text="No", callback_data="noo")]
            ]
        )
    )



@pbot.on_callback_query(filters.regex(r"^yess"))
async def yess_callbacc(client, CallbackQuery):
    alldata = CallbackQuery.data.split("=")
    
    hero1 = alldata[1]
    heroname1 = alldata[2]
    user_id = alldata[3]
    hero1 = alldata[4]
    heroname1 = alldata[5]
    trade_partner_id = alldata[6]
    await CallbackQuery.message.edit_caption(
        "Trade done!!"
    )
    trade(hero1, heroname1, user_id, hero2, heroname2, trade_partner_id)


@Client.on_callback_query(filters.regex("noo"))
async def nooo_callbacc(client, CallbackQuery):
    await CallbackQuery.message.edit_caption(
        "Trade cancelled!!"
    )