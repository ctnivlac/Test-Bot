from nextcord import Interaction
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import guild_ids


class slashping(commands.Cog, name = "Slash Ping"):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(name="roledata", description="prints stuff to terminal", guild_ids=guild_ids)
    async def slashping(self, ctx: Interaction, member: nextcord.Member):
        guild = member.guild
        roleArr = []
        committeeArr = []
        for role in guild.roles:
            roleArr.append(role.id)
            subArr = []
            for person in role.members:
                subArr.append(person.id)
            committeeArr.append(subArr)
        print(roleArr)
        print(committeeArr)
        await ctx.response.send_message("Hello")
        
        


def setup(bot: commands.Bot):
    bot.add_cog(slashping(bot))