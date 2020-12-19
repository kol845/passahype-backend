# When deploying, move config.json to /etc/config.json, and change the URL ""./config.json" to point at "/etc/config.json", as shown in:
# https://www.youtube.com/watch?v=goToXTC96Co
import json
import os
with open('./app/utils/config.json') as configFile:
    config = json.load(configFile)

class Config:
    JWT_SECRET = config.get("JWT_SECRET")
    HOST = config.get("HOST")
    DBNAME = config.get("DBNAME")
    UNAME = config.get("UNAME")
    PASSWD = config.get("PASSWD")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")

    if(os.getenv("JWT_SECRET")):
        JWT_SECRET = os.getenv("JWT_SECRET")

    if(os.getenv("HOST")):
        JWT_SECRET = os.getenv("HOST")
    
    if(os.getenv("DBNAME")):
        JWT_SECRET = os.getenv("DBNAME")

    if(os.getenv("UNAME")):
        JWT_SECRET = os.getenv("UNAME")

    if(os.getenv("PASSWD")):
        JWT_SECRET = os.getenv("PASSWD")

    if(os.getenv("DATABASE_URL")):
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    
