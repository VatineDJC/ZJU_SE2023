from flask import Blueprint, request, jsonify, session
from src.models import Item
from src.models import User
from sqlalchemy.orm import sessionmaker

from src.database import bs_db
from src.util import responseCode, login_required

item = Blueprint('item', __name__)

@item.route("/create", methods=["POST"])
@login_required
def createItem():
    db_session = sessionmaker(bind=bs_db)()

    userID = request.values.get('userID')
    name = request.values.get('name')
    price = request.values.get('price')
    description = request.values.get('description')

    # userID = 1
    # name = '圆珠笔'
    # price = 10
    # description = '这是一支圆珠笔'

    if userID is None or name is None:
        #参数为空
        db_session.close()
        return jsonify({'code': responseCode['invalid_args']})
    
    item = Item()
    item.userID = userID
    item.name = name
    item.price = price
    item.description = description

    query = db_session.query(User).filter(User.ID == item.userID).all()
    if not query:
        # 卖家ID不存在
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.add(item)
    db_session.flush()  # 刷新会话以获取新记录的主键值
    ID = item.ID
    db_session.commit()

    query = db_session.query(Item).filter(Item.ID == ID).all()

    if query:
        return jsonify({'code': responseCode['success'], 'ID': ID})
    else:
        return jsonify({'code': responseCode['error']})



@item.route("/search_key", methods=["POST"])
@login_required
def searchKey():
    db_session = sessionmaker(bind=bs_db)()

    input = request.values.get('input')

    if not input:
        db_session.close()
        return jsonify({'code': responseCode['invalid_args']})

    item_query = db_session.query(Item).filter(Item.name.like('%'+input+'%')).all()
    item_list = []
    for item in item_query:
        if item.valid == 'invalid':
            continue
        pics = item.pictures
        pic_list = []
        for pic in pics:
            pic_list.append({
                'imagePath': pic.path
            })
        item_list.append({
            'id': item.ID,
            'userID': item.userID,
            'stat': item.stat,
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'images': dict(enumerate(pic_list))
        })
    return jsonify({'code': responseCode['success'],
                    'data': dict(enumerate(item_list))})

@item.route("/update", methods=["POST"])
@login_required
def update():
    db_session = sessionmaker(bind=bs_db)()

    itemID = request.values.get('itemID')
    stat = request.values.get('stat')
    name = request.values.get('name')
    price = request.values.get('price')
    description = request.values.get('description')

    query = db_session.query(Item).filter(Item.ID == itemID).all()

    # 被更改的商品ID不存在
    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.query(Item).filter(Item.ID == itemID).update(
        {'stat': stat,
         'name': name,
         'price': price,
         'description': description})
    db_session.commit()
    db_session.close()

    return jsonify({'code': responseCode['success']})

@item.route("/delete", methods=["POST"])
@login_required
def delete():
    db_session = sessionmaker(bind=bs_db)()

    itemID = request.values.get('id')

    query = db_session.query(Item).filter(Item.ID == itemID).all()

    # 被更改的商品ID不存在
    if not query:
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.query(Item).filter(Item.ID == itemID).all().update(
        {'valid': 'invalid'})
    db_session.commit()
    db_session.close()

    return jsonify({'code': responseCode['success']})