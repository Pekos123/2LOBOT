# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import webserver
import discord
from discord.ext.commands import Bot, has_permissions, CheckFailure


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = Bot("$")

TOKEN = os.environ["TOKEN"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def clear(ctx, channel_id, number_of_messages: int):
    channel = bot.get_channel(int(channel_id))
    if channel is None:
        await ctx.send('Nie ma takiego kanału stupid...')
        return
    async for message in channel.history(limit=number_of_messages):
        await message.delete()

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, CheckFailure):
        msg = "haha {} nie masz admina ;)".format(ctx.message.author.mention)  
        await ctx.send(msg)

webserver.keep_alive()

client.run(TOKEN)
