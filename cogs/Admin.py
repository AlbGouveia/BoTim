import discord
from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} foi kickado do servidor.')
        if reason is not None:
            await ctx.send(f'Motivo: {reason}')


def setup(client):
    client.add_cog(Admin(client))
