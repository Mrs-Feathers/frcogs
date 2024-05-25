from .chatxp import ChatXP

__red_end_user_data_statement__ = "This cog allows you earn xp!"


async def setup(bot):
    await bot.add_cog(ChatXP(bot))
