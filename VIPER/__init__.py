import logging
import os
import platform
import sys
import time
from inspect import getfullargspec

from pydrive.auth import GoogleAuth
from pyrogram import Client
from pyrogram import errors
from pyrogram.types import Message
from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker



StartTime = time.time()

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    logging.error('Python version Lower than 3.6! Abort!')
    sys.exit()

VIPER_VERSION = '0.1'
ASSISTANT_VERSION = '0.1'

# IMPORTANT VARS
LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_COMPANION_BOT = Config.TG_COMPANION_BOT
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
