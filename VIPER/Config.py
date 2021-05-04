import os
from . import versions

_REPO = Repo()
_LOG = logging.getLogger(__name__)
logbot.reply_last_msg("Setting Configs ...")


class Config:

    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    STRING_SESSION = os.environ.get("HU_STRING_SESSION")
    OWNER_ID = tuple(filter(lambda x: x, map(int, os.environ.get("OWNER_ID", "0").split())))
    DB_URI = os.environ.get("DATABASE_URL", None)
# COPYRIGHT TEAM DYNAMIC
# DYNAMIC
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY")
    OPEN_WEATHER_MAP = os.environ.get("OPEN_WEATHER_MAP")
    REMOVE_BG_API_KEY = os.environ.get("REMOVE_BG_API_KEY")
    TZ_NUMBER = os.environ.get("TZ_NUMBER", 1)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID")
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET")
    G_DRIVE_PARENT_ID = os.environ.get("G_DRIVE_PARENT_ID")
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK")
    GOOGLE_CHROME_DRIVER = os.environ.get("GOOGLE_CHROME_DRIVER")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN")
    HEROKU_ENV = bool(int(os.environ.get("HEROKU_ENV", "0")))
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    G_DRIVE_IS_TD = os.environ.get("G_DRIVE_IS_TD") == "true"
    TMP_DOWNLOAD_DIRECTORY = os.environ.get(
        "TMP_DOWNLOAD_DIRECTORY",
        "./DOWNLOADS/"
    )

    OFFICIAL_UPSTREAM_REPO = os.environ.get(
        "OFFICIAL_UPSTREAM_REPO",
        "https://github.com/TeamDynamic/Dynamic-Userbot-Pyrogram"
    )
    ALLOWED_CHATS = filters.chat([])
    ALLOW_ALL_PMS = True
    USE_USER_FOR_CLIENT_CHECKS = False
    SUDO_ENABLED = False
    SUDO_USERS: Set[int] = set()
    ALLOWED_COMMANDS: Set[str] = set()
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] \
        if HEROKU_ENV and HEROKU_API_KEY and HEROKU_APP_NAME else None
    STATUS = None
