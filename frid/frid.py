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
    async def fetch_id_card(self, ctx, username: str):
        """Fetches FR ID Card for a given username."""
        api_url = f"https://api.feathersfirst.local:8080/?username={username}"
        async with aiohttp.ClientSession() as session:
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

