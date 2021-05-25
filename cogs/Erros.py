import discord
from discord.ext import commands
from discord.ext.commands import errors


class Erros(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, errors.MissingPermissions):
            await ctx.send('Parece que você não tem permissão para fazer isso.')
        if isinstance(error, errors.CommandNotFound):
            await ctx.send('Não me lembro desse comando, você digitou certo?')
        if isinstance(error, errors.MissingRequiredArgument):
            await ctx.send('Ei, eu preciso que você me dê todos os argumentos!')


def setup(client):
    client.add_cog(Erros(client))