import discord
import os 

from discord.ext import commands


from functions.get_token import get_token
from functions.guild_functions import guild_update_config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True


bot = commands.Bot(command_prefix ='!', intents=intents)

@bot.event
async def on_ready():
    guild_update_config()

    for file in os.listdir("./cogs"):
        if (file.endswith(".py")):
            extention = f"cogs.{file[:-3]}"
            try:
                print(f"Loaded {extention}")
                await bot.load_extension(extention)
            except:
                print(f"An error occurred while loading {extention} ")



bot = bot.run(get_token())