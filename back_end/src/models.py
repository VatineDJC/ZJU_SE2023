# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)
    phoneNumber = db.Column(db.String(11), nullable=False, unique=True)
    descpription = db.Column(db.String(511))
    permission = db.Column(db.String(8), nullable=False, default='user', check_constraint="status IN ('user', 'admin')")
    status = db.Column(db.String(8), nullable=False, default='offline', check_constraint="status IN ('online', 'offline')")

class Order(db.Model):
    __tablename__ = 'order'

    ID = db.Column(db.Integer,primary_key=True, unique=True)
    itemID = db.Column(db.ForeignKey('item.ID'), nullable=False, index=True)
    userID = db.Column(db.ForeignKey('user.ID'), nullable=False, index=True)
    status = db.Column(db.String(16), nullable=False, default='progressing', check_constraint="status IN ('progressing', 'interrupted', 'success')")

    item = db.relationship('Item', primaryjoin='Order.itemID == Item.ID', backref='orders')
    user = db.relationship('User', primaryjoin='Order.userID == User.ID', backref='orders')

class Item(db.Model):
    __tablename__ = 'item'

    ID = db.Column(db.Integer,primary_key=True, unique=True)
    userID = db.Column(db.ForeignKey('user.ID'), nullable=False, index=True)
    status = db.Column(db.String(8), nullable=False, default='onsale', check_constraint="status IN ('onsale', 'offsale', 'reserved')")
    name = db.Column(db.String(63))
    name = db.Column(db.Float)
    descpription = db.Column(db.String(511))

    user = db.relationship('User', primaryjoin='Item.userID == User.ID', backref='items')

class Picture(db.Model):
    __tablename__ = 'picture'

    ID = db.Column(db.Integer,primary_key=True, unique=True)
    itemID = db.Column(db.ForeignKey('item.ID'), nullable=False, index=True)
    imageData = db.Column(db.LargeBinary) # 新增的image列，用于存储二进制数据

    item = db.relationship('Item', primaryjoin='Picture.itemID == Item.ID', backref='pictures')

class Comment(db.Model):
    __tablename__ = 'comment'

    ID = db.Column(db.Integer,primary_key=True, unique=True)
    orderID = db.Column(db.ForeignKey('order.ID'), nullable=False, index=True)
    commenterID = db.Column(db.ForeignKey('user.ID'), nullable=False, index=True)
    commentedID = db.Column(db.ForeignKey('user.ID'), nullable=False, index=True)
    content = db.Column(db.String(511))

    order = db.relationship('Order', primaryjoin='Comment.orderID == Order.ID', backref='comments')
    commenter = db.relationship('User', primaryjoin='Comment.commenterID == User.ID', backref='comments')
    commented = db.relationship('User', primaryjoin='Comment.commentedID == User.ID', backref='commented')