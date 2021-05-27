import discord
from discord.ext import commands
import random
from datetime import datetime


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
    async def on_message(self, message):
        if message.author.bot:
            return

        message.content = message.content.lower()
        if message.content.startswith('oi'):
            await message.channel.send(f'Oi, {message.author.name}!')
            print('Cumprimentos correspondidos!')
        elif message.content.startswith('bom dia'):
            await message.channel.send(f'Bom dia, {message.author.name}!')
            print('Cumprimentos correspondidos!')
        elif message.content.startswith('boa tarde'):
            await message.channel.send(f'Boa tarde, {message.author.name}!')
            print('Cumprimentos correspondidos!')
        elif message.content.startswith('boa noite'):
            await message.channel.send(f'Boa noite, {message.author.name}!')
            print('Cumprimentos correspondidos!')

    @commands.command(name='dol')
    async def dol_command(self, ctx):
        await ctx.send('Doc resumido sobre as avaliações de Comunicação e Expressão:\nhttps://docs.google.com/document/d/1yDeqix34_w6ZMXvJoLQCgRxRJn3zJbpwpIGXrS6kIQs/edit?usp=sharing')

    @commands.command(name='institucional')
    async def av_institucional_command(self, ctx):
        await ctx.send('Link para a Avaliação Institucional (encerramento dia 31/05):\nhttps://aluno.uninassau.edu.br/AvInstitucional/Login.aspx')

    @commands.command(name='datas')
    async def datas_command(self, ctx):
        await ctx.send('''Datas importantes:\n30/05 - Prazo de entrega da atividade 07 de Sistemas
31/05 - Encerramento da Avaliação Institucional
08/06 - Av2 de Lógica Matemática e Comunicação e Expressão
16 e 25/06 - 2CH e AF de Comunicação e Expressão''')

    @commands.command(name='pibic')
    async def pibic_command(self, ctx):
        await ctx.send('Doc sobre o PIBIC (Programa de Iniciação Científica):\nhttps://docs.google.com/document/d/1FK1TvzDGkwla4ylMcIJKR-6FYJoJSYQUU_T0-pDHht0/edit?usp=sharing')


def setup(client):
    client.add_cog(Interativo(client))
