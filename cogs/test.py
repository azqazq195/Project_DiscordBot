import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('test load.')

    # Commands
    @commands.command()
    async def test(self, ctx):
        await ctx.send('test!')


def setup(client):
    client.add_cog(Test(client))
