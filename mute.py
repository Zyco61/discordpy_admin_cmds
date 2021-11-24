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
    bot.add_cog(Mute(bot))

class Mute(commands.Cog):
    def __init__(self, bot):
        self.check_for_unmute.start()
        self.bot = bot
    
    def cog_unload(self):
        self.check_for_mute.cancel()
        
        
    
    async def get_muted_role(self, guild : discord.Guild) -> discord.Role:
        role = get(guild.roles, name="Mute")
        if role is not None:
            return role
        
        else:
            permissions = discord.Permissions(
                send_messages=False,
                speak =  False,
                add_reactions = False)
            role = await guild.create_role(name="Mute", permissions=permissions)
            await role.edit(position = guild.get_member(self.bot.user.id).top_role.position - 1)
            for channel in guild.channels:
                await channel.set_permissions(role, send_messages = False, speak = False)
            return role    
    
    
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, *args):
        langue = get_language(ctx)
        member = None
        time = -1
        raison = ""
        muted_role = await self.get_muted_role(ctx.guild)
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
        
        if ctx.guild.get_member(self.bot.user.id).top_role.position <= muted_role.position:
            return await ctx.send(langue.mutetoproleinpossible)

        for role in member.roles:
            if role.name == "Mute":
                return await ctx.send(langue.mutealreadymute)
                
        if raison == "" or raison == " ":
            raison = langue.noreason

        if time != -1:
            database_handler.add_tempmute(member.id, ctx.guild.id, datetime.datetime.now() + datetime.timedelta(seconds=time))
            await member.add_roles(muted_role)
            embed = discord.Embed(title = langue.mutetitle, color=0xff8000)
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/4274-muted.png")
            embed.add_field(name = langue.mutemember, value = member.mention, inline = False)
            embed.add_field(name = langue.muteduration, value = convert_time(time), inline = False)
            embed.add_field(name = langue.mutereason, value = raison, inline = False)
            embed.add_field(name = langue.mutemodo, value = ctx.author.mention, inline = False)
            await ctx.send(embed = embed)
            await Logs.logsMute(self, ctx, member, raison, convert_time(time))

        else:
            database_handler.add_tempmute(member.id, ctx.guild.id,  "∞")
            await member.add_roles(muted_role)
            embed = discord.Embed(title = langue.mutetitle, color=0xff8000)
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.set_thumbnail(url = "https://emoji.gg/assets/emoji/4274-muted.png")
            embed.add_field(name = langue.mutemember, value = member.mention, inline = False)
            embed.add_field(name = langue.muteduration, value = "∞", inline = False)
            embed.add_field(name = langue.mutereason, value = raison, inline = False)
            embed.add_field(name = langue.mutemodo, value = ctx.author.mention, inline = False)
            await ctx.send(embed = embed)
            await Logs.logsMute(self, ctx, member, raison,  "∞")

    
    async def is_discord_member(self, member: str, guild):
        try:
            return guild.get_member(int(member_re.sub("" ,member)))
        except Exception as e:
            return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if database_handler.is_muted(member.id, member.guild.id):
            mutedrole = await self.get_muted_role(member.guild)
            await member.add_roles(mutedrole)

    @tasks.loop(seconds=1)
    async def check_for_unmute(self):
        for guild in self.bot.guilds:
            active_tempmute = database_handler.active_tempmute_to_revoke(guild.id)
            if len(active_tempmute) > 0:
                muted_role = await self.get_muted_role(guild)
                for row in active_tempmute:
                    member = guild.get_member(row["user_id"])
                    database_handler.revoke_tempmute(row["id"])
                    database_handler.supr_tempmute()
                    await member.remove_roles(muted_role)