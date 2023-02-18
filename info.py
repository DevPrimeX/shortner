import os, re
from os import environ
from dotenv import load_dotenv
load_dotenv()
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8080")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '27639102'))
API_HASH = environ.get('API_HASH', '35142c1407be6264e68fb6bec5dcabd9')
BOT_TOKEN = environ.get('BOT_TOKEN', "6106344962:AAHhzsZSOvgvPr8z9Tp-7h8r1dU4jsAKtPM")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/b78ab94dcc0d698656abf.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5606411877').split()]
ADMINS = (ADMINS.copy() + [5606411877])
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001375419446').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5606411877').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
reqst_channel = environ.get('REQST_CHANNEL_ID')
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Multibot123:Multibot123@cluster0.qnuoqak.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Clusgjgc")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
PLAN_NAME = environ.get('PLAN_NAME', 'Not Active')
EXP_DATE = environ.get('EXP_DATE', 'Not Active')
SUB_DATE = environ.get('SUB_DATE', 'Not Active')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001834678099'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'vj_bot_disscussion')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "ɴᴀᴍᴇ: <code>{file_name}</code> \n\n [𝘼𝙡𝙡 𝙉𝙚𝙬 𝙈𝙤𝙫𝙞𝙚𝙨 𝙐𝙥𝙙𝙖𝙩𝙚𝙨 𝙃𝙚𝙧𝙚](https://t.me/vj_bots)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "ɴᴀᴍᴇ: <code>{file_name}</code> \n\n [𝘼𝙡𝙡 𝙉𝙚𝙬 𝙈𝙤𝙫𝙞𝙚𝙨 𝙐𝙥𝙙𝙖𝙩𝙚𝙨 𝙃𝙚𝙧𝙚](https://t.me/vj_bots)</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b><i>📟 ᴛɪᴛᴛʟᴇ :</b></i> {title} \n<b><i>🌟 ʀᴀᴛɪɴɢ :</b></i> {rating} \n<b><i>🎭 ɢᴇɴʀᴇ :</b></i> {genres} \n<b><i>📆 ʀᴇʟᴇᴀsᴇ :</b></i> {year} </b></i>\n<b><i>⏰ ᴅᴜʀᴀᴛɪᴏɴ :</b></i> {runtime}\n\n<b><i>🔖 𝓟𝓵𝓸𝓽  :</b></i> `{plot}` \n\n<b><i>⚡ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ⚡ :</b></i> {message.chat.title}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
# URL Shortener #

SHORTLINK_URL = environ.get('SHORTLINK_URL', 'mdisklink.link')
SHORTLINK_API = environ.get('SHORTLINK_API', 'a21d381121da4bae1dd61d5c7dc7ae8de52e6041')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 3000))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/How_To_Open_Linkl"

   # Custom Caption Under Button #
CAPTION_BUTTON = "JOIN MY CHANNEL"
CAPTION_BUTTON_URL = "https://t.me/VJ_Bots"


   # Auto Delete For Bot Sending Files #
    

BLACKLIST_WORDS = (
    list(os.environ.get("BLACKLIST_WORDS").split(","))
    if os.environ.get("BLACKLIST_WORDS")
    else []
)

BLACKLIST_WORDS = ["[D&O]", "[MM]", "[]", "[FC]", "[CF]", "LinkZz", "[DFBC]", "@New_Movie", "@Infinite_Movies2", "MM", "@R A R B G", "[F&T]"]


