import discord
from discord.ext import commands
from Data.database_handler import DataBaseHandler
from typing import Optional
import datetime
import re
from get_language import get_language

member_re = re.compile(r"[\D]")

database_handler = DataBaseHandler("database.db")

def setup(bot):
    bot.add_cog(MemberInfo(bot))

class MemberInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases = ["memberinfo", "membreinfos", "membreinfo", "membre", 'member'])
    async def memberInfos(self, ctx, target = None):
        langue = get_language(ctx)
        if not target:
            target = await self.is_discord_member(str(ctx.author.id), ctx.guild)
        else:
            target = await self.is_discord_member(target, ctx.guild)
        if not target:
            return await ctx.send(langue.nouser)
        



        def checkmute(target, guild):
            for role in target.roles:
                if role.name == "Mute":
                    temps = database_handler.quand_unmute(guild.id, target.id)
                    if temps == '∞':
                        temps = langue.memberinfomuteforever
                        return temps 
                    else:
                        temps = langue.memberinfomute.format(datetime.datetime.strptime(temps,'%Y-%m-%d %H:%M:%S.%f').strftime('%d/%m/%Y | %H:%M:%S'))
                        return temps
            temps = "Non"
            return temps

        embed = discord.Embed(title = langue.memberinfotitle.format(target), color=0xff8000)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = target.avatar_url)
        embed.add_field(name = langue.memberinfoid, value = f"{target.id}", inline = False)
        embed.add_field(name = langue.memberinfojoinedat.format(ctx.guild.name), value = target.joined_at.strftime('%d/%m/%Y | %H:%M:%S'), inline = False)
        embed.add_field(name = langue.memberinfocreatedat, value = target.created_at.strftime('%d/%m/%Y | %H:%M:%S'), inline=False)
        embed.add_field(name = langue.memberinfobestrole, value = target.top_role, inline=False)
        embed.add_field(name = langue.memberinfomuteornot, value = checkmute(target, ctx.guild), inline=False)
        return await ctx.send(embed = embed)


    async def is_discord_member(self, member: str, guild):
        try:
            return guild.get_member(int(member_re.sub("" ,member)))
        except Exception as e:
            print(e)
            return