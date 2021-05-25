import discord
import bot
from discord.ext import commands
from datetime import datetime


class Conexao(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await bot.client.change_presence(activity=discord.Game('Tetris'))
        with open('Data/TimLog.txt', 'a') as f:
            f.write(f'\nO Bot está online. {datetime.now()}\n')
        print(f'O Bot está online.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('Data/TimLog.txt', 'a') as f:
            f.write(f'{member} entrou no servidor. {datetime.now()}\n')
        print(f'{member} entrou no servidor.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('Data/TimLog.txt', 'a') as f:
            f.write(f'{member} saiu/foi removido do servidor. {datetime.now()}\n')
        print(f'{member} saiu/foi removido do servidor.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(bot.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Conexao(client))
