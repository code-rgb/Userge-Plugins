#Those pro noob blah blah commands -_-

"""Pro Noob Blah Blah"""
import re, asyncio
from collections import deque
from asyncio import sleep
from re import sub
from userge import userge, Message


@userge.on_cmd("unoob$", about={'header': "You Noob"})
async def unoob_(message: Message):
    """unoob"""
    animation_interval = 1
    animation_ttl = range(9)
    await message.edit("unoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
    ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 9])
            

@userge.on_cmd("menoob$", about={'header': "I'm Noob"})
async def menoob_(message: Message):
    """menoob"""
    animation_interval = 1
    animation_ttl = range(9)
    await message.edit("menoob")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "BiGGeSt",
        "NoOoB",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
    ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 9])
            
            
@userge.on_cmd("upro$", about={'header': "You Pro"})
async def upro_(message: Message):
    """upro"""
    animation_interval = 1
    animation_ttl = range(9)
    await message.edit("upro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "YoU",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
    ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 9])
            
            
@userge.on_cmd("mepro$", about={'header': "I'm Pro"})
async def upro_(message: Message):
    """mepro"""
    animation_interval = 1
    animation_ttl = range(9)
    await message.edit("mepro")
    animation_chars = [
        "EvErYbOdY",
        "iZ",
        "PeRu",
        "uNtiL",
        "i",
        "aRriVe",
        "😈",
        "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
    ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 9])
