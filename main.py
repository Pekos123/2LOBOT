# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import webserver
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('$testcommand'):
    await message.channel.send('TEST COMMAND TYPED')



webserver.keep_alive()

client.run(TOKEN)
