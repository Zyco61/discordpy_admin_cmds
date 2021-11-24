import discord
from discord.ext import commands
from get_language import get_language

def setup(bot):
    bot.add_cog(Clear(bot))

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, nombre):
        langue = get_language(ctx)
        await ctx.message.delete()
        if nombre.isdigit():
            nombre = int(nombre)
            if nombre > 100:
                return await ctx.send(langue.clearmax)
            await ctx.channel.purge(limit = nombre)
        else:
            return await ctx.send(langue.clearinvalidformat)