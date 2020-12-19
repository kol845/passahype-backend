# This file populates the DB with all the tables. Run this file on deployment.

from app import db
from app import app
from app.integration.db_models import EndUser

with app.app_context():
    db.create_all()

