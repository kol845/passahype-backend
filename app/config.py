# When deploying, move config.json to /etc/config.json, and change the URL ""./config.json" to point at "/etc/config.json", as shown in:
# https://www.youtube.com/watch?v=goToXTC96Co
import json
with open('./app/config.json') as configFile:
    config = json.load(configFile)

class Config:
    JWT_SECRET = config.get("JWT_SECRET")
    HOST = config.get("HOST")
    DBNAME = config.get("DBNAME")
    UNAME = config.get("UNAME")
    PASSWD = config.get("PASSWD")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
