import asyncpraw
from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
import os 
from random import shuffle
import time

# env variables 
load_dotenv() 
reddit_client_id = os.environ["reddit_client_id"]
reddit_client_secret = os.environ["reddit_client_secret"]
reddit_user_agent = os.environ["reddit_user_agent"]
# Cogs
class Redditcommands(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    # self.bot.command_prefix=commands.when_mentioned_or(";")

  @commands.command(name="meme")
  async def meme(self,ctx,num_of_memes:int=1):
    # reddit instance
    reddit = asyncpraw.Reddit(
      client_id=reddit_client_id,
      client_secret=reddit_client_secret,
      user_agent="something:justlikethis1234"
    )

    
    memes=[]
    subreddit = await reddit.subreddit("memes")
    async for submission in subreddit.rising(limit=100):
      memes.append(submission)
            
    shuffle(memes)

    for i in range(num_of_memes):
      submission = memes[i]
                
      name = str(submission.title)
      url = submission.url
      upvotes = submission.score
                
      embed = Embed(title=name)
      embed.set_image(url=url)
      embed.set_footer(text=f'👍 {upvotes}')

      await ctx.send(embed=embed)
      time.sleep(3)  

  @commands.command(name="memetag")
  async def memetag(self,ctx,subreddit_topic :str):

    await ctx.channel.send(f'Subreddit topic changed to "{subreddit_topic}"')
        
def setup(bot:commands.Bot):
  bot.add_cog(Redditcommands(bot))


