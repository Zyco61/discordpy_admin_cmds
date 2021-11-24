import discord
from discord.ext import commands
from Data.database_handler import DataBaseHandler
import asyncio
from get_language import get_language

database_handler = DataBaseHandler("database.db")

def setup(bot):
    bot.add_cog(Settings(bot))

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["set","setting"])
    @commands.has_permissions(administrator = True)
    async def settings(self, ctx):
        langue = get_language(ctx)
        
        #settingsprefix
        async def settingsprefix(self, ctx):
            embed = discord.Embed(title = langue.settingsprefixtitle)
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.add_field(name = langue.settingsprefixf1, value = langue.settingsprefixnow.format(database_handler.get_prefix(ctx.guild.id)), inline = False)
            message = await ctx.send(embed = embed)
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            
            def checkEmoji(reaction, user):
                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
            
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check = checkEmoji)
                
                if reaction.emoji == "✅":
                    await ctx.send(langue.settingsprefixselectprefix)
                    def checkMessage(message):
                        return message.author == ctx.message.author and ctx.message.channel == message.channel

                    try:
                        pref = await self.bot.wait_for("message", timeout = 10, check = checkMessage)
                        if len(pref.content) < 1:
                            return await ctx.send(langue.settingsprefixcantuseprefix)
                        if len(pref.content) > 5:
                            return await ctx.send(langue.settingsprefixtoolong)
                        database_handler.change_prefix(pref.content, ctx.guild.id)
                        await ctx.send(langue.settingsprefixnewprefix.format(database_handler.get_prefix(ctx.guild.id)))
                        
                    except:
                        return await ctx.send(langue.settingslvlfail)
                            
                elif reaction.emoji == "❌":
                    return
                
            except:
                return 
            
    
    #settingslogs
        async def settingslogs(self, ctx):
            embed = discord.Embed(title = langue.settingstitle)
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            logs = database_handler.recup_log(ctx.guild.id)
            
            if logs == 1:
                logs = "On"
                chan = database_handler.recup_logchann(ctx.guild.id)
                embed.add_field(name =langue.settingslogswantchangeparams, value = langue.settingslogsnewparams.format(logs, chan))
            
            elif logs == 0:
                logs = "Off"
                embed.add_field(name = langue.settingslogswantchangeparams, value = langue.settingslogsnewparams1.format(logs))
            
            message = await ctx.send(embed = embed)
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            
            def checkEmoji(reaction, user):
                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
        
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check = checkEmoji)
                
                if reaction.emoji == "✅":
                    await message.delete()
                    await changeLogs(self, ctx)
                
                elif reaction.emoji == "❌":
                    return
            
            except:
                return
            
        #changelogs
        async def changeLogs(self, ctx):
                
                #modelogs
            async def modeLogs(self, ctx):
                logs = database_handler.recup_log(ctx.guild.id)
                if logs == 1:
                    log = 0
                    database_handler.change_log(ctx.guild.id, log)
                    await ctx.send(langue.settingslogslogsoff)
                else:
                    log = 1
                    def checkMessage(message):
                            return message.author == ctx.message.author and ctx.message.channel == message.channel

                    try:
                        await ctx.send(langue.settingslogspingchann)
                        chann = await self.bot.wait_for("message", timeout = 30, check = checkMessage)
                        chann = chann.content[2:-1]
                        database_handler.change_logchann(ctx.guild.id, chann)
                        database_handler.change_log(ctx.guild.id, log)
                        await ctx.send(langue.settingslogsnewchann.format(database_handler.recup_logchann(ctx.guild.id)))
                        
                    except:
                        return
                    
                    
            #changeChanLogs
            async def changeChanLogs(self, ctx):
                def checkMessage(message):
                    return message.author == ctx.message.author and ctx.message.channel == message.channel

                try:
                    await ctx.send(langue.settingslogspingchann)
                    chann = await self.bot.wait_for("message", timeout = 30, check = checkMessage)
                    chann = chann.content[2:-1]
                    database_handler.change_logchann(ctx.guild.id, chann)
                    log = 1
                    database_handler.change_log(ctx.guild.id, log)
                    await ctx.send(langue.settingslogsnewchann.format(database_handler.recup_logchann(ctx.guild.id)))
                    
                except Exception as e:
                    print(e)
                    return
                    
                
            embedl = discord.Embed(title = langue.settingstitle)
            embedl.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embedl.add_field(name = ":one:", value = langue.settingslogsonoffsyslog, inline = False)
            embedl.add_field(name = ":two:", value = langue.settingslogschangelogchann, inline = False)
            message = await ctx.send(embed = embedl)
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
                
            def checkEmoji(reaction, user):
                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣")
                
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check = checkEmoji)
                
                if reaction.emoji == "1️⃣":
                    await message.delete()
                    await modeLogs(self, ctx)
                
                elif reaction.emoji == "2️⃣":
                    await message.delete()
                    await changeChanLogs(self, ctx)
        
            except Exception as e:
                print(e)
                return

        #settings langage
        async def settingslanguage(self, ctx):

            async def changelangage(self, ctx):
                embed = discord.Embed(title = langue.settingstitle)
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                embed.add_field(name = langue.settingslanguagewhatlangage, value = "_ _", inline = False)
                message = await ctx.send(embed = embed)
                await message.add_reaction("🇫🇷")
                await message.add_reaction("🇬🇧")
                await message.add_reaction("🇪🇸")
                
                def checkEmoji(reaction, user):
                    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "🇫🇷" or str(reaction.emoji) == "🇬🇧" or str(reaction.emoji) == "🇪🇸")
            
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check = checkEmoji)

                    
                    if reaction.emoji == "🇫🇷":
                        await message.delete()
                        database_handler.change_language(1, ctx.guild.id)
                        return await ctx.send("Je suis désormais en français !")

                    elif reaction.emoji == "🇬🇧":
                        database_handler.change_language(0, ctx.guild.id)
                        return await ctx.send("I'm in english now !")
                    elif reaction.emoji == "🇪🇸":
                        database_handler.change_language(2, ctx.guild.id)
                        return await ctx.send("Ahora soy español ")
                    	
                
                except:
                    return

                language = database_handler.get_language(ctx.guild.id)

                if language == 0:
                    database_handler.change_language(1, ctx.guild.id)
                    return await ctx.send("Je suis désormais en français !")

                elif language == 1:
                    database_handler.change_language(0, ctx.guild.id)
                    return await ctx.send("I'm now in english !")


            embed = discord.Embed(title = langue.settingstitle)
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            embed.add_field(name = langue.settingslanguagechangeornot, value = langue.settingslanguagechangeornot2, inline = False)
            message = await ctx.send(embed = embed)
            await message.add_reaction("✅")
            await message.add_reaction("❌")

            def checkEmoji(reaction, user):
                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
            
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check = checkEmoji)
                
                if reaction.emoji == "✅":
                    await message.delete()
                    await changelangage(self, ctx)
                    
                
                else:
                    return
            
            except:
                return


        #settings

        embed = discord.Embed(title = langue.settingstitle)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        embed.add_field(name = "_ _", value = langue.settingsallsettings)
        message = await ctx.send(embed = embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("❌")
            
        def checkEmoji(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "2️⃣" or str(reaction.emoji) == "3️⃣" or str(reaction.emoji) == "4️⃣" or str(reaction.emoji) == "❌" or str(reaction.emoji) == "5️⃣")
        
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout = 30, check = checkEmoji)
                    
            if reaction.emoji == "1️⃣":
                await message.delete()
                await settingsprefix(self, ctx)
            
            elif reaction.emoji == "2️⃣":
                await message.delete()
                await settingslogs(self, ctx)

            elif reaction.emoji == "3️⃣":
                await message.delete()
                await settingslanguage(self, ctx)
            else:
                return
        except Exception as e:
            print(e)
            return
        
