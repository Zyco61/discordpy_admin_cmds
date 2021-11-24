import os
import sqlite3
import random
import datetime
from sqlite3.dbapi2 import connect

class DataBaseHandler():
    def __init__(self, database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def create_opt_lvl(self, guildid: int):
        cursor = self.con.cursor()
        query = f"INSERT INTO Options (guildid) VALUES (?);"
        cursor.execute(query, (guildid,))
        cursor.close()
        self.con.commit()
        
    def delete_prefix(self, guildid: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM prefix WHERE guildid = ?;"
        cursor.execute(query, (guildid,))
        cursor.close()
        self.con.commit()

    def delete_opt_lvl(self, guildid: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM options WHERE guildid = ?;"
        cursor.execute(query, (guildid,))
        cursor.close()
        self.con.commit()
        
    def create_prefix(self, guildid: int):
        cursor = self.con.cursor()
        query = f"INSERT INTO Prefix (guildid) VALUES (?);"
        cursor.execute(query, (guildid,))
        cursor.close()
        self.con.commit()
        
    def get_prefix(self, guildid: int) -> str:
        cursor = self.con.cursor()
        query = f"SELECT prefix FROM Prefix WHERE guildid = ?;"
        cursor.execute(query, (guildid,))
        result = list(map(dict, cursor.fetchall()))
        result = result[0]["prefix"]
        cursor.close()
        return result

    def change_prefix(self, prefix: str, guildid: int):
        cursor = self.con.cursor()
        query = f"UPDATE Prefix SET prefix = ? WHERE guildid = ?;"
        cursor.execute(query,(prefix, guildid,))
        cursor.close()
        self.con.commit()

    def add_tempmute(self, user_id : int, guild_id : int, expiration_date : datetime.datetime):
        cursor = self.con.cursor()
        query = "INSERT INTO Tempmute (user_id, guild_id, expiration_date) VALUES (?, ?, ?);"
        cursor.execute(query, (user_id, guild_id, expiration_date))
        cursor.close()
        self.con.commit()
        
    def active_tempmute_to_revoke(self, guild_id : int):
        cursor = self.con.cursor()
        query = f"SELECT * FROM Tempmute WHERE guild_id = ? AND active = 1 AND expiration_date < ?;"
        cursor.execute(query, (guild_id, datetime.datetime.now()))
        result = list(map(dict, cursor.fetchall()))
        cursor.close()
        return result

    def quand_unmute(self, guildid: int, userid: int) -> str:
        cursor = self.con.cursor()
        query = f"SELECT expiration_date FROM Tempmute WHERE guild_id = ? AND user_id = ?"
        cursor.execute(query, (guildid, userid))
        result = cursor.fetchone()
        result = result[0]
        cursor.close()
        return result
    
    def revoke_tempmute(self, tempmute_id : int):
        cursor = self.con.cursor()
        query = f"UPDATE Tempmute SET active = 0 WHERE id = ?;"
        cursor.execute(query, (tempmute_id,))
        cursor.close()
        self.con.commit()
    
    def supr_tempmute(self):
        cursor = self.con.cursor()
        query = f"DELETE FROM tempmute WHERE active = 0;"
        cursor.execute(query)
        cursor.close()
        self.con.commit()
    
    def unmute(self, userid: int, guildid: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM tempmute WHERE user_id = ? AND guild_id = ?;"
        cursor.execute(query,(userid, guildid))
        cursor.close()
        self.con.commit()
        
    def supr_tempmuteid(self, userid, guildid):
        cursor = self.con.cursor()
        query = f"DELETE FROM tempmute WHERE user_id = ? AND guild_id = ?;"
        cursor.execute(query, (userid, guildid))
        cursor.close()
        self.con.commit()
    
    def is_muted(self, userid, guildid):
        cursor = self.con.cursor()
        query = f"SELECT * FROM tempmute WHERE user_id = ? AND guild_id = ?;"
        cursor.execute(query, (userid, guildid))
        result = cursor.fetchone()
        result = result[0]
        cursor.close()
        return result != None


    def add_tempban(self, user_id : int, guild_id : int, expiration_date : datetime.datetime):
        cursor = self.con.cursor()
        query = "INSERT INTO tempban (user_id, guild_id, expiration_date) VALUES (?, ?, ?);"
        cursor.execute(query, (user_id, guild_id, expiration_date))
        cursor.close()
        self.con.commit()
        
    def active_tempban_to_revoke(self, guild_id : int):
        cursor = self.con.cursor()
        query = f"SELECT * FROM tempban WHERE guild_id = ? AND active = 1 AND expiration_date < ?;"
        cursor.execute(query, (guild_id, datetime.datetime.now()))
        result = list(map(dict, cursor.fetchall()))
        cursor.close()
        return result

    def quand_unban(self, guildid: int, userid: int) -> str:
        cursor = self.con.cursor()
        query = f"SELECT expiration_date FROM tempban WHERE guild_id = ? AND user_id = ?"
        cursor.execute(query, (guildid, userid))
        result = cursor.fetchone()
        result = result[0]
        cursor.close()
        return result
    
    def revoke_tempban(self, tempban_id : int):
        cursor = self.con.cursor()
        query = f"UPDATE tempban SET active = 0 WHERE id = ?;"
        cursor.execute(query, (tempban_id,))
        cursor.close()
        self.con.commit()
    
    def supr_tempban(self):
        cursor = self.con.cursor()
        query = f"DELETE FROM tempban WHERE active = 0;"
        cursor.execute(query)
        cursor.close()
        self.con.commit()
    
    def unban(self, userid: int, guildid: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM tempban WHERE user_id = ? AND guild_id = ?;"
        cursor.execute(query,(userid, guildid))
        cursor.close()
        self.con.commit()

    def get_language(self, guildid):
        cursor = self.con.cursor()
        query = f"SELECT language FROM Options WHERE guildid = ?"
        cursor.execute(query,(guildid,))
        result = cursor.fetchone()
        result = result[0]
        cursor.close()
        return result

    def change_language(self, language, guildid):
        cursor = self.con.cursor()
        query = f"UPDATE Options SET language = ? WHERE guildid = ?"
        cursor.execute(query, (language, guildid))
        cursor.close()
        self.con.commit()

    def recup_log(self, guildid: int) -> int:
        cursor = self.con.cursor()
        query = f"SELECT log FROM Options WHERE guildid = ?;"
        cursor.execute(query, (guildid,))
        result = cursor.fetchall()
        result = result[0]["log"]
        cursor.close()
        return result
    
    def recup_logchann(self, guildid: int) -> int:
        cursor = self.con.cursor()
        query = f"SELECT logchann FROM Options WHERE guildid = ?;"
        cursor.execute(query, (guildid,))
        result = list(map(dict, cursor.fetchall()))
        result = result[0]["logchann"]
        cursor.close()
        return result
    
    def change_logchann(self, guildid: int, chann = int):
        cursor = self.con.cursor()
        query = f"UPDATE Options SET logchann = ? WHERE guildid = ?;"
        cursor.execute(query,(chann, guildid))
        cursor.close()
        self.con.commit()
    
    def change_log(self, guildid: int, log = int):
        cursor = self.con.cursor()
        query = f"UPDATE Options SET log = ? WHERE guildid = ?;"
        cursor.execute(query,(log, guildid))
        cursor.close()
        self.con.commit()