# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

"""Detects Nsfw content with the help of A.I."""

import os
import requests
from userge import userge, Message, Config
from userge.utils import media_to_image


VARS = Config.HEROKU_APP.config()


@userge.on_cmd("detect", about={
    'header': "Scan media for nsfw content",
    'usage': "{tr}detect [reply to media]"})
async def detect_(message: Message):
    """detect nsfw"""
    reply = message.reply_to_message
    if not reply:
        await message.err("reply to media !", del_in=5)
        return
    if "DEEP_AI" not in VARS:
        await message.edit("add VAR `DEEP_AI` get Api Key from https://deepai.org/", del_in=7)
        return
    api_key = VARS['DEEP_AI']
    photo = await media_to_image(message)
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            'image': open(photo, 'rb'),
        },
        headers={'api-key': api_key}
    )
    os.remove(photo)
    if 'status' in r.json():
        await message.err(r.json()['status'], del_in=6)
        return
    r_json = r.json()['output']
    pic_id = r.json()['id']
    percentage = r_json['nsfw_score'] * 100
    detections = r_json['detections']
    result = "<b><u>Detected Nudity</u> :</b>\n[>>>](https://api.deepai.org/job-view-file/{}/inputs/image.jpg) <code>{:.3f} %</code>\n\n".format(pic_id, percentage)

    if detections:
        for parts in detections:
            name = parts['name']
            confidence = int(float(parts['confidence']) * 100)
            result += f"• {name}:\n   <code>{confidence} %</code>\n"
    await message.edit(result, disable_web_page_preview=True)
    
