import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu

class UserInfoPlugin(commands.Cog):
    """Plugin to fetch and display Discord user information."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="getid")
    async def get_user_info(self, ctx, *, user: discord.User = None):
        """Fetches information about a Discord user."""
        if user is None:
            user = ctx.author  # Default to the user who invoked the command if no user is specified

        embed = discord.Embed(title="User Information", color=discord.Color.blue())
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="Username", value=user.display_name, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        embed.add_field(name="Bot?", value=user.bot, inline=True)

        await ctx.send(embed=embed)
        await ctx.send(f"Command invoked by: {ctx.author}")
        await ctx.send(f"User argument given: {user} test: {user.name}")
