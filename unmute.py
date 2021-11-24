import discord
from discord.ext import commands
from logs import Logs
import re
from Data.database_handler import DataBaseHandler
from logs import Logs
from get_language import get_language

database_handler = DataBaseHandler("database.db")

member_re = re.compile(r"[\D]")

def setup(bot):
    bot.add_cog(Unmute(bot))

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def unmute(self, ctx, member):
        langue = get_language(ctx)
        member = await self.is_discord_member(member, ctx.guild)
        if not member:
            return await ctx.send(langue.nouser)

        for role in member.roles:
            if role.name == "Mute":
                await member.remove_roles(role)
                database_handler.unmute(member.id, ctx.guild.id)
                embed = discord.Embed(title = langue.unmutetitle, color=0xff8000)
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/1352-blurpleunmuted.png")
                embed.add_field(name = langue.unmutemember, value = member.mention, inline = False)
                embed.add_field(name = langue.unmutemodo, value = ctx.author.mention, inline = False)
                await ctx.send(embed = embed)
                return await Logs.logsUnmute(self, ctx, member)

        await ctx.send(langue.unmuteusernotmute)
        
    async def is_discord_member(self, member: str, guild):
        try:
            return guild.get_member(int(member_re.sub("" ,member)))
        except Exception as e:
            return