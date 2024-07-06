from .events import EventLink

__red_end_user_data_statement__ = "Check out our events!"


async def setup(bot):
    await bot.add_cog(EventLink(bot))
