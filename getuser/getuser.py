import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu


class GetUser(commands.Cog):
    """Get a users information from FR API"""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="getuser")
    async def signup(self, ctx):
        """Deliver Invite link."""
        await ctx.send("Your furry refuge account invite link is: https://auth.furryrefuge.com/if/flow/enrollment-invitation/?itoken=62bd2e38-b67b-46d2-9118-7636d54d48c6", delete_after=10)
