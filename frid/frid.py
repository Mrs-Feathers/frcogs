import discord
from discord.ext import commands
import aiohttp
import os

class FRIDPlugin(commands.Cog):
    """Fetch and display FR ID Card."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(name="id")
    async def fetch_id_card(self, ctx: discord.ApplicationContext, username: str):
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
                    await ctx.respond(file=discord.File("/tmp/image.png"))
                    os.remove("/tmp/image.png")
                else:
                    await ctx.respond("Failed to fetch FR ID Card. Please try again later.", ephemeral=True)

