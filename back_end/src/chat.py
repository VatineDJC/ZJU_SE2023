from sqlalchemy import or_, and_

from src.models import User
from src.models import Chat
from src.models import Message
from flask import Blueprint, request, jsonify, session

from sqlalchemy.orm import sessionmaker

from src.database import bs_db
from src.util import responseCode, login_required

chat = Blueprint('chat', __name__)


@chat.route("/create", methods=["POST"])
#@login_required
def createChat():
    db_session = sessionmaker(bind=bs_db)()

    UID1 = request.values.get('UID1')
    UID2 = request.values.get('UID2')

    # userID = 1
    # name = '圆珠笔'
    # price = 10
    # description = '这是一支圆珠笔'

    if UID1 is None or UID2 is None:
        # 参数为空
        db_session.close()
        return jsonify({'code': responseCode['invalid_args']})

    chat = Chat()
    chat.UID1 = UID1
    chat.UID2 = UID2

    query = db_session.query(Chat). \
        filter(or_(and_(Chat.UID1 == chat.UID1, Chat.UID2 == chat.UID2),
                   and_(Chat.UID1 == chat.UID2, Chat.UID2 == chat.UID1))).all()
    if query:
        # chat已存在
        db_session.close()
        return jsonify({'code': responseCode['chat_already_exists']})

    db_session.add(chat)
    db_session.flush()  # 刷新会话以获取新记录的主键值
    chatID = chat.ID
    db_session.commit()

    query = db_session.query(Chat).filter(Chat.ID == chatID).all()
    db_session.close()
    if query:
        return jsonify({'code': responseCode['success'], 'ID': chatID})
    else:
        return jsonify({'code': responseCode['error']})


@chat.route("/get", methods=["POST"])
#@login_required
def getChat():
    db_session = sessionmaker(bind=bs_db)()

    UID = request.values.get('UID')

    query = db_session.query(User). \
        filter(User.ID == UID).all()

    if not query:
        db_session.close()
        return jsonify({'code': responseCode['error']})

    user = query[0]
    chats = db_session.query(Chat). \
                        filter(or_(Chat.UID1 == UID, Chat.UID2 == UID)).all()
    chat_list = []
    for chat in chats:
        messages = chat.messages
        messages_list = []
        for message in messages:
            messages_list.append({
                'sender_id': message.senderUID,
                'text': message.text,
                'time': message.timestamp
            })
        if int(UID) == chat.UID1:
            user_id = chat.UID2
        else:
            user_id = chat.UID1

        user = db_session.query(User). \
            filter(User.ID == user_id).first()


        chat_list.append({
            'id': chat.ID,
            'user_id': user_id,
            'name': user.username,
            'avatar': "https://via.placeholder.com/40x40/ff0000/ffffff?text="+user.username[0],
            'messages': messages_list
        })
    db_session.close()
    return jsonify({'code': responseCode['success'],
                    'data': chat_list})


@chat.route("/send", methods=["POST"])
def sendMessage():
    db_session = sessionmaker(bind=bs_db)()

    chatID = request.values.get('chatID')
    sender_id = request.values.get('sender_id')
    text = request.values.get('text')
    time = request.values.get('time')

    messsage = Message()
    messsage.chatID = chatID
    messsage.senderUID = sender_id
    messsage.text = text
    messsage.timestamp = time

    db_session.add(messsage)
    db_session.flush()  # 刷新会话以获取新记录的主键值
    messsageID = messsage.ID
    db_session.commit()

    query = db_session.query(Message).filter(Message.ID == messsageID).all()
    db_session.close()
    if query:
        return jsonify({'code': responseCode['success']})
    else:
        return jsonify({'code': responseCode['error']})