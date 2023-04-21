from flask import Blueprint, request, jsonify, session
from src.models import Order
from src.models import User
from src.models import Item
from sqlalchemy.orm import sessionmaker

from src.database import bs_db
from src.util import responseCode, login_required

order = Blueprint('order', __name__)


@order.route("/create", methods=["POST"])
@login_required
def createOrder():
    db_session = sessionmaker(bind=bs_db)()

    itemID = request.values.get('itemID')
    userID = request.values.get('userID')

    if userID is None or itemID is None:
        # 参数为空
        return jsonify({'code': responseCode['invalid_args']})

    order = Order()
    order.itemID = itemID
    order.userID = userID

    query = db_session.query(Item).filter(Item.ID == itemID).all()
    if not query or query[0].valid == 'invalid':
        db_session.close()
        print('item not exist')
        return jsonify({'code': responseCode['error']})

    query = db_session.query(User).filter(User.ID == userID).all()
    if not query or query[0].valid == 'invalid':
        db_session.close()
        print('user not exist')
        return jsonify({'code': responseCode['error']})

    db_session.add(order)
    db_session.flush()  # 刷新会话以获取新记录的主键值
    ID = order.ID
    db_session.commit()

    query = db_session.query(Order).filter(Order.ID == ID).all()

    if query:
        return jsonify({'code': responseCode['success'], 'ID': ID})
    else:
        return jsonify({'code': responseCode['error']})


@order.route("/delete", methods=["POST"])
@login_required
def delete():
    db_session = sessionmaker(bind=bs_db)()

    orderID = request.values.get('id')

    query = db_session.query(Order).filter(Order.ID == orderID).all()

    # 被删除的orderID不存在
    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.query(Order).filter(Order.ID == orderID).all().update(
        {'valid': 'invalid'})
    db_session.commit()
    db_session.close()

    return jsonify({'code': responseCode['success']})


@order.route("/update", methods=["POST"])
@login_required
def update():
    db_session = sessionmaker(bind=bs_db)()

    orderID = request.values.get('id')
    stat = request.values.get('stat')

    query = db_session.query(Order).filter(Order.ID == orderID).all()
    # 被更改的orderID不存在
    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.query(Order).filter(Order.ID == orderID).all().update(
        {'stat': stat})
    db_session.commit()
    db_session.close()

    return jsonify({'code': responseCode['success']})


@order.route("/getOrderByID", methods=["POST"])
@login_required
def getOrderByID():
    db_session = sessionmaker(bind=bs_db)()

    orderID = request.values.get('id')
    query = db_session.query(Order).filter(Order.ID == orderID).all()
    # 被查找的orderID不存在
    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.close()
    return jsonify({'code': responseCode['success'],
                    'id': query[0].ID,
                    'itemID': query[0].itemID,
                    'userID': query[0].userID,
                    'stat': query[0].stat})


@order.route("/getOrderByUser", methods=["POST"])
@login_required
def getOrderByUser():
    db_session = sessionmaker(bind=bs_db)()

    userID = request.values.get('id')
    user = db_session.query(User).filter(User.ID == userID).all()

    if not user or user[0].valid == 'invalid':
        db_session.close()
        return

    order_query = user[0].orders
    order_list = []
    for order in order_query:
        if order.valid == 'invalid':
            continue
        order_list.append({
            'ID': order.ID,
            'itemID': order.item.ID,
            'userID': order.userID,
            'stat': order.stat
        })
    db_session.close()
    return jsonify({'code': responseCode['success'],
                    'data': dict(enumerate(order_list))
                    })
