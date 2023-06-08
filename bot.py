import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5966666716:AAHIXeBsuFAi9sq4H0TGQjhm0KA9hpfzZL8")

API_ID = int(os.environ.get("API_ID", "29616312"))

API_HASH = os.environ.get("API_HASH", "dd1a05ab4c47a5a037cc067cf4bded27")

STRING = os.environ.get("STRING", "1BVtsOMMBu0RMh0aCWzTa2JpntwHSjksPOC1O-g4W7UTN98t3Xz4ZlUa9wFVSvPrvQ_vf_pGrmhMMMzpIqz6vwWbkymUH54vFybqbmiElXn1dE6PpPI2Rq-5eoulNX4QFGD39bICusqcsiDHdtt0bcJ_ZL3KYg5bC7TXDxQb_ZaafFEeIFxSVG-WTLE_Xil4t46LTBbGlZZppVKKtF03nRIzYDjNpoxFtUm0cOEWOTd_N52S29orMLJY8n9UNPSBh9iT6B0LIhT-oGDG0o1QTi8QZaD0Ba3NJZCSBdjhaQjyfPMJqdcmm9Lv1HHCckj-Fs9FPVrOboFToyRSUWWF1m1_fRAcWMjU=")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
