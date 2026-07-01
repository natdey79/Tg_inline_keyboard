# app.py
import os
import logging
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Setup ---
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("No TELEGRAM_TOKEN found in environment variables")

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# --- Bot Functions ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message with the 4-button inline keyboard in 2+1+1 layout."""
    keyboard = [
        # Row 1: Two buttons side by side
        [
            InlineKeyboardButton("🎰 KuyaPlay Promotion", url="https://t.me/kuyaplay_CS"),
            InlineKeyboardButton("📊 Betting Tips", url="https://t.me/scorehuntertips"),
        ],
        # Row 2: Single button
        [
            InlineKeyboardButton("📰 Sport News", url="https://t.me/scorehuntersports"),
        ],
        # Row 3: Single button
        [
            InlineKeyboardButton("🎮 Live CS", url="https://t.me/AhBoy_CS"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = (
        "🎯 Welcome to our Telegram Channel Hub!\n\n"
        "Choose a channel below to join:"
    )
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message."""
    help_text = (
        "🤖 Available Commands:\n"
        "/start - Show channel buttons\n"
        "/help - Show this message\n\n"
        "📌 Click any button to join the channel!"
    )
    await update.message.reply_text(help_text)

# --- Create Bot Application ---
bot_app = Application.builder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("help", help_command))

# --- Flask Web Server for Render ---
@app.route("/")
def home():
    return "🤖 Bot is running!"

@app.route("/health")
def health():
    return "OK"

# --- Start Both Services ---
if __name__ == "__main__":
    logging.info("Starting bot...")
    # Start bot polling in the background
    bot_app.run_polling()
    
    # Start Flask server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)