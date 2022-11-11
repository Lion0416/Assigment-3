from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userName = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, unique=True, nullable=False)
    contactNumber = db.Column(db.String(100))
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    user = db.relationship('Order', backref='user')
    comments = db.relationship('Comment', backref='user')



class Event(db.Model):
    __tablename__ = 'event'
    eventid = db.Column(db.Integer, primary_key=True, nullable=False)
    eventName = db.Column(db.String(80))
    eventstartDate = db.Column(db.Date, nullable=False)
    eventstartTime = db.Column(db.Time, nullable=False)
    eventendDate = db.Column(db.Date, nullable=False)
    eventendTime = db.Column(db.Time, nullable=False)
    eventType = db.Column(db.Integer, db.ForeignKey('type.typeid'))
    eventStates = db.Column(db.Integer, db.ForeignKey('states.statesid'))
    description = db.Column(db.String(200))
    ticketQuantity = db.Column(db.Integer)
    ticketPrice = db.Column(db.Integer)
    eventImage = db.Column(db.String(400))

    order = db.relationship('Order', backref='event')
    comments = db.relationship('Comment', backref='event')


class Type(db.Model):
    __tablename__= 'type'
    typeid = db.Column(db.Integer, primary_key=True, nullable=False)
    type = db.Column(db.String(80))

    event = db.relationship('Event', backref = 'eventtype')

class States(db.Model):
    __tablename__= 'states'
    statesid = db.Column(db.Integer, primary_key=True, nullable=False)
    states = db.Column(db.String(80))

    event = db.relationship('Event', backref = 'eventstates')

class Order(db.Model):
    __tablename__ = 'order'
    orderid = db.Column(db.Integer, primary_key=True, nullable=False)
    ticketQuantity = db.Column(db.Integer)
    totalCost = db.Column(db.Integer)
    orderDate = db.Column(db.DateTime, nullable=False)

    #add the foreign keys
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventid = db.Column(db.Integer, db.ForeignKey('event.eventid'))
   
   



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())


    #add the foreign keys
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    eventid = db.Column(db.Integer, db.ForeignKey('event.eventid'))
