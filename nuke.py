import discord
from discord.ext import commands
from Data.database_handler import DataBaseHandler
from logs import Logs
from get_language import get_language

database_handler = DataBaseHandler("database.db")

def setup(bot):
    bot.add_cog(Nuke(bot))

class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def nuke(self, ctx):
        langue = get_language(ctx)
        try:
            await ctx.channel.delete()
            newchan = await ctx.guild.create_text_channel(category = ctx.channel.category, name = ctx.channel.name, overwrites = ctx.channel.overwrites, topic = ctx.channel.topic)
            await newchan.edit(position = ctx.channel.position)
            await newchan.send(langue.nukemsg.format(ctx.author.mention), delete_after=5)
            return await Logs.logsNuke(self, ctx, newchan)
        except:
            return await ctx.send(langue.nukeimpossible, delete_after=5)