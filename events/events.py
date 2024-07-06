import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu


class EventLink(commands.Cog):
    """Deliver Events Calendar link."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="events")
    async def events(self, ctx):
        """Deliver Events Calendar link."""
        await ctx.send("Check out FR Events at: https://furryrefuge.com/events")
