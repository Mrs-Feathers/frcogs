from .achievements import Achievements

__red_end_user_data_statement__ = "This cog allows you to request your FR ID card using information from your Furry Refuge account!"


async def setup(bot):
    await bot.add_cog(Achievements(bot))
