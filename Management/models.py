from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	
    password_hash = db.Column(db.String(255), nullable=False)

