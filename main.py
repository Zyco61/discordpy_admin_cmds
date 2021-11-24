import discord  
from discord.ext import tasks, commands
import sqlite3
from get_language import get_language
import os
from dotenv import load_dotenv
from Data.database_handler import DataBaseHandler

database_handler = DataBaseHandler("database.db")

load_dotenv()


intents = discord.Intents.all()

def get_prefix(bot, message):
    prefix = database_handler.get_prefix(message.guild.id)
    return prefix

bot = commands.Bot(command_prefix = get_prefix, intents = intents, case_insensitive=True, strip_after_prefix = True)
bot.remove_command("help")
owner = int(os.getenv("BOT_OWNER_ID"))

#help
@bot.command()
async def help(ctx, commandSent=None):
    langue = get_language(ctx)
    if commandSent != None:

        for command in bot.commands:
            if commandSent.lower() == command.name.lower():

                paramString = ""

                for param in command.clean_params:
                    paramString += param + ", "

                paramString = paramString[:-2]

                if len(command.clean_params) == 0:
                    paramString = "None"
                embed=discord.Embed(title=f"HELP - {command.name}", description=command.description)
                embed.add_field(name="paramètres", value=paramString)
                await ctx.send(embed=embed)
            else:
                return await ctx.send(langue.cmdnotfoundhelp.format(commandSent))
        
    else:
        await helpNormal(ctx, langue)
#help normal      
async def helpNormal(ctx, langue):
    embed=discord.Embed(title=langue.helptitle, color = 0x0000ff)
    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
    embed.add_field(name=langue.generaltitle, value='_ _', inline=False)
    embed.add_field(name = "help", value = langue.helphelp, inline=False)
    embed.add_field(name = "serverinfo", value = langue.serverinfohelp, inline = False)
    embed.add_field(name = "memberinfo", value = langue.memberinfohelp, inline = False)
    message = await ctx.send(embed = embed)
    await message.add_reaction("▶️")
    
    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "▶️" )
        
    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 120, check = checkEmoji)
        
        if reaction.emoji == "▶️":
            await message.delete()
            await helpModo(ctx, langue)
                
    except Exception as e:
        print(e)
        return
        
#help modo
async def helpModo(ctx, langue):
    embed=discord.Embed(title=langue.helptitle, color = 0x0000ff)
    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
    embed.add_field(name=langue.modotitle, value='\u200b', inline=False)
    embed.add_field(name = "clear", value = langue.clearhelp)
    embed.add_field(name="kick", value=langue.kickhelp, inline=False)
    embed.add_field(name="ban", value=langue.banhelp.format(database_handler.get_prefix(ctx.guild.id), ctx.author.mention), inline=False)
    embed.add_field(name="unban", value=langue.unbanhelp, inline=False)
    embed.add_field(name = "mute", value = langue.mutehelp.format(database_handler.get_prefix(ctx.guild.id), ctx.author.mention), inline = False)
    embed.add_field(name = "unmute", value = langue.unmutehelp, inline = False)
    embed.add_field(name = "lock", value = langue.lockhelp, inline = False)
    embed.add_field(name = "unlock", value = langue.unlockhelp)
    embed.add_field(name = "nuke", value = langue.nukehelp, inline = False)
    message = await ctx.send(embed = embed)
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    
    def checkEmoji(reac, user):
        return ctx.message.author == user and message.id == reac.message.id and (str(reac.emoji) == "▶️" or str(reac.emoji) == "◀️")
        
    try:
        reac, user = await bot.wait_for("reaction_add", timeout = 120, check = checkEmoji)
            
        if reac.emoji == "▶️":
            await message.delete()
            await helpAdmin(ctx, langue)
            
        elif reac.emoji == "◀️":
            await message.delete()
            await helpNormal(ctx, langue)
                
    except Exception as e:
        print(e)
        return
#help admin
async def helpAdmin(ctx, langue):      
    embed=discord.Embed(title=langue.helptitle, color = 0x0000ff)
    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
    embed.add_field(name=langue.admintitle, value='\u200b', inline=False)
    embed.add_field(name="settings", value=langue.helpsettings, inline=False)
    embed.add_field(name="say", value=langue.helpsay, inline=False)
    message = await ctx.send(embed = embed)
    await message.add_reaction("⬅️")
    
    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "⬅️" )
        
    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 120, check = checkEmoji)
        
        if reaction.emoji == "⬅️":
            await message.delete()
            await helpModo(ctx, langue)
                
    except Exception as e:
        print(e)
        return


@bot.listen()
async def on_ready():
    bot.load_extension("erreurs")
    bot.load_extension("settings")
    bot.load_extension("mute")
    bot.load_extension("unmute")
    bot.load_extension("logs")
    bot.load_extension("ban")
    bot.load_extension("lock")
    bot.load_extension("nuke")
    bot.load_extension("unban")
    bot.load_extension("kick")
    bot.load_extension("clear")
    bot.load_extension("say")
    bot.load_extension("memberinfo")
    bot.load_extension("serverinfo")
    print("Bot ready")

@bot.listen()
async def on_guild_join(guild):
    database_handler.create_prefix(guild.id)
    database_handler.create_opt_lvl(guild.id)

@bot.listen()
async def on_guild_remove(guild):
    database_handler.delete_prefix(guild.id)
    database_handler.delete_opt_lvl(guild.id)

#reload
@bot.command()
async def reload(ctx, name=None):
    langue = get_language(ctx)
    if ctx.author.id == owner:
        if name:
            if name == "main":
                return await ctx.send("Vous ne pouvez pas relancer ce fichier.")
            try:
                bot.load_extension(name)
                await ctx.message.delete()
                await ctx.send(f"Le fichier **{name}.py** à bien été reload par {ctx.author.mention}.")
            except:
                bot.unload_extension(name)
                bot.load_extension(name)
                await ctx.message.delete()
                await ctx.send(f"Le fichier **{name}.py** à bien été reload par {ctx.author.mention}.")
                
        else:
            await ctx.message.delete()
            await ctx.send("Précisez un fichier à relancer.")
    else:
        return await ctx.send(langue.nocmd)

#unload
@bot.command()
async def unload(ctx, name=None):
    langue = get_language(ctx)
    if ctx.author.id == owner:
        if name:
            try:
                await ctx.message.delete()
                bot.unload_extension(name)
                await ctx.send(f"Le fichier **{name}.py** à bien été unload par {ctx.author.mention}.")
            except:
                await ctx.message.delete()
                await ctx.send("Impossible")

    else:
        return await ctx.send(langue.nocmd)




bot.run(os.getenv("BOT_TOKEN"))