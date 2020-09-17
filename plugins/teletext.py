# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

from html_telegraph_poster import TelegraphPoster
from userge import userge, Message
import time


@userge.on_cmd("tg", about={'header': "For Posting Text on Telegraph",
  'usage': "{tr}tg Title [reply to text]"})
async def tele_text(message: Message):
    """Paste on Telegra.ph"""
    start = time.time()
    replied = message.reply_to_message
    if not replied:
        await message.err("Reply To Message First !", del_in=5)
        return
    if not replied.text:
        await message.err("Replied Message Doesn't Contain Text. 🤨", del_in=5)
        return
    await message.edit("Pasting...")
    t = TelegraphPoster(use_api=True)
    t.create_api_token('USERGE-X')
    user = await userge.get_me()
    user_n = f"@{user.username}" if user.username else user.first_name
    text = replied.text
    title = message.input_str
    if not title:
        title = f"By {user_n}"
    link = t.post(title=title, author=user_n, text=text)
    msg = "**Pasted to -** "
    msg += f"<a href={link['url']}>{link['path']}</a>\n"
    end = time.time()
    total = "{:.2f}".format(end - start)
    msg += f"in <code>{total}</code> sec"
    await message.edit(msg,  disable_web_page_preview=True)
