# File ini bagian dari Repositori: github.com/raflydtya/menfess-tbot Akun: @raflydtya
# Nama: bot.py | Python Telegram Bot
# Copyright 2022. All Right Reserved.

import html
import time, asyncio, sys, random, inspect, re, logging
from telethon import TelegramClient, events, utils
from typing import Optional

api_id = 2857053 
api_hash = '4a01e3596661ba4bf609d15c1f9e129b'
sesi_file = 'menfessbot'
bot_token = '6176925571:AAE580KWJZm1scSYh-ltJcd0xsBC-Ytm0Ns'

menfessbot = TelegramClient(sesi_file, api_id, api_hash).start(bot_token=bot_token)

group = '<caritemangobrol>'
ch = '<tesssmanfess>'

def menfess(**args):
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!.]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        client.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator

FOTO = "<isi link media foto telegraph>"
@menfess(pattern=("/start"))
async def start(event):
  TEXT = f"Halo {event.sender.first_name}!\n"
  TEXT+= f"Ini adalah bot Menfess di Telegram. Kirim pesanmu dengan trigger (....), maka pesanmu akan terkirim ke (.....)"
  BUTTON = [[Button.url("Grup", group)]]
  await bot.send_file(event.chat_id, FOTO, caption=TEXT, buttons=BUTTON )
  print(time.asctime(), '|', event.sender.first_name, '|', event.sender.username, '|', event.sender.id, '|', 'Started Bot' )

@menfessbot.on(events.NewMessage)
async def handler(event):
        pesan = event.raw_text
 
         if '<.>' in pesan:
            time.sleep(0.5)
            await bot.send_message(<group/ch>, pesan)
            return

with menfessbot:
    print(time.asctime(), '-', '--BOT STARTED--')
    menfessbot.run_until_disconnected()
