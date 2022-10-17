from nextcord import Interaction
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import guild_ids


class slashping(commands.Cog, name = "Slash Ping"):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(name="slashping", description="ping pong", guild_ids=guild_ids)
    async def slashping(self, ctx: Interaction):
        await ctx.response.send_message("Pong!")

def setup(bot: commands.Bot):
    bot.add_cog(slashping(bot))