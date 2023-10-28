# start.py

from pyrogram import Client, Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Command handler for /start
@app.on_message(Filters.command("start"))
def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Create a welcome message
    welcome_message = "Hi, I'm the Pokemon Catcher Bot! 🌟\n\n"
    
    # Create an InlineKeyboardMarkup with a button for adding the bot to a group
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Add me to your group", url="https://t.me/YOUR_BOT_USERNAME?startgroup=true")]])
    
    # Send the welcome message and inline button together
    client.send_message(chat_id, welcome_message, reply_markup=keyboard)
