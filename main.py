import discord
from discord import app_commands
from discord.ext import commands


client = commands.Bot(command_prefix="e!", intents=discord.Intents().all())

sync = await client.tree.sync()
@client.event
async def on_ready():
  
  print("Bot online")
  print("Comandi slash:" + sync)
@client.tree.command(description="Test")
async def test(i: discord.Interaction):
  try:
    await i.response.send_message("Sono vivo! I miei comandi slash sono: " + sync)
  except Exception as e:
    await i.response.send_message("Errore")
    raise e

