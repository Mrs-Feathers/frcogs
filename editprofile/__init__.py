from .signup import FRSignup

__red_end_user_data_statement__ = "This cog allows you to request an invitation to make a Furry Refuge account!"


async def setup(bot):
    await bot.add_cog(FRSignup(bot))
