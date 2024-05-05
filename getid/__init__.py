from .givexp import GiveXP

__red_end_user_data_statement__ = "Give xp to a discord user"


async def setup(bot):
    await bot.add_cog(GiveXP(bot))
