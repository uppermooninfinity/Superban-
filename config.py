import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

#--------------------------------
load_dotenv()

#--------------------------------
API_ID = 39679517
API_HASH = "aed61e5ff8c711895f8b0c99e51c16cc"
BOT_TOKEN = "8451766490:AAFbP9bWAEWr9nGoSb8rRM5LyidxYLR3r-g"
MONGO_DB_URI = "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#--------------------------------
SUPERBAN_CHAT_ID = -1003228624224
STORAGE_CHANNEL_ID = -1003852280111
AUTHORS = [7651303468]

#--------------------------------
String_client_1 = "AQJddh0APZpFgUYUqjpz_R2XxA0qiVoUT1aQlM-07mWV-b0Cdp3-nn6KtmeInHqSgdTz-5JYMnRcl6dEcvJwlvPPHybwjOdBrKVSAJsBLP-B5QqRdOJPRCVKysXh2V66nWcdwSKQ-YGQtPJYEflBRCaz8avq9paDm_hop6D7i68wS2VXY64Lkhs5_Cl4z1aDH7cqwTpXhlpvae1eUg76hYY0_fprQHq06xFd3zNtyS2gfx5ruvfBp39G3WHx9OLkBdOS6DL6SunhOMF9qoQxBLJvphbAhcMJIDNSwlh-s44udKLEZjl5fsx1HzTPyJfasohJmq9kO0Jk-ZvtMULreoRxbnC16gAAAAHZk9LIAAAQIP33AANEizZ3BxPJi5EJg2Iyr75eKBEMT2CtpM2RFBIfOXeBVGgTj2fVVGLS2mDimjibRErtVS1ZDRJ3RwcIG8RrOiEsr95lcGZh_8MMBuB1usugJd5ILTmavBSNAdXokceODHf1CGC3uOnlSw_8oEAkHk8O7tu_V3LUfNHYZ33aRW-cabo3R9U5KL349PcrgyF4UhOF77RROS6nRIegO0G1rtQHEFslaWJ27opnD2pVmOYnr3ToLIykCAgHsH3lZnNFehwp_viBAaqnH650x4UEiJfRkZha6mEa1tdtJ_2pzOMEg9LoR2yahLvG_Cd_MKVVOZAwWE17SoqQ64O6QZtNchrgAAAAHN07JeAA"
String_client_2 = "AQIP33AANEizZ3BxPJi5EJg2Iyr75eKBEMT2CtpM2RFBIfOXeBVGgTj2fVVGLS2mDimjibRErtVS1ZDRJ3RwcIG8RrOiEsr95lcGZh_8MMBuB1usugJd5ILTmavBSNAdXokceODHf1CGC3uOnlSw_8oEAkHk8O7tu_V3LUfNHYZ33aRW-cabo3R9U5KL349PcrgyF4UhOF77RROS6nRIegO0G1rtQHEFslaWJ27opnD2pVmOYnr3ToLIykCAgHsH3lZnNFehwp_viBAaqnH650x4UEiJfRkZha6mEa1tdtJ_2pzOMEg9LoR2yahLvG_Cd_MKVVOZAwWE17SoqQ64O6QZtNchrgAAAAHN07JeAA"
String_client_3 = ""
Mustjoin = "snowy_hometown"

#--------------------------------
SUPERBAN_REQUEST_TEMPLATE = """ᴀᴘᴘʀᴏᴠᴇ sᴜᴘᴇʀʙᴀɴ ꜰᴏʀ ᴜꜱᴇʀ :
{user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɪᴅ : {chat_id}
ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɴᴀᴍᴇ : {chat_name}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ᴅᴀᴛᴇ & ᴛɪᴍᴇ : {ind_time}
ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERBAN_REQUEST_RESPONSE = """ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴛᴇᴀᴍ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ʏᴏᴜʀ ʀᴇQᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄʜᴇᴄᴋᴇᴅ ᴀɴᴅ ɪꜰ ɪᴛ'ꜱ ɢᴇɴᴜɪɴ ᴛʜᴇɴ ʙᴇ ꜱᴜʀᴇ ɪᴛ ᴡɪʟʟ ʙᴇ ᴀᴘᴘʀᴏᴠᴇᴅ.
ᴛʜᴀɴᴋꜜs ꜰᴏʀ ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @snowy_hometown
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERBAN_APPROVED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ, ɴᴏᴡ ꜱᴛᴀʀᴛɪɴɢ sᴜᴘᴇʀʙᴀɴ.....

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERBAN_DECLINED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇᴄʟɪɴᴇᴅ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴅᴇᴄʟɪɴᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERBAN_COMPLETE_TEMPLATE = """sᴜᴘᴇʀʙᴀɴ ɪꜱ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.

ᴜꜱᴇʀ : {user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇᴀꜱᴏɴ : {reason}
ᴛᴏᴛᴀʟ ʙᴀɴ ɪɴ ꜰᴇᴅꜱ : {fed_count}
ɢʙᴀɴ ɪɴ : {extra_bans}

ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴛɪᴍᴇ ᴛᴀᴋᴇɴ : {time_taken}

ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @snowy_hometown
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

#--------------------------------
SUPERUNBAN_REQUEST_TEMPLATE = """ᴀᴘᴘʀᴏᴠᴇ sᴜᴘᴇʀᴜɴʙᴀɴ ꜰᴏʀ ᴜꜱᴇʀ :
{user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɪᴅ : {chat_id}
ʀᴇQᴜᴇꜱᴛ ꜰʀᴏᴍ ᴄʜᴀᴛ ɴᴀᴍᴇ : {chat_name}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ᴅᴀᴛᴇ & ᴛɪᴍᴇ : {ind_time}
ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}

ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERUNBAN_REQUEST_RESPONSE = """ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇɴᴅᴇᴅ ᴛᴏ ᴛᴇᴀᴍ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀᴜɴʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ʀᴇQᴜᴇꜱᴛ ʙʏ : {request_by}

ʏᴏᴜʀ ʀᴇQᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄʜᴇᴄᴋᴇᴅ ᴀɴᴅ ɪꜰ ɪᴛ'ꜱ ɢᴇɴᴜɪɴ ᴛʜᴇɴ ʙᴇ ꜱᴜʀᴇ ɪᴛ ᴡɪʟʟ ʙᴇ ᴀᴘᴘʀᴏᴠᴇᴅ.
ᴛʜᴀɴᴋꜜs ꜰᴏʀ ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @snowy_hometown
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERUNBAN_APPROVED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ, ɴᴏᴡ ꜱᴛᴀʀᴛɪɴɢ sᴜᴘᴇʀᴜɴʙᴀɴ.....

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀᴜɴʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERUNBAN_DECLINED_TEMPLATE = """ʏᴏᴜʀ sᴜᴘᴇʀᴜɴʙᴀɴ ʀᴇQᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇᴄʟɪɴᴇᴅ

ʀᴇQᴜᴇꜱᴛ ᴛᴏ sᴜᴘᴇʀᴜɴʙᴀɴ
ᴜꜱᴇʀ : {user_first}

ʀᴇᴀꜱᴏɴ : {reason}
ᴅᴇᴄʟɪɴᴇᴅ ʙʏ ᴀᴜᴛʜᴏʀ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""

SUPERUNBAN_COMPLETE_TEMPLATE = """sᴜᴘᴇʀᴜɴʙᴀɴ ɪꜱ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.

ᴜꜱᴇʀ : {user_first}
ᴜꜱᴇʀ ɪᴅ : {user_id}

ʀᴇᴀꜱᴏɴ : {reason}
ᴛᴏᴛᴀʟ ᴜɴʙᴀɴ ɪɴ ꜰᴇᴅꜱ : {fed_count}
ɢᴜɴʙᴀɴ ɪɴ : {extra_bans}

ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ : {approval_author}

ᴜɴɪᴠᴇʀꜱᴀʟ ᴛɪᴍᴇ : {utc_time}
ᴛɪᴍᴇ ᴛᴀᴋᴇɴ : {time_taken}

ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : @snowy_hometown
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @dark_musictm"""
#--------------------------------

START_VIDEO = "https://files.catbox.moe/dvij1v.mp4"
HELP_MENU_VIDEO = "https://files.catbox.moe/dvij1v.mp4"

#--------------------------------
LOGGER_ID = -1003228624224
STATS_VIDEO = "https://files.catbox.moe/dvij1v.mp4"
OWNER_ID = 7651303468

#--------------------------------
CLIENT_CHAT_DATA = [
    {
        "session": String_client_1,
        "chat_ids": [-1002746914942],
        "messages": [
            "/Joinfed 1111-aaaa",
            "/fban {user_id} {reason} \n\nApproved by {approver} \nTime: {utc_time}"
        ]
    },
    {
        "session": String_client_2,
        "chat_ids": [-1002871771020],
        "messages": [
            "/Joinfed 2222-bbbb",
            "/fban {user_id} Reason: {reason} \n\nDone by {approver}"
        ]
    },
    {
        "session": String_client_3,
        "chat_ids": [-1003333333333],
        "messages": [
            "/Joinfed 3333-cccc",
            "Ban user {user_id} - Reason: {reason} - By: {approver}"
        ]
    },
]

#--------------------------------
CLIENT_CHAT_DATA2 = [
    {
        "session": String_client_1,
        "chat_ids": [-1002746914942],
        "messages": [
            "/Joinfed 1111-aaaa",
            "/fban {user_id} {reason} \n\nApproved by {approver} \nTime: {utc_time}"
        ]
    },
    {
        "session": String_client_2,
        "chat_ids": [-1002222222222],
        "messages": [
            "/Joinfed 2222-bbbb",
            "/fban {user_id} Reason: {reason} \n\nDone by {approver}"
        ]
    },
    {
        "session": String_client_3,
        "chat_ids": [-1003333333333],
        "messages": [
            "/Joinfed 3333-cccc",
            "Ban user {user_id} - Reason: {reason} - By: {approver}"
        ]
    },
]

#--------------------------------

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

#--------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dark_musictm")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/snowy_hometown")

#--------------------------------
if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")
