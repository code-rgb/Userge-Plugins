"""Last FM"""

# Copyright (C) 2020 BY USERGE-X
# All rights reserved.
#
# Authors: 1. https://github.com/lostb053 [TG: @Lostb053]
#          2. https://github.com/code-rgb [TG: @DeletedUser420]
#
# API: https://www.last.fm/api


import aiohttp
from userge import Config, Message, userge
from userge.utils import rand_array

API = "http://ws.audioscrobbler.com/2.0"

# In Case Song Does't have any Album Art.
PIC_URL = [
    "https://i.imgur.com/l772pcA.png",
    "https://i.imgur.com/KehK98D.png",
    "https://i.imgur.com/LuwSKeO.png",
    "https://i.imgur.com/EZ1S9cJ.png",
]


if hasattr(Config, "LASTFM_API_KEY") and (
    Config.LASTFM_API_KEY and Config.LASTFM_USERNAME
):

    @userge.on_cmd(
        "lastfm",
        about={"header": "Get Lastfm now playing pic"},
    )
    async def last_fm_pic_(message: Message):
        """now playing"""
        params = {
            "method": "user.getrecenttracks",
            "limit": 1,
            "extended": 1,
            "user": Config.LASTFM_USERNAME,
            "api_key": Config.LASTFM_API_KEY,
            "format": "json",
        }
        view_data = (await get_response(params))[1]
        if "error" in view_data:
            return await message.err(view_data["error"], del_in=5)
        recent_song = view_data["recenttracks"]["track"]
        if len(recent_song) == 0:
            return await message.err("No Recent Tracks found", del_in=5)
        rep = f"<b>[{Config.LASTFM_USERNAME}](https://www.last.fm/user/{Config.LASTFM_USERNAME})</b> is currently listening to ...\n"
        song_ = recent_song[0]
        song_name = song_["name"]
        artist_name = song_["artist"]["name"]
        rep += f"🎧  <b>[{song_name}]({song_['url']})</b> - [{artist_name}]({song_['artist']['url']})"
        if song_["loved"] != "0":
            rep += " (♥️, loved)"
        # Trying to Fetch Album of the track
        get_track = (
            (
                await get_response(
                    {
                        "method": "track.getInfo",
                        "track": song_name,
                        "artist": artist_name,
                        "api_key": Config.LASTFM_API_KEY,
                        "format": "json",
                    }
                )
            )[1]
        )["track"]
        img = (
            (get_track["album"]["image"].pop())["#text"]
            if get_track.get("album")
            else rand_array(PIC_URL)
        )
        get_tags = "\n"
        # tags of the given track
        for tags in get_track["toptags"]["tag"]:
            get_tags += f"[#{tags['name']}]({tags['url']})  "
        await message.edit(f"[\u200c]({img})" + rep + get_tags)

    @userge.on_cmd(
        "lastuser",
        about={
            "header": "Get Lastfm user info",
            "usage": "{tr}lastuser [lastfm username] (optional)",
        },
    )
    async def last_fm_user_info_(message: Message):
        """user info"""
        lfmuser = message.input_str or Config.LASTFM_USERNAME
        params = {
            "method": "user.getInfo",
            "user": lfmuser,
            "api_key": Config.LASTFM_API_KEY,
            "format": "json",
        }
        view_data = (await get_response(params))[1]
        if "error" in view_data:
            return await message.err(view_data["error"], del_in=5)
        lastuser = view_data["user"]
        if lastuser["gender"] == "m":
            gender = "🙎‍♂️ "
        elif lastuser["gender"] == "f":
            gender = "🙍‍♀️ "
        else:
            gender = "👤 "
        lastimg = lastuser["image"].pop() if len(lastuser["image"]) != 0 else None
        age = lastuser["age"]
        playlist = lastuser["playlists"]
        subscriber = lastuser["subscriber"]
        result = ""
        if lastimg:
            result += f"[\u200c]({lastimg['#text']})"
        result += f"<b>LastFM User Info for [{lfmuser}]({lastuser['url']})</b>:\n"
        result += f" {gender}<b>Name:</b> {lastuser['realname']}\n"
        if age != "0":
            result += f" 🎂 <b>Age:</b> {age}\n"
        result += f" 🎵 <b>Total Scrobbles:</b> {lastuser['playcount']}\n"
        result += f" 🌍 <b>Country:</b> {lastuser['country']}\n"
        if playlist != "0":
            result += f" ▶️ <b>Playlists:</b> {playlist}\n"
        if subscriber != "0":
            result += f" ⭐️ <b>Subscriber:</b> {subscriber}"
        await message.edit(result)

    @userge.on_cmd(
        "lastlove",
        about={
            "header": "Get Lastfm Loved Tracks",
            "usage": "{tr}lastlove [lastfm username] (optional)",
        },
    )
    async def last_fm_loved_tracks_(message: Message):
        """liked songs"""
        user_ = message.input_str or Config.LASTFM_USERNAME
        params = {
            "method": "user.getlovedtracks",
            "limit": 20,
            "page": 1,
            "user": user_,
            "api_key": Config.LASTFM_API_KEY,
            "format": "json",
        }
        view_data = (await get_response(params))[1]
        tracks = view_data["lovedtracks"]["track"]
        if "error" in view_data:
            return await message.err(view_data["error"], del_in=5)
        if len(tracks) == 0:
            return await message.edit("You Don't have any Loved tracks yet.")

        rep = f"<b>Favourite (♥️) Tracks for [{user_}](https://www.last.fm/user/{user_})</b>"
        for count, song_ in enumerate(tracks, start=1):
            song_name = song_["name"]
            artist_name = song_["artist"]["name"]
            rep += f"\n{count}. 🎧  <b>[{song_name}]({song_['url']})</b> - [{artist_name}]({song_['artist']['url']})"
        await message.edit(rep, disable_web_page_preview=True)

    @userge.on_cmd(
        "lastplayed",
        about={
            "header": "Get Upto 20 recently played LastFm Songs",
            "usage": "{tr}lastplayed [lastFM username] (optional)",
        },
    )
    async def last_fm_played_(message: Message):
        """recently played songs"""
        user_ = message.input_str or Config.LASTFM_USERNAME
        params = {
            "method": "user.getrecenttracks",
            "limit": 20,
            "extended": 1,
            "user": user_,
            "api_key": Config.LASTFM_API_KEY,
            "format": "json",
        }
        view_data = (await get_response(params))[1]
        if "error" in view_data:
            return await message.err(view_data["error"], del_in=5)
        recent_song = view_data["recenttracks"]["track"]
        if len(recent_song) == 0:
            return await message.err("No Recent Tracks found", del_in=5)
        rep = f"<b>[{user_}'s](https://www.last.fm/user/{user_})</b> recently played 🎵 songs:\n"
        for count, song_ in enumerate(recent_song, start=1):
            song_name = song_["name"]
            artist_name = song_["artist"]["name"]
            rep += f"\n{count}. 🎧  <b>[{song_name}]({song_['url']})</b> - [{artist_name}]({song_['artist']['url']})"
            if song_["loved"] != "0":
                rep += " (♥️)"
        await message.edit(rep, disable_web_page_preview=True)

    async def get_response(params: dict):
        async with aiohttp.ClientSession() as session:
            async with session.get(API, params=params) as resp:
                status_code = resp.status
                json_ = await resp.json()
            session.close()
        return status_code, json_
