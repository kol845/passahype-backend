import sqlite3
import datetime as dt
from flask_bcrypt import Bcrypt
dbFolder = "./../db"
dbName = "alert.db"
conn = sqlite3.connect(f"{dbFolder}/{dbName}")
c = conn.cursor()

def createTables():
    c.execute('''
    CREATE TABLE user(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        uname TEXT NOT NULL UNIQUE,
        passwd TEXT NOT NULL,
        reg_date TEXT NOT NULL);
    ''')
    #TICKER table has error. 'name' should be 'user' and a INT. Foreign key is also not established
    c.execute('''
    CREATE TABLE ticker(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        ticker TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL UNIQUE);
    ''')
    c.execute('''
    CREATE TABLE alert(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user INTEGER NOT NULL,
        ticker INTEGER NOT NULL,
        price_target REAL NOT NULL,
        floor INTEGER NOT NULL,
        FOREIGN KEY(user) REFERENCES user(id),
        FOREIGN KEY(ticker) REFERENCES ticker(id));
    ''')
    c.execute('''
    CREATE TABLE token(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user INTEGER NOT NULL,
        token TEXT NOT NULL UNIQUE,
        exp_d TEXT NOT NULL,
        FOREIGN KEY(user) REFERENCES user(id));
    ''')
    conn.commit()
def createUser(uname, passwd, reg_date):
    c.execute(f'''
    INSERT INTO user(uname, passwd, reg_date)
    VALUES('{uname}','{passwd}','{reg_date}')
    ''')
    conn.commit()

def hash_pass(passwd):
    hashed_passwd = Bcrypt().generate_password_hash(passwd).decode('utf-8')
    return hashed_passwd
def createUserPrep():
    uname = "pebo"
    passwd = "admin"
    reg_date = dt.datetime.now()
    passwd = hash_pass(passwd)
    createUser(uname, passwd, reg_date)
def removeUser(uname):
    c.execute(f'''
    DELETE FROM user
    WHERE uname = '{uname}'
    ''')
    conn.commit()
def getAllUsers():
    c.execute(f'''
    SELECT * FROM user
    ''')
    rows = c.fetchall()
    conn.close()
    return rows
rows = getAllUsers()
for r in rows:
    print(r)

