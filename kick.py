import discord
from discord.ext import commands
from logs import Logs
import re
from Data.database_handler import DataBaseHandler
from get_language import get_language

database_handler = DataBaseHandler("database.db")

member_re = re.compile(r"[\D]")

def setup(bot):
    bot.add_cog(Kick(bot))

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user, *, reason = "Aucune raison"):
        langue = get_language(ctx)
        user = await self.is_discord_member(user, ctx.guild)
        if not user.bot:
            if user == ctx.author:
                return await ctx.send(langue.kickme)

            if not reason:
                reason = langue.reason
            
            if ctx.author.top_role > user.top_role or ctx.author.id == ctx.guild.owner.id:
                try:
                    embed = discord.Embed(title = langue.kicktitle, description = langue.kickdescription, color=0xff8000)
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
                    embed.add_field(name = langue.kickuser, value = user.mention, inline = True)
                    embed.add_field(name = langue.reason, value = reason, inline = True)
                    embed.add_field(name = langue.moderator, value = ctx.author.mention, inline = True)
                    await ctx.guild.kick(user, reason = reason)
                    await ctx.send(embed = embed)
                    return await Logs.logsKick(self, ctx, user, reason)
                except:
                    return await ctx.send(langue.errorbotdoesnthavepermissions)
                
            if ctx.author.top_role < user.top_role:
                return await ctx.send(langue.kicktoprole)
            
            if ctx.author.top_role == user.top_role:
                return await ctx.send(langue.kickequalrole)
        else:
            return await ctx.send(langue.kickbot)

    
    async def is_discord_member(self, member: str, guild):
        try:
            return guild.get_member(int(member_re.sub("" ,member)))
        except Exception as e:
            return
