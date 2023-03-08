from dotenv import load_dotenv
from os import getenv, path

load_dotenv() if not path.exists("local.env") else load_dotenv("local.env")


class Config:
    api_id = int(getenv("API_ID", "2857053"))
    api_hash = getenv("API_HASH", "4a01e3596661ba4bf609d15c1f9e129b")
    bot_token = getenv("BOT_TOKEN", "6176925571:AAE580KWJZm1scSYh-ltJcd0xsBC-Ytm0Ns")
    log_channel = int(getenv("LOG_CHANNEL", "-1001515293309"))
    fsub_chid = int(getenv("FORCESUB_CHANNEL", "-1001515293309"))
    db_chid = int(getenv("DB_CHANNEL", "-1001691630680"))
    blacklisted_channel = [int(x) for x in getenv("BLACKLISTED_CHANNEL", "-1001874961981").split(",") if x is not None]
    channel1 = int(getenv("CHANNEL_1", "-1001515293309"))
    DB_URI = os.environ.get("DATABASE_URL", "")


config = Config()
