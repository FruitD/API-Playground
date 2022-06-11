import os
import sys

import discord
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands

intents = discord.Intents.default()
#intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

path = sys.path[2] + '/StinkRat/config/.env'
load_dotenv(find_dotenv(path))
stink_rat_bot_key = os.getenv('STINK_RAT_BOT_KEY')


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    print("StinkRatBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("hey dirtbag")


bot.run(stink_rat_bot_key)
