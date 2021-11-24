import discord
import datetime
from discord.ext import commands
from discord.utils import get
from Data.database_handler import DataBaseHandler
from get_language import get_language


database_handler = DataBaseHandler("database.db")

def setup(bot):
    bot.add_cog(Logs(bot))

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
#log ban
    async def logsBan(self,ctx, membre, raison, duree):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logsbantitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logsbanmember, value=f"{membre} ({membre.id})", inline=False)
            embed.add_field(name = langue.logsbanduration, value = duree, inline=False)
            embed.add_field(name=langue.logsbanmodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.add_field(name=langue.logsbanreason, value=f"{raison}", inline = False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)
            
    #Logs Kick
    async def logsKick(self, ctx, membre, raison):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logskicktitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logskickmember, value=f"{membre} ({membre.id})", inline=False)
            embed.add_field(name=langue.logskickmodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.add_field(name=langue.logskickreason, value=f"{raison}", inline = False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)

    #Logs Unban     
    async def logsUnban(self, ctx, target, modo):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logsunbantitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logsunbanmember, value=f"{target} ({target.id})", inline=False)
            embed.add_field(name=langue.logsunbanmodo, value=f"{modo} ({modo.id})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)

    #Logs Mute
    async def logsMute(self, ctx, member, raison, duree):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logsmutetitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logsmutemember, value=f"{member} ({member.id})", inline=False)
            embed.add_field(name = langue.logsmutereason, value = f"{raison}", inline=False)
            embed.add_field(name = langue.logsmuteduration, value = duree)
            embed.add_field(name=langue.logsmutemodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)

    #Logs Unmute
    async def logsUnmute(self, ctx, member):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logsunmutetitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logsunmutemember, value=f"{member} ({member.id})", inline=False)
            embed.add_field(name=langue.logsunmutemodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)
            
    async def logsLock(self, ctx):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logstitlelock, value = "\u200b", inline=False)
            embed.add_field(name=langue.logslockchannel, value=f"{ctx.channel.mention} ({ctx.channel.id})", inline=False)
            embed.add_field(name=langue.logslockmodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)
            
    async def logsUnlock(self, ctx):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logsunlocktitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logsunlockchannel, value=f"{ctx.channel.mention} ({ctx.channel.id})", inline=False)
            embed.add_field(name=langue.logsunlockmodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)

                
    async def logsNuke(self, ctx, chan):
        langue = get_language(ctx)
        if database_handler.recup_log(ctx.guild.id) == 1:
            channel = self.bot.get_channel(database_handler.recup_logchann(ctx.guild.id))
            embed=discord.Embed(title=langue.logstitle, color = 0x0404B4)
            embed.add_field(name = langue.logsnuketitle, value = "\u200b", inline=False)
            embed.add_field(name=langue.logsnukechannel, value=f"{chan.mention} ({chan.id})", inline=False)
            embed.add_field(name=langue.logsnukemodo, value=f"{ctx.author} ({ctx.author.id})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().strftime('%d/%m/%Y | %H:%M:%S')}")
            await channel.send(embed = embed)