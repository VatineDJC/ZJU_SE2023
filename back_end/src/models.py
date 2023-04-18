# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Device(db.Model):
    __tablename__ = 'device'

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    roomID = db.Column(db.ForeignKey('room.ID'), nullable=False, index=True)
    type = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.JSON, nullable=False)
    posx = db.Column(db.Float)
    posy = db.Column(db.Float)

    room = db.relationship('Room', primaryjoin='Device.roomID == Room.ID', backref='devices')



class Place(db.Model):
    __tablename__ = 'place'

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    userID = db.Column(db.ForeignKey('user.ID'), nullable=False, index=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(511), unique=True)

    user = db.relationship('User', primaryjoin='Place.userID == User.ID', backref='places')



class Room(db.Model):
    __tablename__ = 'room'

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    placeID = db.Column(db.ForeignKey('place.ID'), nullable=False, index=True)
    name = db.Column(db.String(20), nullable=False)
    img_src = db.Column(db.String(511))

    place = db.relationship('Place', primaryjoin='Room.placeID == Place.ID', backref='rooms')



class User(db.Model):
    __tablename__ = 'user'

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)
    phoneNumber = db.Column(db.String(11), nullable=False, unique=True)
    descpription = db.Column(db.String(511))