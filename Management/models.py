from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    userId = db.Column(db.Integer, primary_key=True, nullable=False)
    userName = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    user = db.relationship('Order', backref='user')
    comments = db.relationship('Comment', backref='user')

class Event(db.Model):
    __tablename__ = 'event'
    eventId = db.Column(db.Integer, primary_key=True, nullable=False)
    eventName = db.Column(db.String(80))
    eventDateAndTime = db.Column(db.DateTime, nullable=False)
    eventType = db.Column(db.String(80))
    eventState = db.Column(db.Integer)
    description = db.Column(db.String(200))
    ticketQuantity = db.Column(db.Integer)
    ticketPrice = db.Column(db.Integer)
    eventImage = db.Column(db.String(400))

    order = db.relationship('Order', backref='event')
    comments = db.relationship('Comment', backref='event')




class Order(db.Model):
    __tablename__ = 'order'
    orderId = db.Column(db.Integer, primary_key=True, nullable=False)
    ticketQuantity = db.Column(db.Integer)
    totalCost = db.Column(db.Integer)
    orderDate = db.Column(db.DateTime, nullable=False)

    #add the foreign keys
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    eventId = db.Column(db.Integer, db.ForeignKey('event.eventId'))
   
   



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())


    #add the foreign keys
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'))
    eventId = db.Column(db.Integer, db.ForeignKey('event.eventId'))
