import re
import os
from os import getenv, environ




api_id = int(environ.get("api_id", "22946135"))
api_hash = environ.get("api_hash", "93e1b0c387cabe34a3ccfa1724ae8527")
SUDO_USERS = int(environ.get("SUDO_USERS", "5827915041"))
bot_token = environ.get("bot_token", "7313088857:AAFTKLis7R15rOsxgKuzVHNAZjzbNRCqUlc")
OWNER_ID = int(environ.get("OWNER_ID", "7062964338"))

/upload To use the bot and Plz Donate Some Amount
𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.
<code>PandaWep@ybl</code>"""
DONATE_TXT = """<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> <code>PandaWep@ybl</code>"""
