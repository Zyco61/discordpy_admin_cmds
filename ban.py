import discord
from discord.enums import _is_descriptor
from discord.ext import tasks, commands
from discord.utils import get
import datetime
import re
from Data.database_handler import DataBaseHandler
from logs import Logs
from get_language import get_language

database_handler = DataBaseHandler("database.db")

time_re = re.compile(r"\d+[smhd]")
member_re = re.compile(r"[\D]")

def convert_time(a:int):
    d = 0
    h = 0
    m = 0
    while a > 59:
        if a >= 86400:
            d += 1
            a -= 86400
        elif a >= 3600:
            h += 1
            a -= 3600
        elif a >= 60:
            m += 1
            a -= 60
    msg = ""
    if d != 0:
        msg += f"{d}j "
    if h != 0:
        msg += f"{h}h "
    if m != 0:
        msg += f"{m}m "
    if a != 0:
        msg += f"{a}s"
    return msg

def get_time(time:str, index:int) -> int:
    sec = 0
    mult = 1
    for i in range(index-1, -1, -1):
        if not time[i].isdigit():
            return sec
        sec += int(time[i])*mult
        mult *= 10
    return sec

def calcul(time:str):
    if not bool(time_re.match(time)):
        return -1
    sec = 0
    x = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    for i in range(len(time)):
        if time[i] in x:
            sec += get_time(time, i) * x[time[i]]
    return sec

def setup(bot):
    bot.add_cog(Ban(bot))

class Ban(commands.Cog):
    def __init__(self, bot):
        self.check_for_unban.start()
        self.bot = bot
    
    def cog_unload(self):
        self.check_for_unban.cancel()
        
        
      
    
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, *args):
        langue = get_language(ctx)
        member = None
        time = -1
        raison = ""
        a = []

        for e in args:
            if not member and (member := await self.is_discord_member(e, ctx.guild)):
                    a.append(e)

            if time == -1 and bool(time_re.match(e)) and (time := calcul(e)):
                    a.append(e)

        raison = " ".join(args)
        for w in a:
            raison = raison.replace(w, "")

                
        if not member:
            return await ctx.send(langue.nouser)

        if member == ctx.author:
            await ctx.message.delete()
            return await ctx.send(langue.banme)
                
        if raison == "" or raison == " ":
            raison = langue.noreason
        if ctx.author.top_role > member.top_role or ctx.author == ctx.guild.owner:
            if time != -1:
                database_handler.add_tempban(member.id, ctx.guild.id, datetime.datetime.now() + datetime.timedelta(seconds=time))
                await member.ban(reason = raison)
                embed = discord.Embed(title = langue.titleban, color=0xff8000)
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
                embed.add_field(name = langue.userbanned, value = member.mention, inline = False)
                embed.add_field(name = langue.banduration, value = convert_time(time), inline = False)
                embed.add_field(name = langue.reason, value = raison, inline = False)
                embed.add_field(name = langue.moderator, value = ctx.author.mention, inline = False)
                await ctx.send(embed = embed)
                return await Logs.logsBan(self, ctx, member, raison, convert_time(time))

            else:
                database_handler.add_tempban(member.id, ctx.guild.id,  "∞")
                await member.ban(reason = raison)
                embed = discord.Embed(title = langue.titleban, color=0xff8000)
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
                embed.add_field(name = langue.userbanned, value = member.mention, inline = False)
                embed.add_field(name = langue.banduration, value = "∞", inline = False)
                embed.add_field(name = langue.reason, value = raison, inline = False)
                embed.add_field(name = langue.moderator, value = ctx.author.mention, inline = False)
                await ctx.send(embed = embed)
                return await Logs.logsBan(self, ctx, member, raison,  "∞")

        if ctx.author.top_role < member.top_role:
            return await ctx.send(langue.bantoprole)
            
        if ctx.author.top_role == member.top_role:
            return await ctx.send(langue.banequalrole)

    
    async def is_discord_member(self, member: str, guild):
        try:
            return guild.get_member(int(member_re.sub("" ,member)))
        except Exception as e:
            return

    @tasks.loop(seconds=1)
    async def check_for_unban(self):
        for guild in self.bot.guilds:
            active_tempban = database_handler.active_tempban_to_revoke(guild.id)
            if len(active_tempban) > 0:
                for row in active_tempban:
                    member = row["user_id"]
                    database_handler.revoke_tempban(row["id"])
                    database_handler.supr_tempban()
                    bans = await guild.bans()
                    for ban in bans:
                        if ban[1].id == member:
                            await guild.unban(ban[1])
