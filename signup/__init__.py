from .infocommands import FRInfo

__red_end_user_data_statement__ = "This cog gives informational commands to help with the FR community!"


async def setup(bot):
    await bot.add_cog(FRInfo(bot))
