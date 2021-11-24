import discord
from discord.ext import tasks, commands
import sqlite3
import Languages.francais
import Languages.english
import Languages.espagnol
from Data.database_handler import DataBaseHandler

database_handler = DataBaseHandler("database.db")

def get_language(ctx):
    lang = database_handler.get_language(ctx.guild.id)
    if lang == 0:
        return Languages.english.Language
    elif lang == 1:
        return Languages.francais.Language
    elif lang == 2: 
        return Languages.espagnol.Language