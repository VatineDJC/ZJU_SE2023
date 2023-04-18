from flask import Blueprint, request, jsonify, session
from src.models import User
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
        return jsonify({'state': responseCode['error']})

    query = DBsession.query(User).filter(User.ID == ID).all()
    DBsession.close()
    return jsonify({'state': responseCode['success'], 'username': query[0].username, 'phoneNumber': query[0].phoneNumber})


@account.route("/register", methods=["POST"])
def signUp():
    """
    signup: perform registry

    """
    db_session = sessionmaker(bind=bs_db)()

    username = request.values.get('username')
    password = request.values.get('password')
    phone = request.values.get('phoneNumber')

    print(request.values)

    print(username, password, phone)

    if username is None or password is None:
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
    db_session.commit()

    query = db_session.query(User).filter(User.username == registry.username).all()

    user = query[0];

    ID = user.ID

    db_session.close()
    session['ID'] = user.ID
    return jsonify({'code': responseCode['success'],'ID' : ID})


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
        return jsonify({'code': responseCode['error']})

    # check the validity of `user` and `password`
    query = db_session.query(User) \
        .filter(User.username == username) \
        .filter(User.password == password).all()

    db_session.close()

    if not query:
        return jsonify({'code': responseCode['error']})
    else:
        session['ID'] =query[0].ID
        return jsonify({'code': responseCode['success']})


@account.route("/logout", methods=["POST"])
@login_required
def logOut():
    """
    logout: logout
    """
    session.pop("ID")
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



