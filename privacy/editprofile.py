import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu


class EditProfile(commands.Cog):
    """Deliver Profile Editing link."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="editprofile")
    async def editprofile(self, ctx):
        """Deliver Profile Editing link."""
        await ctx.send("Your furry refuge account profile editing link is: https://auth.furryrefuge.com/if/user/#/settings", delete_after=10)
