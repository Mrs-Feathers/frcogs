from .chatxp import GiveXP

__red_end_user_data_statement__ = "This cog allows you earn xp!"


async def setup(bot):
    await bot.add_cog(GiveXP(bot))
