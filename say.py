import discord
from discord.ext import commands
from get_language import get_language


def setup(bot):
    bot.add_cog(Say(bot))

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def say(self, ctx, *, msg):
        langage = get_language(ctx)
        await ctx.message.delete()
        await ctx.send(langage.saymsg.format(ctx.author.mention, msg))