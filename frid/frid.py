import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu


class FRIDPlugin(commands.Cog):
    """Fetch and display FR ID Card."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="id")
    async def fetch_id_card(self, ctx, username: str = None):
        """Fetches FR ID Card for a given Discord username."""
        if username is None:
            username = ctx.author.name
        lookup_url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22tgname%22%3A+%22{username}%22%7D"
        headers = {
            'accept': 'application/json',
            'authorization': 'Bearer ***REMOVED***'
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get(lookup_url, headers=headers) as lookup_response:
                if lookup_response.status == 200:
                    user_data = await lookup_response.json()
                    if user_data['results']:
                        username = user_data['results'][0]['username']
                        api_url = f"http://api.feathersfirst.local:8080/?username={username}"
                        async with session.get(api_url) as response:
                            if response.status == 200:
                                with open("/tmp/image.png", "wb") as f:
                                    while True:
                                        chunk = await response.content.read(1024)
                                        if not chunk:
                                            break
                                        f.write(chunk)
                                await ctx.send(file=discord.File("/tmp/image.png"))
                                os.remove("/tmp/image.png")
                            else:
                                await ctx.send("Failed to fetch FR ID Card. Please try again later.", delete_after=10)
                    else:
                        await ctx.send("No user found with the provided Discord username.")
                else:
                    await ctx.send("Failed to lookup user information. Please try again later.", delete_after=10)

