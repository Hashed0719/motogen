import os
import dotenv
from discord import __version__
from discord.ext import commands
from discord.flags import Intents
import logging 
from alive import countrun,keep_alive
import sys
# import discord
# from discord.client import Client
# from dotenv import load_dotenv


# logging system 
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='motogen.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#enviorenment variables
dotenv.load_dotenv()
token = os.environ['token']

# bot initiate and Intents
intents = Intents.default()
intents.members=True
intents.presences=True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),intents=intents)


# bot events
@bot.event
async def on_ready():
    bot_channel = bot.get_channel(id=931029261203152956)
    await bot_channel.send('alive!!!!')
    sys.stdout.write(f'connected as {bot.user}\n')
    
    countrun("countrun.txt")

    # importing cogs (def setup is needed as global function to import through bot.loadextension())
    bot.load_extension("CogsFolder.CommandsCog")
    bot.load_extension("CogsFolder.RedditCommandCog")   
    bot.load_extension("CogsFolder.MusicCog")
    # bot.load_extension("CogsFolder.MusicCog")





keep_alive()

# version
sys.stdout.write(__version__+"\n")
# run 
bot.run(token) 

