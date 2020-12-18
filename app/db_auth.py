# REDUNDANT FILE, PLEASE REMOVE
class DBAuth:
    def __init__(self):
        super().__init__()
        self.jwtSecret = '73869a97078920dd470b20a6f7487c81'
        self.host = "localhost"
        self.dbName = "passahype"
        self.uname = "pebo"
        self.passwd = "ZMw9p25AVAG2vFkWrPj24Usyr"
    def getJwt(self):
        return self.jwtSecret
    def getHost(self):
        return self.host
    def getDBName(self):
        return self.dbName
    def getUname(self):
        return self.uname
    def getPasswd(self):
        return self.passwd