import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_member_join(member):
    print(f'{member} has entered the server! {member} is incredibly smelly!')


bot.run('NzUzNDc3MzAwNjU3MzI0MTAy.X1mwaw.vyeOsqtVs3ffMbXFJBzN-eQ0X7E')