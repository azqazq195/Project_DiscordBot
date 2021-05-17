import os
import random

import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=".")
status = cycle(['Status 1', 'Status 2'])


@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello there!'))
    print('Bot is ready.')


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('뭔소리여')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODQzODIzMzAzODE0ODA3NTUy.YKJdsQ.MhKAaHINP4Dr27U94I-CbGrSOaA')
