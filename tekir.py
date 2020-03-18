#Tekir By Haso
import discord
import asyncio
import logging
import random
from discord.ext.commands import Bot
from discord.ext import commands

BOT_PREFIX = "hkd!"
TOKEN = "NjgzNTk4MzU4MDY1MTg0NzY4.XnH7DQ.TtiJsnygccoZW3QZ_3tsujsnL7I"
client = Bot (command_prefix=BOT_PREFIX)

print (discord.__version__)

@client.event
async def on_ready():
    print ("Hazırım!!!")
    print ("Başlıyorum!!! " + client.user.name)
    print ("ID: " + client.user.id) 
    await client.change_presence(game=discord.Game(name='hkd!'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hkd!okkes'):
        await client.send_message(message.author, 'https://i.hizliresim.com/k01jqv.gif')
client.run(TOKEN) 
