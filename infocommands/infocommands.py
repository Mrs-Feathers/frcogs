import discord
from discord.ext import commands
import aiohttp
import os

from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_number
from redbot.core.utils.views import SimpleMenu


class FRInfo(commands.Cog):
    """Deliver Informations."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="signup")
    async def signup(self, ctx):
        """Get invite link to sign up for an FR account."""
        await ctx.send("Your Furry Refuge account invite link is: https://auth.furryrefuge.com/if/flow/enrollment-invitation/?itoken=8c5d1f9d-1fbc-40b9-9bed-a6b5c42d137c")

    @commands.command(name="support")
    async def support(self, ctx):
        """Need support? Contact us!"""
        await ctx.send("!!!Support is always here to help, send an email to support@furryrefuge.com including everything you think is relivant and we will try to help!")

    @commands.command(name="privacy")
    async def privacy(self, ctx):
        """Deliver link to privacy policy."""
        await ctx.send("Furry Refuge Privacy Policy: https://furryrefuge.com/privacy-policy")

    @commands.command(name="events")
    async def events(self, ctx):
        """Check out a link to our Events Calendar!"""
        await ctx.send("Check out FR Events at: https://furryrefuge.com/events")

    @commands.command(name="editprofile")
    async def editprofile(self, ctx):
        """Profile Editing link on FR website."""
        await ctx.send("Your furry refuge account profile editing link is: https://auth.furryrefuge.com/if/user/#/settings", delete_after=60)

    @commands.command(name="donate")
    async def editprofile(self, ctx):
        """Link to our Patreon."""
        await ctx.send("Our patreon link is https://patreon.com/FurryRefuge Help keep our community running!")
