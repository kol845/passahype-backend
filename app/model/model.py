import json
import sys
from flask_bcrypt import Bcrypt
from flask import jsonify
import jwt
import psycopg2
from utils.files import get_full_path
import base64
import time
# import datetime as dt
import time
import re 

from sqlalchemy import exc

from app.integration.db_handler import DB
from app.utils.utils import Utils
from app.utils.config import Config

#Flask printing:
#print('Hello world!', file=sys.stderr)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # Used for email control

class Model:
    def __init__(self):
        super().__init__()
        self.db = DB()
        apiErrorsFile = get_full_path("app/utils/apiErrors.json")
        self.apiErrors = json.loads(open(apiErrorsFile,"r").read())
        self.statusRejected = 0
        self.statusAccepted = 1
        #JWT experation time in minutes
        self.jwtExperationTime = 30
        # The exposure of the hard-coded jwt secret key is a concern...
        self.jwtSecret = Config.JWT_SECRET
        self.defaultUtype = 0
    def getReject(self, err_type):
        response = {'status':Utils.REJECTED,'error':self.apiErrors[err_type]}
        return response
    def getAccept(self, data={}):
        response = {'status':Utils.ACCEPTED}
        response.update(data)
        return response
    def createJWT(self, uid, email):
        experation = time.time()+Utils.JWT_EXP
        jwtData = {'uid':uid,'email':email,'exp':experation}
        token = jwt.encode(jwtData,self.jwtSecret)
        token = base64.b64encode(token).decode("ascii")
        return token
    def authPasswd(self,hashedPasswd,passwd):
        #print(f"Hashed: {hashedPasswd}, Passwd: {passwd}, Result: {Bcrypt().check_password_hash(hashedPasswd,passwd)}", file=sys.stderr)
        return Bcrypt().check_password_hash(hashedPasswd,passwd)
    def login(self, data):
        if 'email' in data and 'passwd' in data:
            email = data['email']
            passwd = data['passwd']
            user = self.db.getUser(email=email)
            if(not user): # If no user with that email exists in DB
                return self.getReject('LOGIN_ERROR')
            if (self.authPasswd(user.passwd, passwd)):
                token = self.createJWT(user.id, email)
                return self.getAccept({'uid':user.id, 'email':email, 'jwt':token})
            else:
                return self.getReject('LOGIN_ERROR')
        else:
            error = self.getReject("ARG_MISSING")
            return error
    def registerUser(self, data):
        if 'email' in data and 'passwd' in data:
            email = data['email']
            email = email.lower()
            passwd = data['passwd']
            if(not emailControl(email)):
                error = self.getReject("BAD_EMAIL")
                return error
            
            if(not passwdControl(passwd)):
                error = self.getReject("BAD_PASSWD")
                return error
            
            utype = self.defaultUtype
            hashed_passwd = Bcrypt().generate_password_hash(passwd).decode('utf-8')
            regDate = time.time()
            if('utype' in data):
                utype = data[utype]
            try:
                self.db.registerUser(email=email, passwd= hashed_passwd, regDate = regDate, utype=utype)
            except exc.IntegrityError as e:
                error = self.getReject("USER_ALREADY_EXISTS")
                return error
            except Exception as e:
                print(f"Error occured during user registration in the DB: {e}")
            return self.getAccept()
            # return self.getReject("UNAME_ALREADY_EXISTS")
        else:
            error = self.getReject("ARG_MISSING")
            return error

def emailControl(email):
    if(re.search(regex,email) and len(email)<=Utils.MAX_CHARS):  
        return True
    else:
        return False 
def passwdControl(passwd):
    if(len(passwd)>=Utils.MIN_PASSWD and len(passwd)<=Utils.MAX_CHARS):
        return True
    else:
        return False

