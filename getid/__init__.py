from .getid import get_user_info

__red_end_user_data_statement__ = "Test to get debug info from user"


async def setup(bot):
    await bot.add_cog(get_user_info(bot))
