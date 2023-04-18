import functools
from flask import session

# 错误码
responseCode = {
    'login': {
        'change-password' : {
            'id_doesnt_exist': 101,
            'old_is_wrong': 102,
            'same_password': 103
        }
    },
    'place': {

    },
    'room' : {

    },
    'device' : {

    },
    'success': 0,
    'error': 1,
    'user_already_exists': 2,
    'user_doesnot_exist': 3,
    'telephone_already_exists': 4,
    'identical_password_required': 5,
    'scene_doesnot_exist': 6,
    'login_required': 7,
    'room_doesnot_exist': 8,
    'wrong_device_type_id': 9,
    'install_error': 10,
    'uninstall error': 11,
    'device_doesnot_exist': 12,
    'bind_error': 13,
    'update_error': 14,
    'invalid_args': 15
}

# responseCode = {
#     'success': 0,
#     'error': 1,
#     'user_already_exists': 2,
#     'user_doesnot_exist': 3,
#     'telephone_already_exists': 4,
#     'identical_password_required': 5,
#     'scene_doesnot_exist': 6,
#     'login_required': 7,
#     'room_doesnot_exist': 8,
#     'wrong_device_type_id': 9,
#     'install_error': 10,
#     'uninstall error': 11,
#     'device_doesnot_exist': 12,
#     'bind_error': 13,
#     'update_error': 14,
#     'invalid_args': 15
# }



# 修饰器，需要登录状态
def login_required(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if session.get('ID'):
            return function(*args, **kwargs)
        else:
            return {"state": responseCode["login_required"]}

    return wrapper