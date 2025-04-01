import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps.
API_ID = int(getenv("API_ID", "28228075"))
API_HASH = getenv("API_HASH", "785f20222ea7de471d714c1d563c59df")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7593985219:AAFS8C5ElPGJ8kF9KdEaJCAnQP0Twk1EmlA")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","silent_aura")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "ll_shilpa_music_ll_bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "SOMUMUSIC")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "Cuteshizu")
EVALOP = list(map(int, getenv("EVALOP", "6656608288  6656608288").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://manoranjanhor43:somuxd@manoranjan.wsglmdq.mongodb.net/?retryWrites=true&w=majority&appName=Manoranjan")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002100433415))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7070591202))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/tutorialwindoxIk/somuishu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/somueditingzone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/somueditingzone")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get @tmm_string_bot session from @tmm_STRING_BOT
STRING1 = getenv("STRING_SESSION", "BQG0OpUAMDEpck1hjcd447vCrDQCYbE2XwEjpGzQTpZw51kCWG1lYt_3O2euUOzeyDmNfe3vWAepTxLXsxQrxHIAqRWDlMHEL8uzPalqC9pIstUXsGrOi7qjVvjoUwbue2ul_JN6kVwnm5yNltCInyNCfqlYPiB8lIbp4IrMywY4ooFR-WKjReHZ7KPsxeimTtEB8RnW2OFucw0RdX6heB1K3GOs-SavwCNdxCDGyLtcLXa244X0NRC1L4QfzxZal1H1nwmCNRuTdIPrcM66mW5r3D8bFvEMCpfLeas-FhdFJ4MSj7_tm-q1h-3UL_nShSzOm4BlU2gUEK1upQm3EWtxJMxBAAAAAAHfjZBmAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AMBOT = [
    "𓄂sʜɪʟᴘᴀ 〄 ᴍᴜsιᴄ...𝐏ɤσƈɛssɩŋʛ🦋"
]
AMOP = ["🚩ʜᴀʀ ʜᴀʀ ᴍᴀʜᴀᴅᴇᴠ 🚩\n🚩ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ🚩\n🚩ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {0}🍷\n\n❥ sᴏᴍυ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ᴛʜɪs ʙᴏᴛ ɪs ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ʟɪsᴛᴇɴ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ \n────────────────── \n➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ  ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\nʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ [๛ᴍʀsᴏᴍᴜ࿐](https://t.me/alone_somu6)"
       ]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/58e1e93e1e90a4e99dc2a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/00360393a15daf7fc4e9d.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/78ac6fc48e240895e5ec8.jpg"
STATS_IMG_URL = "https://graph.org/file/6abe3a913bf645b5b89ce.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/443076090048170968b90.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/0c40d1fc5f17c524a6c16.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/bc0844a1139b5214ba78f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
