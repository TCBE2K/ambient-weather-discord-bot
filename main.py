import discord
from discord import app_commands
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
AMBIENT_WEATHER_API_KEY = os.getenv("AMBIENT_WEATHER_API_KEY")
AMBIENT_WEATHER_APP_KEY = os.getenv("AMBIENT_WEATHER_APP_KEY")
AMBIENT_WEATHER_MAC_ADDRESS = os.getenv("AMBIENT_WEATHER_MAC_ADDRESS")


def get_temp():
    # Make the HTTP request
    response = requests.get(f'https://rt.ambientweather.net/v1/devices/{AMBIENT_WEATHER_MAC_ADDRESS}?apiKey={AMBIENT_WEATHER_API_KEY}&applicationKey={AMBIENT_WEATHER_APP_KEY}&limit=1')

    # Parse the JSON response
    data = response.json()

    # Access the temperature value
    temperature_fahrenheit = data[0]['tempf']
    return temperature_fahrenheit

def get_feels_like():
    # Make the HTTP request
    response = requests.get(f'https://rt.ambientweather.net/v1/devices/{AMBIENT_WEATHER_MAC_ADDRESS}?apiKey={AMBIENT_WEATHER_API_KEY}&applicationKey={AMBIENT_WEATHER_APP_KEY}&limit=1')
    # Parse the JSON response
    data = response.json()

    # Access the temperature value
    feels_like = data[0]['feelsLike']
    return feels_like

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    # Print when the bot is ready
    print("Bot is Up and Ready!")
    try:
        pass
        # Print how many commands are active
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)!")
    except Exception as e:
        print(e)

@bot.hybrid_command(name="temp", description="Outputs the temperature")
async def temp(ctx: commands.Context):
    # Call "get_temp"
    await ctx.send(get_temp(), ephemeral=True)

@bot.hybrid_command(name="feels_like", description="Outputs what it feels like outside")
async def temp(ctx: commands.Context):    
    # Call "get_feels_like"
    await ctx.send(get_feels_like(), ephemeral=True)




bot.run(DISCORD_TOKEN)
