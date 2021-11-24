import discord
import datetime
from discord.ext import commands
from Data.database_handler import DataBaseHandler
from logs import Logs
from get_language import get_language


database_handler = DataBaseHandler("database.db")


def setup(bot):
    bot.add_cog(Lock(bot))

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        langue = get_language(ctx)
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages=False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(langue.lockmsg.format(ctx.author.mention))
        await Logs.logsLock(self, ctx)

    

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        langue = get_language(ctx)
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages=True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(langue.unlockmsg.format(ctx.author.mention))
        await Logs.logsUnlock(self, ctx)