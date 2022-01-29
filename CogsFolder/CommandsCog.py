import discord
import requests
import os 
import psutil
from CogsFolder.cleanUp import MessageCleanUp
from discord.ext import commands
from discord.ui import View, Button
from discord.abc import Messageable


class GeneralCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    ctx = commands.Context
    channel = Messageable

    command = commands.command

    @command(name="cpu_percent", alias=["cpuusage", "cpupercent"])
    async def cpu_percent(self, ctx: ctx):
        async with MessageCleanUp(ctx):
            channel = ctx.channel 
            await channel.send(psutil.cpu_percent(), delete_after=3.0)

    @command(name='ping')
    async def ping(self, ctx: commands.Context):
        async with MessageCleanUp(ctx):
            if ctx.author.id == self.bot.user.id:
                return
            await ctx.reply(
                f"{round(self.bot.latency*1000)}ms",
                delete_after=3.0
            )  # Mention_author=False(for later use)

    @command(name='avatar')
    async def avatar(self, ctx):
        if ctx.message.mentions:
            for messageuser in ctx.message.mentions:
                await ctx.channel.send(messageuser.avatar_url)
        else:
            await ctx.reply(ctx.author.avatar_url)

    @command(name='checkmobile')
    async def checkmobile(self, ctx):
        if ctx.message.mentions:
            for messageuser in ctx.message.mentions:
                # await ctx.channel.send(f"{str(messageuser.is_on_mobile())}")
                await ctx.channel.send("Yes") if messageuser.is_on_mobile() else await ctx.channel.send("No")
        else:
            await ctx.reply(f"Please tag whom you wanna perform check on.")

    @command(name="whereishelp")
    async def whereishelp(self, ctx):
        async with ctx.typing():
            # unsplash api request
            url = "https://api.unsplash.com/photos/random"
            access_key = os.environ['Unsplash_access_key']
            parameters = {
                "client_id": access_key,
                "query": "flowers",
                "orientation": "landscape"
            }
            response_unsplash = requests.get(url=url, params=parameters).json()
            flower_url = response_unsplash["urls"]["raw"]

            # discord embed creation
            embed = discord.Embed(
                title="Help is here,but wait..",
                color=discord.Colour.dark_magenta(),
                description="Sorry! Currently we are working on help commands. \nThanks for your patience"
            )
            embed.set_image(url=flower_url)
        
        await ctx.reply(embed=embed)

    @command(name="getpic")
    async def getpic(self, ctx, term: str):
        async with ctx.typing():
            # unsplash api request
            url = "https://api.unsplash.com/photos/random"
            access_key = os.environ["Unsplash_access_key"]
            parameters = {
                "client_id": access_key,
                "query": term,
                "orientation": "landscape"
            }
            response_unsplash = requests.get(url=url, params=parameters).json()
            type_url = response_unsplash["urls"]["raw"]
            embed = discord.Embed()
            embed.set_image(url=type_url)
        await ctx.reply(embed=embed)

    @command(name="google", alias=["g"])
    async def google(self, ctx):
        button = Button(style=discord.ButtonStyle.primary, label="google", url="https://google.com")
        view = View(timeout=60)
        view.add_item(button)
        async with ctx.typing():
            await ctx.channel.send("Here We Go!", view=view)

    @command(name="print")
    async def printt(self, ctx):
        async def printhello(context):
            await context.channel.send("hello")
        button = Button(style=discord.ButtonStyle.success, label="print")
        button.callback = printhello
        view = View(button, timeout=60)
        async with ctx.typing():
            await ctx.channel.send("click click click!!!", view=view)
        
    @command(name="eb")
    async def connected(self, ctx :commands.Context):
        await ctx.channel.send("command invoked")
        embed = discord.Embed()
        embed.color=discord.Color.nitro_pink()
        embed.add_field(name="name",value="value",inline=True)
        embed.add_field(name="name2",value="value2",inline=False)
        button = Button(style=discord.ButtonStyle.success, label="embed")
        view = View(button, timeout=60*5)
        button.callback =  self.disconnected
        await ctx.channel.send(embed=embed,view=view)


    @command(name="disconnected")
    async def disconnected(self, ctx :commands.Context):
        await ctx.channel.send("disconnected")

            
def setup(bot: commands.Bot):
    bot.add_cog(GeneralCommands(bot))
