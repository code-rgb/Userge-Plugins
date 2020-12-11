#https://github.com/midnightmadwalk/mutation
import asyncio
import os
import shutil

from pathlib import Path

from userge import Message, userge
from userge.utils import runcmd
from userge.plugins.misc.upload import upload


@userge.on_cmd(
    "merge",
    about={
        "formats": "mp4 mp3 mkv webm",
        "usage": "{tr}merge mp4/mp3/mkv/webm",
        "example": "reply first video with {tr}download a.format and second with {tr}download b.format then do {tr}merge format"
    },
)
async def ffmpeg(message: Message):
    """MergeMedia with FFmpeg"""
    x = message.input_str
    if not x:
        await message.edit("`enter valid extension check .help mergemedia`")
    else:
    	bar = "downloads/output." + x
    	foo = "file 'a." + x + "'" + "\n" + "file 'b." + x + "'"
    	x = open('downloads/merge.txt', 'w+')
    	x.write(foo)
    	x.close()
    	await message.edit("`processing your`"+" "+x+" "+"`files`")
    	await runcmd(f"ffmpeg -f concat -i downloads/merge.txt -map 0 -c copy -scodec copy {bar}")
        await message.edit("`Uploading`")
        await upload(message, Path(bar))
        y = "./downloads"
        if os.path.exists(y):
        	shutil.rmtree(y)
        	if not os.path.exists(y):
        		os.mkdir(y)
