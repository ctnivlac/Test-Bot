from nextcord.ext import commands
from config import IT_ROLE_ID

class Echo(commands.Cog, name="Echo"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog... Ready! \t| Echo")

    @commands.command()
    async def echo(ctx, *,args):
            await ctx.send(args)
            await ctx.message.delete()

def setup(bot: commands.Bot):
    bot.add_cog(Echo(bot))