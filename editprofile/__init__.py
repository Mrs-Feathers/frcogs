from .editprofile import EditProfile

__red_end_user_data_statement__ = "This cog allows you to request an link to edit your Furry Refuge account profile!"


async def setup(bot):
    await bot.add_cog(EditProfile(bot))
