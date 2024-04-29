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
    async def get_user(self, ctx, platform, username):
        """Fetch user information from different platforms."""
        if platform in ["tg", "telegram"]:
            username = f"@{username}" if not username.startswith('@') else username
            platform = "tgname"
            url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22{platform}%22%3A+%22{username}%22%7D"
        elif platform in ["disc", "discord"]:
            platform = "discname"
            url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22{platform}%22%3A+%22{username}%22%7D"
        elif platform == "fr":
            url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22tgname%22%3A+%22%40Mrs_Feathers%22%7D&username={username}"
        else:
            await ctx.send('Please specify a valid platform: "tg" for Telegram, "disc" for Discord, or "fr" for Furry Refuge.')
            return

        headers = {
            'accept': 'application/json',
            'authorization': 'Bearer '
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    user_data = await response.json()
                    user = user_data.get('results', [None])[0]
                    if user:
                        reply_message = f"User Information for {username}:\n"
                        reply_message += f"Username: {user['username']}\n"
                        reply_message += f"Name: {user['name']}\n"
                        reply_message += f"Active: {user['is_active']}\n"
                        reply_message += f"Last login: {user['last_login']}\n"
                        reply_message += f"Email: {user['email']}\n"
                        reply_message += "Attributes:\n"
                        for key, value in user['attributes'].items():
                            if not any(x in key.lower() for x in ["user", "pass", "settings"]):
                                reply_message += f"  {key}: {value}\n"
                        await ctx.send(reply_message)
                    else:
                        await ctx.send('No user found with the provided username.')
                else:
                    await ctx.send('Failed to fetch user attributes.')
