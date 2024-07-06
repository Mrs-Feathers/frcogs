import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu


class PrivacyPolicy(commands.Cog):
    """Deliver link to privacy policy."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="privacy")
    async def privacy(self, ctx):
        """Deliver link to privacy policy."""
        await ctx.send("Furry Refuge Privacy Policy: https://furryrefuge.com/privacy-policy", delete_after=10)
