from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from app.utils.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{Config.UNAME}:{Config.PASSWD}@{Config.HOST}/{Config.DBNAME}'
db = SQLAlchemy(app)


class EndUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    passwd = db.Column(db.String(128), unique=True, nullable=False)

    utype = db.Column(db.Integer, nullable=False, default=0)
    regDate = db.Column(db.Integer, nullable=False, default=0)
    avatar_processed = db.Column(db.LargeBinary)
    phone = db.Column(db.Integer)

    ocupation = db.Column(db.String(128))
    location = db.Column(db.String(128))
    pitch = db.Column(db.String(1248))
    description = db.Column(db.String(8248))
    website = db.Column(db.String(128))


    def __repr__(self):
        return f"User('{self.email}', '{self.utype}', '{self.regDate}')"

# class Token(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     token = db.Column(db.String(128), nullable=False)
#     endUserID = db.Column(db.Integer, db.ForeignKey("end_user.id"))

#     def __repr__(self):
#         return f"Token('{self.id}', '{self.token}', '{self.endUserID}')"


@app.route("/")
def index():
    return '<h1>I WILL NEVER BE SEEN.</h1>'

if __name__ == '__main__':
    app.run(debug=True)