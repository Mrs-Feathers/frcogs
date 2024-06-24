from .karma import KarmaPlugin

__red_end_user_data_statement__ = "Give karma to a discord user"


async def setup(bot):
    await bot.add_cog(KarmaPlugin(bot))
