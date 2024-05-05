from .getid import UserInfoPlugin

__red_end_user_data_statement__ = "Test to get debug info from user"


async def setup(bot):
    await bot.add_cog(UserInfoPlugin(bot))
