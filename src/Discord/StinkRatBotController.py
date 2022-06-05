import os
import sys

import discord
from dotenv import load_dotenv, find_dotenv

bot = discord.Client()
path = sys.path[2] + '/StinkRat/config/.env'
load_dotenv(find_dotenv(path))
stink_rat_bot_key = os.getenv('STINK_RAT_BOT_KEY')


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("hey dirtbag")


bot.run(os.getenv('STINK_RAT_BOT_KEY'))
