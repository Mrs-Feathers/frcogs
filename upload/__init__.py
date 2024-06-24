from .upload import Upload

__red_end_user_data_statement__ = "Get a link to upload a photo"


async def setup(bot):
    await bot.add_cog(Upload(bot))
