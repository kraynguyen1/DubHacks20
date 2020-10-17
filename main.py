import os
import discord
from discord.ext import commands
from discord.utils import get

CLIENT = commands.Bot(command_prefix='/')
TOKEN = 'NzY3MTIzNzY1Mjg3OTc2OTgw.X4tVrg.76zyxJjTYwMAmeVnYLJxzGKGbq0'


# When you type /ping
# the bot will say "pong!"
@CLIENT.command()
async def ping(ctx):
    await ctx.send("pong!")


# When you type /hello
# the bot will say "hello!"
@CLIENT.command()
async def hello(ctx):
    await ctx.send("hello!")


# This method only runs once in the beginning
@CLIENT.event
async def on_ready():
    print("Discord Bot Activated")

# This is testing by Jong



CLIENT.run(TOKEN)
