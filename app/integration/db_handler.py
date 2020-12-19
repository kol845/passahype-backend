from app import db
from app.integration.db_models import EndUser


class DB():
    def registerUser(self, email, passwd, regDate, utype = 0):
        newUser = EndUser(email=email, passwd=passwd, regDate=regDate, utype=utype)
        db.session.add(newUser)
        db.session.commit()
        # print(f"Creating user: {email}, {regDate}, {passwd}")
    def getUser(self, email):
        user = EndUser.query.filter_by(email=email).first()
        return user
    # def getToken(self, uid):
    #     token = Token.query.filter_by(endUserID=uid).first()
    #     return token
    # def setToken(self, token, uid):
    #     token = Token.query.filter_by(endUserID=uid).first()
    #     if(token):
    #         db.session.delete(token)
    #     newToken = Token(token=token, endUserID=uid)
    #     db.session.add(newToken)
    #     db.session.commit()