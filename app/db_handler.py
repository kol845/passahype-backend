import sys
import sqlite3
from utils.files import get_full_path
class DB:
    def __init__(self):
        super().__init__()
        dbFolder = "db"
        dbName = "alert.db"
        self.fullDBPath = get_full_path(dbFolder,dbName)
    def connect(self):
        return sqlite3.connect(self.fullDBPath)
    def checkIfUsernameExists(self, uname):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
        SELECT * FROM user
        WHERE uname = ? 
        ''', (uname,))
        rows = c.fetchall()
        conn.close()
        return rows
    def getUserIDAndPassword(self,uname):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
        SELECT id, passwd FROM user
        WHERE uname = ? 
        ''', (uname,))
        rows = c.fetchall()
        conn.close()
        return rows
    def getPassword(self, uid):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
        SELECT passwd FROM user
        WHERE id = ? 
        ''', (uid,))
        rows = c.fetchall()
        conn.close()
        return rows
    def getUserID(self, uname):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
        SELECT id FROM user
        WHERE uname = ? 
        ''', (uname,))
        rows = c.fetchall()
        conn.close()
        return rows
    def getToken(self, uID):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
        SELECT token FROM token
        WHERE user = ? 
        ''', (uID,))
        rows = c.fetchall()
        conn.close()
        return rows
    def registerUser(self, uname, passwd, reg_date):
        conn = self.connect()
        c = conn.cursor()
        c.execute(f'''
        INSERT INTO user(uname, passwd, reg_date)
        VALUES('{uname}','{passwd}','{reg_date}')
        ''')
        conn.commit()
        conn.close()