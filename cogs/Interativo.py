import discord
from discord.ext import commands
import random
from datetime import datetime

badWords = ['safada']

class Interativo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        respostas = ['Com certeza!', 'Claro!', 'Sim.', 'Tenho a impressão que sim...',
                     'Acho que não, talvez...', 'Não tenho certeza.', 'Não.', 'Definitivamente não!']
        await ctx.send(f'{random.choice(respostas)}')

    @commands.command(name='hello')
    async def hello_command(self, ctx):
        timeNow = datetime.now()

        if 6 <= timeNow.hour < 12:
            await ctx.send('Bom dia!')
        elif 12 <= timeNow.hour < 18:
            await ctx.send('Boa tarde!')
        elif 18 <= timeNow.hour <= 23:
            await ctx.send('Boa noite!')
        else:
            await ctx.send('Boa madrugada!')

    @commands.Cog.listener()
    async def on_message(self, event):
        if event.author.bot:
            return

        event.content = event.content.lower()
        if event.content.startswith('oi'):
            await event.channel.send(f'Oi, {event.author.name}!')
        elif event.content.startswith('bom dia'):
            await event.channel.send(f'Bom dia, {event.author.name}!')
        elif event.content.startswith('boa tarde'):
            await event.channel.send(f'Boa tarde, {event.author.name}!')
        elif event.content.startswith('boa noite'):
            await event.channel.send(f'Boa noite, {event.author.name}!')

    @commands.Cog.listener()
    async def on_message(self, event):
        if event.author.bot:
            return

        event.content = event.content.lower()
        for palavra in event.content.split():
            if palavra in badWords:
                await event.delete()


def setup(client):
    client.add_cog(Interativo(client))
