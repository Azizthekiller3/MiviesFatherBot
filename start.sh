#!/bin/bash
set -e

PYTHON=/nix/store/010r29jy64nj14dx7fabacypr4f2q077-python3-3.11.9-env/bin/python3
VENV=/home/runner/workspace/MiviesFatherBot/.venv
BOT_DIR=/home/runner/workspace/MiviesFatherBot

cd $BOT_DIR

# Create venv if not exists
if [ ! -f "$VENV/bin/python3" ]; then
    echo "Creating virtual environment..."
    $PYTHON -m venv $VENV
fi

PIP=$VENV/bin/pip
VPYTHON=$VENV/bin/python3

echo "Installing dependencies..."
$PIP install --quiet --upgrade pip
$PIP install --quiet pyrofork "pyromod==1.5" "aiofiles==22.1.0" "aiohttp==3.8.3" tgcrypto requests beautifulsoup4
$PIP install --quiet "pymongo[srv]==3.12.3" "marshmallow==3.14.1" "umongo==3.0.1" "motor==2.5.1"
$PIP install --quiet yt-dlp youtube-search-python youtube-search telegraph python-dotenv
$PIP install --quiet pytz ujson hachoir humanize numpy "gTTS==2.3.1" Pillow "psutil==5.9.4"
$PIP install --quiet "dnspython==2.3.0" opencv-python-headless wget
$PIP install --quiet "git+https://github.com/TheBlackxyz/cinemagoer"

echo "Starting MiviesFather Bot..."
$VPYTHON bot.py
