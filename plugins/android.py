from requests import get
from bs4 import BeautifulSoup
from userge import userge, Message

@userge.on_cmd("twrp", about={
    'header': "Find twrp for you device",
    'usage': "{tr}twrp <device codename>"}, allow_via_bot=True)
async def device_recovery(message: Message):
    """ Get Latest TWRP """
    replied = message.reply_to_message
    args = message.filtered_input_str
    if args:
        device = args
    else:
        await message.err("```Provide Device Codename !!```", del_in=3)
        return
    await message.delete()
    url = get(f'https://dl.twrp.me/{device}/')
    if url.status_code == 404:
            reply = f"`Couldn't find twrp downloads for {device}!`\n"
            return await message.edit(reply, del_in=5)
    page = BeautifulSoup(url.content, 'lxml')
    download = page.find('table').find('tr').find('a')
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = f'**Latest TWRP for {device}:**\n' \
            f'[{dl_file}]({dl_link}) - __{size}__\n' \
            f'**Updated:** __{date}__\n'
    await message.edit(reply)


@userge.on_cmd("magisk$", about={'header': "Get Latest Magisk Zip and Manager"})
async def magisk_(message: Message):
    """Get Latest MAGISK"""

    magisk_dict = {
            "⦁ 𝗦𝘁𝗮𝗯𝗹𝗲":
            "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
            "⦁ 𝗕𝗲𝘁𝗮":
            "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
            "⦁ 𝗖𝗮𝗻𝗮𝗿𝘆 (𝗗𝗲𝗯𝘂𝗴)":
            "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/debug.json"
    }
    releases = "<code><i>𝗟𝗮𝘁𝗲𝘀𝘁 𝗠𝗮𝗴𝗶𝘀𝗸 𝗥𝗲𝗹𝗲𝗮𝘀𝗲:</i></code>\n\n" 
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += f'{name}: [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | ' \
                        f'[APK v{data["app"]["version"]}]({data["app"]["link"]}) | ' \
                        f'[Uninstaller]({data["uninstaller"]["link"]})\n'
    await message.edit(releases, disable_web_page_preview=True)






