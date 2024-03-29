from flask import Blueprint, request, jsonify, session
from src.models import User
from src.models import Comment
from sqlalchemy.orm import sessionmaker
from src.database import bs_db
from src.util import responseCode, login_required, responseCode
import json

account = Blueprint('account', __name__)


@account.route("/check", methods=["POST"])
@login_required
def checkSession():

    DBsession = sessionmaker(bind=bs_db)()
    ID = session.get('ID')
    username = session.get('username')
    print(ID)
    if not ID:
        DBsession.close()
        return jsonify({'code': responseCode['error']})

    query = DBsession.query(User).filter(User.ID == ID).all()
    DBsession.close()
    return jsonify({'code': responseCode['success'], 'username': query[0].username,
                    'phoneNumber': query[0].phoneNumber, 'id':ID})


@account.route("/register", methods=["POST"])
def signUp():
    """
    signup: perform registry

    """
    db_session = sessionmaker(bind=bs_db)()

    username = request.values.get('username')
    password = request.values.get('password')
    phone = request.values.get('phoneNumber')

    # username = 'user1'
    # password = '1'
    # phone = '111'

    print(request.values)

    print(username, password, phone)

    if username is None or password is None:
        db_session.close()
        return jsonify({'code': responseCode['error']})

    registry = User()
    registry.username=username
    registry.password=password
    registry.phoneNumber=phone

    query = db_session.query(User).filter(User.username == registry.username).all()

    if query:
        db_session.close()
        return jsonify({'code': responseCode['user_already_exists']})

    query = db_session.query(User).filter(User.phoneNumber == registry.phoneNumber).all()

    if query:
        db_session.close()
        return jsonify({'code': responseCode['telephone_already_exists']})

    db_session.add(registry)
    db_session.flush()
    ID = ID = registry.ID
    db_session.commit()

    query = db_session.query(User).filter(User.ID == registry.ID).all()

    user = query[0]

    db_session.close()
    session['ID'] = user.ID
    return jsonify({'code': responseCode['success'], 'ID': ID})


@account.route("/login", methods=["POST"])
def signIn():
    """
    signin: perform login

    """
    db_session = sessionmaker(bind=bs_db)()
    # print(request)
    # print(request.json)

    # data = json.loads(request.get_data(as_text=True))
    #
    # if request.content_type ==
    # data = request.get_json();
    # print(data)
    # print(data.get('username'))

    username = request.values.get('username')
    password = request.values.get('password')
    # print(username, password)

    # 简单的边界条件 判空
    if username is None or password is None:
        db_session.close()
        return jsonify({'code': responseCode['error']})

    # check the validity of `user` and `password`
    query = db_session.query(User) \
        .filter(User.username == username) \
        .filter(User.password == password).all()

    if query and query[0].valid != 'invalid':
        db_session.query(User).filter(User.ID == query[0].ID).update(
        {'stat': 'online'})
    else:
        db_session.close()
        return jsonify({'code': responseCode['error']})


    db_session.close()

    if not query:
        return jsonify({'code': responseCode['error']})
    else:
        session['ID'] =query[0].ID
        return jsonify({'code': responseCode['success'],'id' : query[0].ID})


@account.route("/logout", methods=["POST"])
@login_required
def logOut():
    """
    logout: logout
    """

    db_session = sessionmaker(bind=bs_db)()
    db_session.query(User).filter(User.ID == session['ID']).update(
        {'stat': 'offline'})
    db_session.commit()
    session.pop("ID")
    db_session.close()
    return jsonify({'code': responseCode['success']})


@account.route("/changepassword", methods=["POST"])
@login_required
def modifyPassword():
    """
    modifypasswd: change password

    """
    db_session = sessionmaker(bind=bs_db)()

    # username = request.values.get('user')
    # 不能修改任意用户的密码，只能修改当前登陆的。
    ID = session.get('ID')
    old_password = request.values.get('oldpassword')
    new_password = request.values.get('newpassword')

    if ID is None or new_password is None:
        db_session.close()
        return jsonify({'code': responseCode['error']})

    query = db_session.query(User).filter(User.ID == ID).all()

    if query is []:
        db_session.close()
        return jsonify({'code': responseCode['login']['change-password']['id_doesnt_exist']})

    if old_password != query[0].password:
        db_session.close()
        return jsonify({'code': responseCode['login']['change-password']['old_is_wrong']})

    if new_password == old_password:
        db_session.close()
        return jsonify({'code': responseCode['login']['change-password']['same_password']})

    db_session.query(User).filter(User.ID == ID).update(
        {'password': new_password})
    db_session.commit()
    db_session.close()

    return jsonify({'code': responseCode['success']})


@account.route("/searchbyname", methods=["POST"])
@login_required
def searchUserByName():
    """
    searchUserByName: search by name

    """
    db_session = sessionmaker(bind=bs_db)()

    username = request.values.get('username')

    # 简单的边界条件 判空
    if username is None:
        db_session.close()
        return jsonify({'code': responseCode['error']})
    
    query = db_session.query(User) \
        .filter(User.username == username).all()

    query_2 = db_session.query(Comment) \
        .filter(Comment.commentedID == id).all()
    comments = []
    for comment in query_2:
        comments.append({
            'user':comment.commenterID,
            'content':comment.content,
            'time':'2023-05-20'
            })

    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})
    
    db_session.close()
    return jsonify({'code': responseCode['success'],
                    'id': query[0].ID,
                    'username': query[0].username,
                    'phoneNumber': query[0].phoneNumber,
                    'isLoggedIn': query[0].stat,
                    'description':query[0].description,
                    'comments':comments,
                    })

@account.route("/searchbyid", methods=["POST"])
@login_required
def searchUserByID():
    """
    searchUserByID: search by id

    """
    db_session = sessionmaker(bind=bs_db)()

    id = request.values.get('id')

    # 简单的边界条件 判空
    if id is None:
        db_session.close()
        return jsonify({'code': responseCode['invalid_args']})
    
    query = db_session.query(User) \
        .filter(User.ID == id).all()
    query_2 = db_session.query(Comment) \
        .filter(Comment.commentedID == id).all()
    comments = []
    for comment in query_2:
        comments.append({
            'user':comment.commenterID,
            'content':comment.content,
            'time':'2023-05-20'
            })
    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})
    
    db_session.close()
    return jsonify({'code': responseCode['success'],
                    'id': query[0].ID,
                    'username': query[0].username,
                    'phoneNumber': query[0].phoneNumber,
                    'isLoggedIn': query[0].stat,
                    'description':query[0].description,
                    'comments':comments
                    })

@account.route("/displayAllUser", methods=["GET"])
@login_required
def displayAllUser():
    db_session = sessionmaker(bind=bs_db)()
    query = db_session.query(User).all()
    ret_list = []
    for user in query:
        if user.valid == 'invalid':
            continue
        ret_list.append({
            'id': user.ID,
            'username': user.username,
            'phoneNumber': user.phoneNumber,
            'description': user.description,
        })
    db_session.close()
    return jsonify({'code': responseCode['success'],
                    'users': dict(enumerate(ret_list))})

@account.route("/delete", methods=["POST"])
@login_required
def deleteUser():
    db_session = sessionmaker(bind=bs_db)()

    userID = request.values.get('id')

    query = db_session.query(User).filter(User.ID == userID).all()

    if not query or query[0].valid == 'invalid':
        db_session.close()
        return jsonify({'code': responseCode['error']})

    db_session.query(User).filter(User.ID == userID).update({
        'valid': 'invalid'
    })

    db_session.commit()
    db_session.close()

    return jsonify({'code': responseCode['success']})
