"""Last FM"""

from userge import userge, Message


@userge.on_cmd("lastfm", about={
    'header': "Get LastFm songs via inline"}, allow_channels=False)
async def last_fm_(message: Message):
    """Last FM via @lastfmrobot"""
    inline_msg = await userge.get_inline_bot_results(
            "lastfmrobot",
            ""
    )
    if inline_msg.switch_pm and inline_msg.switch_pm.start_param == "set":
        return await message.edit(
            "**Set Up Last Fm Bot First !**\nGoto @lastfmrobot do /set\n"
            "then follow the instructions"
        )
    await message.delete()
    await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=inline_msg.query_id,
            result_id=inline_msg.results[0].id
    )
