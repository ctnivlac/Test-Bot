from nextcord.ext import commands
from config import IT_ROLE_ID

class Ping(commands.Cog, name="Ping pong"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog... Ready! \t| Ping")

    @commands.command()
    async def ping(ctx):
        await ctx.send("pong");

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))   