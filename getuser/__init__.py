from .getuser import GetUser

__red_end_user_data_statement__ = "allows admin to get more info on a user"


async def setup(bot):
    await bot.add_cog(GetUser(bot))
