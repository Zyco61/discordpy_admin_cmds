import discord
from discord.ext import commands
from discord.utils import get
from logs import Logs
import re
from Data.database_handler import DataBaseHandler
from get_language import get_language

database_handler = DataBaseHandler("database.db")


member_re = re.compile(r"[\D]")

def setup(bot):
    bot.add_cog(Unban(bot))

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user):
        langue = get_language(ctx)
        
        bans = await ctx.guild.bans()
        if user.isdigit():
            for ban in bans:
                if ban[1].id == int(user):
                    await ctx.guild.unban(ban[1])
                    database_handler.unban(int(user), ctx.guild.id)
                    embed = discord.Embed(title = langue.unbantitle, description = langue.unbandesc, color=0xff8000)
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/2365-love.gif")
                    embed.add_field(name = langue.unbanmember, value = ban[1].mention, inline = True)
                    embed.add_field(name = langue.unbanmodo, value = ctx.author.mention, inline = True)
                    await ctx.send(embed = embed)
                    return await Logs.logsUnban(self, ctx, ban[1], ctx.author)

                else:
                    await ctx.send(langue.unbannotbanned)

        else:
            banned_users = await ctx.guild.bans()
            member = user
            member_name, member_discriminator = member.split('#')
            for ban_entry in banned_users:
                user = ban_entry.user
                
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    database_handler.unban(user.id, ctx.guild.id)
                    embed = discord.Embed(title = langue.unbantitle, description = langue.unbandesc, color=0xff8000)
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/2365-love.gif")
                    embed.add_field(name = langue.unbanmember, value = user.mention, inline = True)
                    embed.add_field(name = langue.unbanmodo, value = ctx.author.mention, inline = True)
                    await ctx.send(embed = embed)
                    return await Logs.logsUnban(self, ctx, user, ctx.author)
            return await ctx.send(langue.unbannotbanned)
