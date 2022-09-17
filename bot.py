import nextcord
import os
from nextcord.ext import commands

def main():
   
    intents = nextcord.Intents.default()
    intents.message_content = True
    
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print("The bot is ready to go!")

    @bot.commands
    async def ping(ctx):
        await ctx.send("pong")

    bot.run('MTAyMDQ0NTg1MjY1NDg5OTMwMQ.GPPiCY.PkwzyGjp6lbjN5JZNvOKwfBPDP4zZFmyZLLmdY')

if __name__ == '__main__':
    main()
 