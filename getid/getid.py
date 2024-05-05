import discord
from discord.ext import commands

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
        embed.set_thumbnail(url=user.avatar_url)

        await ctx.send(embed=embed)

