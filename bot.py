import nextcord
import os
from dotenv import load_dotenv
from nextcord.ext import commands
from config import *

def main():
    intents = nextcord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    load_dotenv()
    
    @bot.event
    async def on_ready():
        print("Rocketry Bot is Online")

    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            bot.load_extension(f"modules.{folder}.cog")

    bot.run("MTAwNTU3MTI1NDM4MTcxMTM2MA.GtKY8F.JTg4cABk6tO6TRz9x2fCp8C434ER6N144OAdos")

if __name__ == '__main__':
    main()