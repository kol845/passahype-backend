from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

import sys
import os

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_object(Config)


# db.init_app(app)
from app import routes

