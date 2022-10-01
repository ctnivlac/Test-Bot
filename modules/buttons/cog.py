from nextcord.ext import commands 
from .role_view import RoleView
from config import IT_ROLE_ID

class Buttons(commands.Cog, name= "Button Roles"):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RoleView())
        print ("Buttons roles are ready")

    @commands.command()
    @commands.has_role(IT_ROLE_ID)
    async def buttons(self, ctx: commands.Context):
        await ctx.send("Click a button", view=RoleView())

def setup(bot: commands.Bot):
    bot.add_cog(Buttons(bot))
