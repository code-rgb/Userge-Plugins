#by darkrider frame from deleteduser420
import os

PATH = 'downloads/temp_vid.mp4'

reply = message.reply_to_message

if not (reply.audio):

    return

audio_thumb = reply.audio.thumbs[0].file_id

thumb = await userge.download_media(audio_thumb)

if not thumb:

    return

music = await reply.download()

os.rename(music, 'music.mp3')

os.rename(thumb, 'thumb.jpg')

os.system(f'ffmpeg -loop 1 -i thumb.jpg -i music.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf \"scale=\'iw-mod (iw,2)\':\'ih-mod(ih,2)\',format=yuv420p\" -shortest -movflags +faststart downloads/temp_vid.mp4')

if os.path.exists(PATH):

    await message.reply_video_note(PATH)

    os.remove(PATH)

    os.remove('music.mp3')

    os.remove('thumb.jpg')
