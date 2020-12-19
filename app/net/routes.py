from flask import jsonify, request
from app import app
from app.controller import Controller
from app.integration.db_models import EndUser


contr = Controller()

@app.route("/", methods=['GET'])
def main():
    return "Welcome!\nTry to POST to the URL '/api/login' with postman"

@app.route("/api/login", methods=['POST'])
def login():
    data = request.args
    response = contr.login(data)
    return response

@app.route("/api/register", methods=['POST'])
def register():
    data = request.args
    response = contr.registerUser(data)
    return response
# @app.route("/test/<email>/<passwd>/<utype>/<regDate>")
# def addTest(email, passwd, utype, regDate):
#     endUser = EndUser(email=email, passwd=passwd, utype=utype, regDate=regDate)
#     db.session.add(endUser)
#     db.session.commit()
#     return '<h1>User successfully added!!</h1>'