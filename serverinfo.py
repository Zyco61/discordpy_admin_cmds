import discord
from discord.ext import commands
from Data.database_handler import DataBaseHandler
from get_language import get_language

database_handler = DataBaseHandler("database.db")

def setup(bot):
    bot.add_cog(ServerInfo(bot))

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=["server", "servinfo", "serverinfos","servinfos","serveur"])
    async def serverinfo(self, ctx):
        langue = get_language(ctx)
        embed=discord.Embed(title=langue.serverinfotitle, color = 0x0000ff)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.add_field(name=langue.serverinfonameserver, value=f"{ctx.guild.name}", inline=False)
        embed.add_field(name=langue.serverinfoowneroftheserver, value = f"{ctx.guild.owner.mention}", inline = False)
        embed.add_field(name = langue.serverinfodesc, value = f"{ctx.guild.description}")
        embed.add_field(name = langue.serverinfocreatedat, value = f"{ctx.guild.created_at.strftime('%d/%m/%Y | %H:%M:%S')}", inline = False)
        embed.add_field(name=langue.serverinfonbofmembers, value=langue.serverinfonbofmembersanswer.format(ctx.guild.member_count), inline=False)
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
        embed.add_field(name =langue.serverinfomemberstatus, value = f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}")
        embed.add_field(name=langue.serverinfonbchann, value=langue.serverinfonbchannanswer.format(len(ctx.guild.text_channels), len(ctx.guild.voice_channels), len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)), inline=False)
        embed.add_field(name=langue.serverinfonbroles, value = langue.serverinfonbrolesanswer.format(len(ctx.guild.roles)), inline = False)
        embed.add_field(name=langue.serverinfonbboost, value=f"{ctx.guild.premium_subscription_count} boosts (palier {ctx.guild.premium_tier})", inline=False)
        await ctx.send(embed = embed)
        