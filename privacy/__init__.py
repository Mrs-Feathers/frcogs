from .privacy import PrivacyPolicy

__red_end_user_data_statement__ = "Deliver link to privacy policy."


async def setup(bot):
    await bot.add_cog(PrivacyPolicy(bot))
