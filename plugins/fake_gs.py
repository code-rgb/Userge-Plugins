"""Get a user-customised google search meme!"""

# Plugin By - XlayerCharon[XCB]
# TG ~>>//@CharonCB21 

import asyncio
import os 
from PIL import Image, ImageDraw, ImageFont
from userge import userge, Message
from wget import download


@userge.on_cmd("fgs", about={
    'header': "Get a user-customised google search meme!",
    'usage': "{tr}fgs [UpperText] ; [LowerText]",
    'examples': "{tr}fgs Who Made this plugin? ; @CharonCB21"})
async def FakeGoogleSearch(message: Message):
    """ Get a user-customised google search meme! """
    text = message.input_str
    if not text:
        return await message.err("No input found!", del_in=5)
    if ";" in text:
        search, result = text.split(";", 1)
    else: 
        return await message.err("Invalid Input! Check help for more info!", del_in=5)
      
    await message.delete()
    await asyncio.sleep(2)
    img='https://imgur.com/download/ShaVox7/fgs'
    r=download(img)
    photo=Image.open(r)
    drawing=ImageDraw.Draw(photo)
    blue=(0,0,255)
    black=(0,0,0)
    font1=ImageFont.truetype("resources/ProductSans-BoldItalic.ttf",20)
    font2=ImageFont.truetype("resources/ProductSans-Regular.ttf",23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    photo.save("Downloads/test.jpg")
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    await message.client.send_photo(
        message.chat.id,
        'downloads/test.jpg',
        reply_to_message_id=reply_id)
    os.remove('Downloads/test.jpg')
