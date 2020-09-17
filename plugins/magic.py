#By @deleteduser420
""" Invert, filp/mirror, rotate """
import os
import time
from PIL import Image, ImageOps
from userge import userge, Message, Config
from userge.utils import media_to_image


@userge.on_cmd("(invert|mirror|flip)$", about={
    'header': "Invert, Mirror or Flip any media",
    'usage': "{tr}invert [reply to any media]\n"
             "{tr}mirror [reply to any media]\n"
             "{tr}flip [reply to any media]"}, name="transform")
async def transform(message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.err("<code>Give Me Something to transform (¬_¬)</code>")
        await message.client.send_sticker(
            sticker="CAADAQADhgADwKwII4f61VT65CNGFgQ", chat_id=message.chat.id)
        return 
    transform_choice = message.matches[0].group(1).lower()
    choice_string = transform_choice.capitalize()
    await message.edit(f"<code>{choice_string}ing Media!...</code>")
    dls_loc = await media_to_image(message)
    if not dls_loc:
        return
    webp_file = await transform_media(dls_loc, transform_choice)
    await message.client.send_sticker(
        chat_id=message.chat.id,
        sticker=webp_file,
        reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)
    
    
async def transform_media(image_path, transform_choice):
    im = Image.open(image_path)
    os.remove(image_path)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    if transform_choice == "flip":
        out = ImageOps.flip(im)
    elif transform_choice == "invert":
        out = ImageOps.invert(im)
    else:
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
    image_name = "invert.webp"
    webp_file = os.path.join(Config.DOWN_PATH, image_name)
    out.save(webp_file, "WebP")
    return webp_file

"""Rotate any media"""
@userge.on_cmd("rotate", about={
    'header': "Rotate any media",
    'usage': "{tr}rotate [angle to rotate] [reply to media]\n" 
             "angle = 0 to 360(default is 90)"})
    
async def rotate_(message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.err("<code>Give Me Something to Rotate (¬_¬)</code>")
        await message.client.send_sticker(
            sticker="CAADAQADhgADwKwII4f61VT65CNGFgQ", chat_id=message.chat.id)
        return
    if message.input_str:
        input_ = int(message.input_str)
        if not message.input_str.isdigit():
            await message.err("```You input is invalid, check help...```", del_in=5)
            return
        if not 0 < input_ < 360:
            await message.err("```Invalid Angle...```", del_in=5)
            return
        args = input_
    else:
        args = 90
    await message.edit(f"<code>Rotating Media by {args}°...</code>")
    dls_loc = await media_to_image(message)
    if not dls_loc:
        return   
    webp_file = await rotate_media(dls_loc, args)
    await message.client.send_sticker(chat_id=message.chat.id,
                                    sticker=webp_file,
                                    reply_to_message_id=replied.message_id)
    await message.delete()
    os.remove(webp_file)
    
async def rotate_media(image_path, args):
    im = Image.open(image_path)
    os.remove(image_path)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    angle = args
    out = im.rotate(angle, expand=True)
    image_name = "rotated.webp"
    webp_file = os.path.join(Config.DOWN_PATH, image_name)
    out.save(webp_file, "WebP")
    return webp_file