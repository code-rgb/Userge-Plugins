import asyncio

from userge import userge


@userge.on_cmd("call$", about={'header': "Ban any tg account by contacting durov"})
async def call_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    DEFAULTUSER = user['mention']
    animation_chars = [
        "```Calling Pavel Durov (ceo of telegram)......```",
        "```Connecting To Telegram Headquarters...```",
        "```Call Connected.```",
        "```Telegram: Hello This is Telegram HQ. Who is this?```",
        "```Connection Established ```",
        "```Me: Yo this is```` {DEFAULTUSER}``` ,```Please Connect me to my lil bro,Pavel Durov```",
        "```User Authorised.```",
        "```Calling Pavel Durov `  `At +916969696969```",
        "```Private  Call Connected...```",
        "```Me: Hello Sir, Please Ban This Telegram Account.```",
        "```Pavel Durov : May I Know Who Is This?```",
        "```Me: Yo Brah, I Am` {DEFAULTUSER} ```",
        "```Pavel Durov : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.```",
        "```Me: Thanks, See You Later Brah.```",
        "```Pavel Durov : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.```",
        "```Me: Is There Any Issue/Emergency???```",
        "```Pavel Durov : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.```",
        "```Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.```",
        "```Pavel Durov : Sure Sur \nTC Bye Bye :)```",
    ]
    called = (f"**Private Call Disconnected.**\n\n```BY``` {DEFAULTUSER}``` ")
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(3)
        await message.edit(animation_chars[i % max_ani])
    await message.edit(called)
