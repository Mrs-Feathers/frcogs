import discord
from discord.ext import commands
import aiohttp
import os
import time

from redbot.core import commands, Config

class ChatXP(commands.Cog):
    """Give XP to a user based on Discord username"""

    def __init__(self, bot) -> None:
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(token=None, last_post_time={})

    @commands.command(name="chatxpsettoken")
    @commands.is_owner()
    async def set_token(self, ctx, token: str):
        """Set the API token for fetching user data."""
        await self.config.token.set(token)
        await ctx.send("Token set successfully.")

    @commands.Cog.listener()
    async def on_message(self, message):
        """Give XP to a user."""
        if not message.author.bot and isinstance(message.channel, discord.TextChannel):
            username = message.author.name
            last_post_time = await self.config.last_post_time()
            current_time = time.time()

            if not last_post_time.get(username) or current_time - last_post_time[username] >= 3600: # 3600 seconds = 1 hour
                token = await self.config.token()
                if not token:
                    return
                headers = {
                    'accept': 'application/json',
                    'authorization': f'Bearer {token}'
                }
                url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22discname%22%3A+%22{username}%22%7D"

                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        if response.status == 200:
                            data = await response.json()

                            if data['results']:
                                user_data = data['results'][0]
                                user_attributes = user_data['attributes']
                                current_xp = int(user_attributes['xp']) if 'xp' in user_attributes else 0
                                new_xp = current_xp + 1
                                user_attributes['xp'] = str(new_xp)
                                update_url = f"https://auth.furryrefuge.com/api/v3/core/users/{user_data['pk']}/"
                                async with session.patch(update_url, json={'attributes': user_attributes}, headers=headers) as update_response:
                                    if update_response.status == 200:
                                        last_post_time[username] = current_time
                                        await self.config.last_post_time.set(last_post_time)
                                        await message.channel.send(f"DEBUG: {username} has gained 1 XP! They now have {new_xp} XP.")
                                    else:
                                        print(f"Failed to update user data: {update_response.status} {update_response.reason}")
                            else:
                                print("No user found with the provided username.")
                        else:
                            print(f"Failed to fetch user data: {response.status} {response.reason}")
