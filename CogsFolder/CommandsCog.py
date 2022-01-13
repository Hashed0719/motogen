from discord.ext import commands
import discord
import requests
import os 

class GeneralCommands(commands.Cog):
    def __init__(self,bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self,ctx: commands.Context):
        if ctx.author.id == self.bot.user.id:
            return

        await ctx.reply(f"{round(self.bot.latency*1000)}ms",delete_after=3.0) #mention_author=False(for later use)

        await ctx.message.delete(delay=4.0)

    # @commands.command(name="d")
    # async def d(self,ctx,minutess):
    #   for x in minutess:
    #     if type(x) == int or float:
    #       await ctx.message.delete(x*60)
          


    @commands.command(name='avatar')
    async def avatar(self,ctx):
        if ctx.message.mentions:
            for messageuser in ctx.message.mentions:
                await ctx.channel.send(messageuser.avatar_url)
        else:
            await ctx.reply(ctx.author.avatar_url)

    @commands.command(name='checkmobile')
    async def checkmobile(self,ctx):
        if ctx.message.mentions:
            for messageuser in ctx.message.mentions:
                # await ctx.channel.send(f"{str(messageuser.is_on_mobile())}")
                await ctx.channel.send("Yes") if messageuser.is_on_mobile() else await ctx.channel.send("No")
        else:
            await ctx.reply(f"Please tag whom you wanna perform check on.")

    @commands.command(name="whereishelp")
    async def whereishelp(self,ctx):
        async with ctx.typing():
            # unsplash api request
            url="https://api.unsplash.com/photos/random"
            access_key = os.environ['Unsplash_access_key']
            parameters={
                "client_id":access_key,
                "query":"flowers",
                "orientation":"landscape"
            }
            response_unsplash=requests.get(url=url,params=parameters).json()
            flower_url=response_unsplash["urls"]["raw"]

            # discord embed creation
            embed = discord.Embed(title="Help is here,but wait..",color=discord.Colour.dark_magenta(),description="Sorry! Currently we are working on help commands. \nThanks for your patience")
            embed.set_image(url=flower_url)
        
        await ctx.reply(embed=embed)

    @commands.command(name="getpic")
    async def getpic(self,ctx,term :str):
        async with ctx.typing():
             # unsplash api request
            url="https://api.unsplash.com/photos/random"
            access_key=os.environ["Unsplash_access_key"]
            parameters={
                "client_id":access_key,
                "query":term,
                "orientation":"landscape"
            }
            response_unsplash=requests.get(url=url,params=parameters).json()
            type_url=response_unsplash["urls"]["raw"]
            embed=discord.Embed()
            embed.set_image(url=type_url)
        await ctx.reply(embed=embed)

       
       
       

        
def setup(bot: commands.Bot):
    bot.add_cog(GeneralCommands(bot)) 
    



    