# MiviesFather AutoFilter Bot

A powerful Telegram AutoFilter bot for **Miviesfather** — indexes movies and files from Telegram channels and lets groups search and retrieve them instantly.

## Features

- 🎬 Auto-indexes files from Telegram channels
- 🔍 Full-text search with regex support
- 📁 Supports movies, series, and all file types
- 🔗 Inline search results with file links
- 👥 Group filter management
- 🛡️ Force subscribe / join request support
- 📊 IMDB info integration
- 🚫 Banned users & chats management
- 📡 Multi-channel indexing
- ⚡ Fast MongoDB-powered search

## Setup

### Required Environment Variables

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Your Telegram Bot Token (from @BotFather) |
| `API_ID` | Telegram API ID (from my.telegram.org) |
| `API_HASH` | Telegram API Hash (from my.telegram.org) |
| `DATABASE_URI` | MongoDB Atlas connection string |

### Optional Environment Variables

| Variable | Default | Description |
|---|---|---|
| `LOG_CHANNEL` | `0` | Channel ID for bot logs |
| `ADMINS` | `` | Space-separated admin user IDs |
| `CHANNELS` | `` | Space-separated channel IDs to index |
| `AUTH_CHANNEL` | `` | Force-subscribe channel ID |
| `DATABASE_NAME` | `MiviesFatherDB` | MongoDB database name |
| `COLLECTION_NAME` | `Telegram_files` | MongoDB collection name |
| `MAX_RIST_BTNS` | `10` | Max results per search |
| `IMDB` | `True` | Enable IMDB info |
| `SINGLE_BUTTON` | `True` | Single button mode |
| `PROTECT_CONTENT` | `False` | Protect forwarded files |
| `SHORT_URL` | `yamlinks.com` | URL shortener domain |
| `SHORT_API` | `` | URL shortener API key |
| `GRP_LNK` | `https://t.me/Miviesfather` | Support group link |
| `CHNL_LNK` | `https://t.me/Miviesfather` | Channel link |

## Running

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

## Stack

- **Python 3.11**
- **Pyrogram** (Telegram MTProto client)
- **Motor** (async MongoDB driver)
- **MongoDB Atlas** (database)
- **aiohttp** (web server for keep-alive)

## Credits

Bot by **@Miviesfather**

> For support: [Telegram](https://t.me/Miviesfather)
