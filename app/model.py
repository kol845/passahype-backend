import json
import sys
from app.db_handler import DB
from flask_bcrypt import Bcrypt
from flask import jsonify
import jwt
from utils.files import get_full_path
import base64
import time
import datetime as dt

#Flask printing:
#print('Hello world!', file=sys.stderr)
'''
Returning user 
(2, 'pebo', '$2b$12$NQCUiCBA6C/Onf9KHwCEUe90O4bnJQmC5T5d8i8oPT5n5OGFOMTya', 
'2020-07-31 18:39:08.433990')
'''


class Model:
    def __init__(self):
        super().__init__()
        self.db = DB()
        apiErrorsFile = get_full_path("app/apiErrors.json")
        self.apiErrors = json.loads(open(apiErrorsFile,"r").read())
        self.statusRejected = 2
        self.statusAccepted = 1
        #JWT experation time in minutes
        self.jwtExperationTime = 30
        # The exposure of the hard-coded jwt secret key is a concern...
        self.jwtSecret = '73869a97078920dd470b20a6f7487c81'
    def getReject(self, err_type):
        response = {'status':self.statusRejected,'error':self.apiErrors[err_type]}
        return response
    def getAccept(self, data={}):
        response = {'status':self.statusAccepted}
        response.update(data)
        return response
    def createJWT(self, uid, uname):
        experation = time.time()+self.jwtExperationTime*60
        jwtData = {'uid':uid,'uname':uname,'exp':experation}
        token = jwt.encode(jwtData,self.jwtSecret)
        token = base64.b64encode(token).decode("ascii")
        return token
    def authPasswd(self,hashedPasswd,passwd):
        #print(f"Hashed: {hashedPasswd}, Passwd: {passwd}, Result: {Bcrypt().check_password_hash(hashedPasswd,passwd)}", file=sys.stderr)
        return Bcrypt().check_password_hash(hashedPasswd,passwd)
    def login(self, data):
        if 'uname' in data and 'passwd' in data:
            passwd = data['passwd']
            uname = data['uname']
            query = self.db.getUserIDAndPassword(uname)
            if(len(query)==0):
                return self.getReject('LOGIN_ERROR')
            (uid, storedPasswd) = query[0]

            if (self.authPasswd(storedPasswd, passwd)):
                token = self.createJWT(uid, uname)
                return self.getAccept({'uid':uid, 'uname':uname, 'jwt':token})
            else:
                return self.getReject('LOGIN_ERROR')
        else:
            error = self.getReject("ARG_MISSING")
            return error
    def registerUser(self, data):
        if 'uname' in data and 'passwd' in data:
            passwd = data['passwd']
            uname = data['uname']
            query = self.db.checkIfUsernameExists(uname)
            if(len(query)==0):
                hashed_passwd = Bcrypt().generate_password_hash(passwd).decode('utf-8')
                reg_date = dt.datetime.now()
                self.db.registerUser(uname, hashed_passwd, reg_date)
                return self.getAccept()
            return self.getReject("UNAME_ALREADY_EXISTS")
        else:
            error = self.getReject("ARG_MISSING")
            return error