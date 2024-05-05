import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu

# Set up a simple in-memory "database" for rate limits
rate_limits = {}

# Custom rate limit function
def check_rate_limit(user_id, ctx):
    current_time = discord.utils.utcnow().timestamp()
    limit_duration = 3600  # 1 hour in seconds
    limit_count = 3

    if user_id not in rate_limits:
        rate_limits[user_id] = []

    # Filter out expired timestamps
    rate_limits[user_id] = [timestamp for timestamp in rate_limits[user_id] if current_time - timestamp < limit_duration]

    if len(rate_limits[user_id]) >= limit_count:
        ctx.send("You can only give karma 3 times per hour.")
        return False
    else:
        # Add current timestamp to the record
        rate_limits[user_id].append(current_time)
        return True

class KarmaPlugin(commands.Cog):
    """Plugin to manage karma points."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "+1" and message.reference:
            ctx = await self.bot.get_context(message)
            target_message = await message.channel.fetch_message(message.reference.message_id)
            target_user = target_message.author
            giver_user = message.author

            if target_user.id == giver_user.id:
                await ctx.send("You cannot give karma to yourself.")
                return

            # Apply rate limiting
            if check_rate_limit(giver_user.id, ctx):
                lookup_url = f"https://auth.furryrefuge.com/api/v3/core/users/?attributes=%7B%22discname%22%3A+%22{target_user.name}%22%7D"
                headers = {
                    'accept': 'application/json',
                    'authorization': 'Bearer ***REMOVED***'
                }

                async with aiohttp.ClientSession() as session:
                    async with session.get(lookup_url, headers=headers) as lookup_response:
                        if lookup_response.status == 200:
                            user_data = await lookup_response.json()
                            if user_data['results']:
                                user = user_data['results'][0]
                                user_attributes = user['attributes']
                                current_karma = int(user_attributes.get('karma', 0))
                                new_karma = current_karma + 1
                                user_attributes['karma'] = str(new_karma)

                                update_url = f"https://auth.furryrefuge.com/api/v3/core/users/{user['pk']}/"
                                async with session.patch(update_url, json={'attributes': user_attributes}, headers=headers) as update_response:
                                    if update_response.status == 200:
                                        await ctx.send(f"Karma given! {target_user.display_name} has now {new_karma} karma points.")
                                    else:
                                        await ctx.send("Failed to update karma. Please try again later.", delete_after=10)
                            else:
                                await ctx.send("It seems like the target user's Furry Refuge account is not linked. Please check and try again.")
                        else:
                            await ctx.send("Failed to lookup user information. Please try again later.", delete_after=10)

