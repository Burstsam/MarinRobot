import os
import urllib

import aiohttp
import requests
from pyrogram import filters
from Flare_Robot import pbot


@pbot.on_message(filters.command("memes"))
async def memes(client, message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            "https://meme-api.herokuapp.com/gimme/wholesomememes"
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r["url"], caption=r["title"])




help = """
• /memes*:* Get Some Fresh Memes
"""
    
mod_name = "Meme"
