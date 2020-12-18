# from db_auth import DBAuth
# import psycopg2

# auth = DBAuth()

# conn = psycopg2.connect(database=auth.getDBName(), user=auth.getUname(), password=auth.getPasswd(), host=auth.getHost())

# cur = conn.cursor()

# cur.execute("""CREATE TABLE endUser (
#             id SERIAL NOT NULL,
#             email VARCHAR(320) NOT NULL,
#             passwd VARCHAR(128) NOT NULL,
#             utype INT NOT NULL,
#             regDate INT NOT NULL,
#             avatar_processed BYTEA,
#             phone INT,
#             occupation VARCHAR(128),
#             location VARCHAR(128),
#             pitch VARCHAR(4248),
#             description VARCHAR(8248),
#             website VARCHAR(320),
#             PRIMARY KEY(id)
#             );""")
# conn.commit()
# cur.close()
# conn.close()

# print(auth.getPasswd())

from config import Config

print(Config.UNAME)