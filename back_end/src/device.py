from random import randint, random
from flask import Blueprint, request, jsonify
from src.models import Device, Room
from sqlalchemy.orm import sessionmaker
from src.database import bs_db
from src.util import responseCode, login_required

DEFAULT_VALUE = {
    'light': 10,
    'sensor': randint(15, 35) + random(),
    'door_lock': 1,
    'switch': 0
}

device = Blueprint('device', __name__)


@device.route("/add", methods=["POST"])
@login_required
def createDevice():
    db_session = sessionmaker(bind=bs_db)()
    name = request.values.get('name')
    type = int(request.values.get('type'))
    roomID = request.values.get('roomid')
    info = request.values.get('info')

    new_device = Device()

    typename = ""
    if type == 0:
        typename = "light"
    elif type == 1:
        typename = "sensor"
    elif type == 2:
        typename = "switch"
    elif type == 3:
        typename = "lock"

    new_device.name = name
    new_device.type = type
    new_device.roomID = roomID
    new_device.info = info
    new_device.posx=0
    new_device.posy=0

    if type == 0 :
        info = {"light":1}
    elif type == 1:
        info = {"Temperature":23,"wet":60}
    elif type == 2:
        info = {"status":"off"}
    elif type == 3:
        info = {"status":"off"}

    new_device.info = info

    try:
        print(new_device.name)
        db_session.add(new_device)
        query = db_session.query(Device) \
            .filter(Device.name == name) \
            .order_by(Device.ID.desc()) \
            .all()
        new_device_id = query[0].ID
        db_session.commit()
    except Exception as e:
        print(e)
        db_session.close()
        return jsonify({'code': responseCode['install_error']})

    db_session.close()

    return jsonify({
        'ID': new_device_id,
        'code': responseCode['success'],
        'data': {
            'id': new_device_id,
            'name': name,
            'type': type,
            "posx": 0,
            "posy": 0,
            "info": info,
            "type_content": typename
        }
    })


@device.route("/delete", methods=["POST"])
@login_required
def delete():
    db_session = sessionmaker(bind=bs_db)()
    deleted_device_id = request.values.get('id')
    if deleted_device_id is None:
        return jsonify([{'code': responseCode['error']}])

    query = db_session.query(Device).filter(
        Device.ID == deleted_device_id).all()
    if not query:
        return jsonify({'code': responseCode['device_doesnot_exist']})

    try:
        query = db_session.query(Device).filter(
            Device.ID == deleted_device_id).delete()
        db_session.commit()
    except:
        return jsonify({'code': responseCode['uninstall']})
    finally:
        db_session.close()

    return jsonify({'code': responseCode['success']})


@device.route("/list", methods=["POST"])
@login_required
def getAllDevices():
    db_session = sessionmaker(bind=bs_db)()
    room_id = request.values.get('roomid')
    print(room_id)
    # 这一段是只返回 [{device_id, device_type}] 的
    query = db_session.query(Room).filter(Room.ID == room_id).all()
    if not query:
        return jsonify([{'code': responseCode['room_doesnot_exist']}])
    query = db_session.query(Device).filter(Device.roomID == room_id).all()
    device_list = []
    for d in query:
        typename=""
        if d.type == 0:
            typename = "light"
        elif d.type == 1:
            typename = "sensor"
        elif d.type == 2:
            typename = "switch"
        elif d.type == 3:
            typename = "lock"
        device_list.append({
            'id': d.ID,
            'type':d.type,
            'name':d.name,
            'info':d.info,
            'posx':d.posx,
            'posy':d.posy,
            'info':d.info,
            'type_content':typename
        })
    db_session.close()
    return jsonify({'code':responseCode["success"],'data': device_list})


@device.route("/update/info", methods=["POST"])
@login_required
def updateDeviceInfo():

    db_session = sessionmaker(bind=bs_db)()

    data = request.get_json();

    print(data)

    device_id = data.get('id')
    device_info = data.get('info')

    if device_id is None or device_info is None:
        db_session.close()
        return jsonify([{'code': responseCode['error']}])

    query = db_session.query(Device).filter(
        Device.ID == device_id).all()

    if not query:
        db_session.close()
        return jsonify({'code': responseCode['device_doesnot_exist']})
    else:
        db_session.query(Device).filter(Device.ID == device_id).update(
            {'info': device_info})
        db_session.commit()

    db_session.close()
    return jsonify({'code': responseCode['success']})
@device.route("/update/pos", methods=["POST"])
@login_required
def updateDevicePos():

    db_session = sessionmaker(bind=bs_db)()

    device_id = request.values.get('id')
    device_pos_x = request.values.get('pos_x')
    device_pos_y = request.values.get('pos_y')

    print(device_id, device_pos_x, device_pos_y)

    if device_id is None:
        db_session.close()
        return jsonify({'code': responseCode['error']})

    query = db_session.query(Device).filter(
        Device.ID == device_id).all()

    if not query:
        db_session.close()
        return jsonify({'code': responseCode['device_doesnot_exist']})
    else:
        db_session.query(Device).filter(Device.ID == device_id).update({
            'posx':
            device_pos_x,
            'posy':
            device_pos_y
        })
        db_session.commit()

    db_session.close()
    return jsonify({'code': responseCode['success']})


@device.route("/update/name", methods=["POST"])
@login_required
def updateDeviceName():
    db_session = sessionmaker(bind=bs_db)()

    device_id = request.values.get('id')
    device_name = request.values.get('name')

    print("in /device/update/name " + device_id + " " + device_name)


    if device_id is None:
        db_session.close()
        return jsonify({'state': responseCode['error']})

    query = db_session.query(Device).filter(
        Device.ID == device_id).all()

    if not query:
        db_session.close()
        return jsonify({'state': responseCode['device_doesnot_exist']})
    else:
        db_session.query(Device).filter(Device.ID == device_id).update({
            'name': device_name
        })
        db_session.commit()

    db_session.close()
    return jsonify({'state': responseCode['success']})