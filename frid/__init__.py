from .frid import FRIDPlugin

__red_end_user_data_statement__ = "This cog allows you to generate your FR ID card using information from your Furry Refuge account!"


async def setup(bot):
    await bot.add_cog(FRIDPlugin(bot))
