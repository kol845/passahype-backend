from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pebo:ZMw9p25AVAG2vFkWrPj24Usyr@localhost/passahype'
db = SQLAlchemy(app)


class EndUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    passwd = db.Column(db.String(128), unique=True, nullable=False)

    utype = db.Column(db.Integer, nullable=False)
    regDate = db.Column(db.Integer, nullable=False)
    avatar_processed = db.Column(db.LargeBinary)
    phone = db.Column(db.Integer)

    ocupation = db.Column(db.String(128))
    location = db.Column(db.String(128))
    pitch = db.Column(db.String(1248))
    description = db.Column(db.String(8248))
    website = db.Column(db.String(128))


    def __repr__(self):
        return f"User('{self.email}', '{self.utype}', '{self.regDate}')"

@app.route("/")
def fuck_off_tmp():
    return '<h1>I WILL NEVER BE SEEN.</h1>'

if __name__ == '__main__':
    app.run(debug=True)