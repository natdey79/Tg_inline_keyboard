# Telegram Channel Hub Bot

A Telegram bot that provides quick access to multiple channels via an inline keyboard.

## Features

- 4-channel inline keyboard with 2+1+1 layout
- URL buttons that open Telegram channels directly
- Clean, user-friendly interface

## Channels

1. 🎰 KuyaPlay Promotion - @kuyaplay_CS
2. 📊 Betting Tips - @scorehuntertips
3. 📰 Sport News - @scorehuntersports
4. 🎮 Live CS - @AhBoy_CS

## Deployment on Render

1. Fork this repository to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set environment variable `TELEGRAM_TOKEN`
5. Deploy!

## Local Development

```bash
pip install -r requirements.txt
export TELEGRAM_TOKEN="your_bot_token"
python app.py