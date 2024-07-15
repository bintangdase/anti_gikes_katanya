import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6672829481:AAFhs_MWAGVA4PxQ-IhbHoQXrOcx4LXS5CU")
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

APP_ID = int(os.environ.get("APP_ID", "27057469"))
API_HASH = os.environ.get("API_HASH", "4244e8924b0cb5c6e061b4767bc8b003")

LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1002214254535"))

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://ankes:apaanke1@antkes.hxaq4uq.mongodb.net/?retryWrites=true&w=majority&appName=antkes")
DB_NAME = os.environ.get("DB_NAME", "suckkmydicks")
BROADCAST_AS_COPY = True

PLUG = dict(root="antigcast/plugins")

OWNER_ID = [int(x) for x in (os.environ.get("OWNER_ID", "6996341586").split())]
OWNER_NAME = os.environ.get("OWNER_NAME", "DANTE")


LOG_FILE_NAME = "antigcast_logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

