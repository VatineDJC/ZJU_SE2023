# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DDL


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    ID = db.Column(db.Integer, primary_key=True, unique=True,autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)
    phoneNumber = db.Column(db.String(11), nullable=False, unique=True)
    description = db.Column(db.String(511))
    permission = db.Column(db.String(8), nullable=False, default='user')
    stat = db.Column(db.String(8), nullable=False, default='offline')

class Order(db.Model):
    __tablename__ = 'orders'

    ID = db.Column(db.Integer,primary_key=True, unique=True,autoincrement=True)
    itemID = db.Column(db.ForeignKey('items.ID'), nullable=False, index=True)
    userID = db.Column(db.ForeignKey('users.ID'), nullable=False, index=True)
    stat = db.Column(db.String(16), nullable=False, default='progressing')

    item = db.relationship('Item', primaryjoin='Order.itemID == Item.ID', backref='orders')
    user = db.relationship('User', primaryjoin='Order.userID == User.ID', backref='orders')

class Item(db.Model):
    __tablename__ = 'items'

    ID = db.Column(db.Integer,primary_key=True, unique=True)
    userID = db.Column(db.ForeignKey('users.ID'), nullable=False, index=True,autoincrement=True)
    stat = db.Column(db.String(8), nullable=False, default='onsale')
    name = db.Column(db.String(63))
    price = db.Column(db.Float)
    description = db.Column(db.String(511))

    user = db.relationship('User', primaryjoin='Item.userID == User.ID', backref='items')

class Picture(db.Model):
    __tablename__ = 'pictures'

    ID = db.Column(db.Integer,primary_key=True, unique=True,autoincrement=True)
    itemID = db.Column(db.ForeignKey('items.ID'), nullable=False, index=True)
    imageData = db.Column(db.LargeBinary) # 新增的image列，用于存储二进制数据

    item = db.relationship('Item', primaryjoin='Picture.itemID == Item.ID', backref='pictures')

class Comment(db.Model):
    __tablename__ = 'comments'

    ID = db.Column(db.Integer,primary_key=True, unique=True,autoincrement=True)
    orderID = db.Column(db.ForeignKey('orders.ID'), nullable=False, index=True)
    commenterID = db.Column(db.ForeignKey('users.ID'), nullable=False, index=True)
    commentedID = db.Column(db.ForeignKey('users.ID'), nullable=False, index=True)
    content = db.Column(db.String(511))

    order = db.relationship('Order', primaryjoin='Comment.orderID == Order.ID', backref='comments')
    commenter = db.relationship('User', primaryjoin='Comment.commenterID == User.ID', backref='comments')
    commented = db.relationship('User', primaryjoin='Comment.commentedID == User.ID', backref='commented')