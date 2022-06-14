import os
from dotenv import load_dotenv
import discord

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="ctof", help="Converts Celsius to Fahrenheit")
async def CtoF(ctx, celsius):
    F = round(((float(celsius) * 1.8) + 32), 2)
    response = f'{celsius} C is equal to {F} F'
    await ctx.send(response)

@bot.command(name="ftoc", help="Converts Fahrenheit to Celsius")
async def FtoC(ctx, fahrenheit):
    C = round(((float(fahrenheit) - 32) / 1.8), 2)
    response = f'{fahrenheit} F is equal to {C} C'
    await ctx.send(response)

@bot.command(name="mtokm", help="Converts Miles to Kilometers")
async def MtoKM(ctx, miles):
    KM = round((float(miles)*1.609344),2)
    response = f'{miles} miles is equal to {KM} kilometers'
    await ctx.send(response)

@bot.command(name="kmtom", help="Converts Kilometers to Miles")
async def KMtoM(ctx, kilometers):
    M = round((float(kilometers)*0.621371),2)
    response = f'{kilometers} kilometers is equal to {M} miles'
    await ctx.send(response)

bot.run(TOKEN)