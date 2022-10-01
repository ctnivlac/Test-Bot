from nextcord.ext import commands

class Ping(commands.Cog, name="Ping pong"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog... Ready! \t| Ping")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong")
 
def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))   