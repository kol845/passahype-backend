from datetime import datetime
from app import db

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
