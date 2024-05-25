import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu

class GiveXP(commands.Cog):
    """Give XP to a user based on Discord username"""

    def __init__(self, bot) -> None:
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(token=None)

    @commands.command(name="givexpsettoken")
    @commands.is_owner()
    async def set_token(self, ctx, token: str):
        """Set the API token for fetching user data."""
        await self.config.token.set(token)
        await ctx.send("Token set successfully.")

    @commands.command(name="givexp")
    @commands.is_owner()
    async def give_xp(self, ctx, amount: int, user: discord.User = None):
        """Give XP to a user."""
        if user is None:
            await ctx.send("You must specify a user.")
            return

        token = await self.config.token()
        if not token:
            await ctx.send("API token is not set. Use givexpsettoken command to set the API token.")
            return
        headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {token}'
        }
        url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22discname%22%3A+%22{user.name}%22%7D"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()

                    if data['results']:
                        user_data = data['results'][0]
                        user_attributes = user_data['attributes']
                        current_xp = int(user_attributes['xp']) if 'xp' in user_attributes else 0
                        new_xp = current_xp + amount
                        user_attributes['xp'] = str(new_xp)
                        update_url = f"https://auth.furryrefuge.com/api/v3/core/users/{user_data['pk']}/"
                        async with session.patch(update_url, json={'attributes': user_attributes}, headers=headers) as update_response:
                            if update_response.status == 200:
                                await ctx.send(f"XP updated successfully for {user.name}. New XP: {new_xp}")
                            else:
                                await ctx.send(f"Failed to update user data: {update_response.status} {update_response.reason}")
                    else:
                        await ctx.send("No user found with the provided username.")
                else:
                    await ctx.send(f"Failed to fetch user data: {response.status} {response.reason}")