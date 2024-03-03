import discord
import asyncio
from discord.ext import commands
from datetime import datetime, timedelta
from os import getenv
from dotenv import load_dotenv
import logging

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

load_dotenv()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel_id = getenv("CHANNEL_ID")

    # Attempt to convert channel_id to integer
    try:
        channel_id = int(channel_id)
    except ValueError:
        print("Error: channel_id is not a valid integer.")
        return

    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Hello! Bot is ready!")
    else:
        print(f"Error: Could not find the channel with ID {channel_id}")
    await schedule_pings(channel)


async def schedule_pings(channel):
    while True:
        # Calculate the time until the next scheduled ping (8:53 pm or the next multiple of 3 hours)
        now = datetime.now()
        next_ping_time = datetime(now.year, now.month, now.day, hour=11, minute=52)
        print(next_ping_time)

        while now >= next_ping_time:
            next_ping_time += timedelta(hours=3)
            print(next_ping_time)

        time_until_ping = next_ping_time - now
        print(time_until_ping)

        # Sleep until the next scheduled ping
        await asyncio.sleep(time_until_ping.total_seconds())

        # Get the channel where you want to send the ping

        await channel.send("<@&1213641465419530371> characters Time for a 3-hourly ping!")


# Run the bot with your token
bot.run(getenv("BOT_TOKEN"))
