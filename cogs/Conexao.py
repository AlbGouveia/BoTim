import discord
import bot
from discord.ext import commands


class Conexao(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await bot.client.change_presence(activity=discord.Game('Tetris'))
        print('O Bot está online.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(bot.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Conexao(client))
