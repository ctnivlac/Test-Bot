from nextcord.ext import commands
from config import *

class echo(commands.Cog, name="Echo"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog... Ready! \t| Echo")

    @commands.command()
    @commands.has_role(IT_ROLE_ID)
    async def echo(self, ctx: commands.Context, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(echo(bot))