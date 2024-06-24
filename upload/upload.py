import discord
from discord.ext import commands
import aiohttp
import os
import base64

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu

class Upload(commands.Cog):
    """Upload files using a user's Discord username as a token"""

    def __init__(self, bot) -> None:
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(token=None)

    @commands.command(name="upload")
    async def upload(self, ctx):
        """Upload using the user's username as a token."""
        if not isinstance(ctx.channel, discord.TextChannel):
            username = ctx.author.name
            token = base64.b64encode(username.encode()).decode()
            url = f"https://photovoter.furryrefuge.com/upload.php?token={token}"
            await ctx.send(f"DO NOT SHARE THIS LINK! This is your token: {url}")
        else:
            await ctx.send("The !upload command can only be used in private messages with me!")
