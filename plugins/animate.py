#Taken from USERGE_X and few modifications done by Bhoomi

"""Spammy Animations ☠️"""
import re, asyncio
from collections import deque
from asyncio import sleep
from re import sub
from userge import userge, Message


@userge.on_cmd("think$", about={'header': "Pretending to Think"})
async def think_(message: Message):
    """think"""
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)
		
@userge.on_cmd("lmaos$", about={'header': "lmaos Bruh! xD Lol"})
async def lamos_(message: Message):
    """lmaos"""
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)

    
@userge.on_cmd("nothappy$", about={'header': "Mood Swing"})
async def Moods_(message: Message):
    """Mood Swing"""
    deq = deque(list("😁☹️😁☹️😁☹️"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await message.edit("".join(deq))
        deq.rotate(1)
		
  
@userge.on_cmd("muah$", about={'header': "LUV"})
async def muah_(message: Message):
    """MUAH"""
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)	


@userge.on_cmd("heart$", about={'header': "Rainbow hearts"})
async def heart_(message: Message):
    """♥️"""
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)        
        
		
@userge.on_cmd("gym$", about={'header': "Get Active!, Stay healthy 💪"})
async def gym_(message: Message):
    """Gym"""
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)
    
       
@userge.on_cmd("smoon$", about={'header': "Another kensar moon animation"})
async def smoon_(message: Message):
    """smoon"""
    animation_interval = 0.1
    animation_ttl = range(50)
    await message.edit("smoon..")
    animation_chars = [

            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",    
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 8])
            
@userge.on_cmd("theart$", about={'header': "Another kensar heart animation"})
async def theart_(message: Message):
    """theart"""
    animation_interval = 0.4
    animation_ttl = range(117)
    await message.edit("theart")
    animation_chars = [

            "❤️",
            "🧡",    
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "❤️",
            "🧡",    
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "❤️",
            "🧡",    
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "❤️",
            "🧡",    
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 28])
		
		
@userge.on_cmd("tmoon$", about={'header': "Another kensar moon animation"})
async def tmoon_(message: Message):
    """tmoon"""
    animation_interval = 0.4
    animation_ttl = range(117)
    await message.edit("tmoon")
    animation_chars = [

            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",    
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 32])

@userge.on_cmd("thinking$", about={'header': "Thinking Text"})
async def thinking_(message: Message):
    """thinking"""
    animation_interval = 0.1
    animation_ttl = range(72)
    await message.edit("thinking")
    animation_chars = [

	"THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING... 🤔"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 32])
		
@userge.on_cmd("ok$", about={'header': "Okay Sar"})
async def ok_(message: Message):
    """Ook"""
    animation_interval = 0.01
    animation_ttl = range(0)
    await message.edit("thinking")
    animation_chars = [
	    "F",
            "U",
            "C",
            "K",
            "Y",
            "O",
            "U",
            "B",
            "C",
            "FK",
            "UU",
            "FCUK",
            "UOY",
            "C",
            "F",
            "Y",
            "F",
            "Ok Sar 😇"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i % 18])
