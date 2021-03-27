import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '+', description = '')


@bot.event
async def on_ready():
	print('Pret !')

@bot.event
async def on_message(message):
	#print("Message dans :", message.channel)
	await message.add_reaction("✅")
	await message.add_reaction("❌")

		
bot.run('')
