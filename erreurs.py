import discord
from discord.ext import commands
import asyncio
from Data.database_handler import DataBaseHandler
from get_language import get_language

database_handler = DataBaseHandler("database.db")

def setup(bot):
    bot.add_cog(Erreurs(bot))

class Erreurs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        langue = get_language(ctx)
        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(langue.errorcmddoesntexist)

        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(langue.errormissingarguments)
            
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(langue.errornopermission)
            
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send(langue.errorcantuse)
            
        if isinstance(error, discord.Forbidden):
            return await ctx.send(langue.errorbotdoesnthavepermissions)
            
        if isinstance(error, commands.BadArgument):
            return await ctx.send(langue.errorbadargument)
        # else:
        #     return await ctx.send("Error. Please contact the support")