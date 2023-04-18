from flask import Blueprint, request, jsonify
from src.models import Room, Place
from sqlalchemy.orm import sessionmaker
from src.database import bs_db
from src.util import responseCode, login_required

room = Blueprint('room', __name__)


@room.route("/create", methods=["POST"])
@login_required
def createRoom():
    """
    createRoom: create new room for specified scene
    
    input: scene_id & room_name
    
    output:
        state: 0 - success + new roomId
               6 - failed: scene doesn't exist
    
    """
    DBsession = sessionmaker(bind=bs_db)()
    name = request.values.get('name')
    placeID = request.values.get('placeid')
    img_src = request.values.get('img')
    print(placeID)
    # check the existence of 'scene'
    query = DBsession.query(Place).filter(Place.ID == placeID).all()
    roomID = 0
    if query:
        # add new room
        newRoom = Room()
        newRoom.name = name
        newRoom.placeID = placeID
        DBsession.add(newRoom)


        # get new roomId
        roomID = 0
        query = DBsession.query(Room).filter(Room.placeID == placeID).filter(
            Room.name == name).order_by(Room.ID.desc()).all()
        for i in query:
            roomID = i.ID
            break

        DBsession.commit()
        DBsession.close()

        # return success & new room id
        return jsonify({
            'code': responseCode['success'],
            'info': {
                'id': roomID,
                'name': name
            }
        })
    else:
        DBsession.close()
        # scene doesn't exist
        return jsonify({'state': responseCode['scene_doesnot_exist']})


@room.route("/remove", methods=["POST"])
@login_required
def removeRoom():
    """
    
    deleteScene: delete exist room
    
    input: id
    
    return: 0 - success
            8 - room doesn't exist
    
    """

    DBsession = sessionmaker(bind=bs_db)()

    ID = request.values.get('id')

    # check the existence of 'room'
    query = DBsession.query(Room).filter(Room.ID == ID).all()

    if query != []:

        # delete room
        query = DBsession.query(Room).filter(Room.ID == ID).delete()

        # return 'success'
        DBsession.commit()
        DBsession.close()

        return jsonify({'state': responseCode['success']})
    else:
        DBsession.close()
        # room doesn't exist
        return jsonify({'state': responseCode['room_doesnot_exist']})


@room.route("/list", methods=["POST"])
# @login_required
def listRooms():
    """
        
    getAllScenes: select all rooms by scene_id
    
    input: scene_id
    
    return: [{room_id, room_name}]
    
    """

    DBsession = sessionmaker(bind=bs_db)()
    # print(request.get_data(as_text=True))

    placeID = request.values.get('placeid')
    if not placeID:
        DBsession.close()
        return jsonify({'state': responseCode['invalid_args']})

    query = DBsession.query(Room).filter(Room.placeID == placeID).all()

    res = []
    for i in query:
        res.append({'id': i.ID, 'name': i.name, 'img':i.img_src})
    DBsession.close()
    return jsonify({'data':res})


@room.route("/changeimg", methods=["POST"])
@login_required
def updateImage():
    DBsession = sessionmaker(bind=bs_db)()

    ID = request.values.get("roomid")
    new_img = request.values.get("new_img")

    # print("now in changeimg roomid:" + ID + " new_img:" +new_img)
    print("now in changeimg roomid:" )
    print(ID)
    print(new_img)

    if ID is None or new_img is None:
        DBsession.close()
        return jsonify([{'code': responseCode['error']}])

    query = DBsession.query(Room).filter(Room.ID == ID).all()

    if not query:
        DBsession.close()
        return jsonify({'code': responseCode['scene_doesnot_exist']})
    else:
        DBsession.query(Room).filter(Room.ID == ID).update(
            {'img_src': new_img})
        DBsession.commit()

    DBsession.close()
    return jsonify({'code': responseCode['success']})

@room.route("/changename", methods=["POST"])
@login_required
def updateName():
    DBsession = sessionmaker(bind=bs_db)()

    ID = request.values.get("id")
    new_name = request.values.get("new_name")

    if ID is None or new_name is None:
        DBsession.close()
        return jsonify([{'state': responseCode['error']}])

    query = DBsession.query(Room).filter(Room.ID == ID).all()

    if not query:
        DBsession.close()
        return jsonify({'state': responseCode['scene_doesnot_exist']})
    else:
        DBsession.query(Room).filter(Room.ID == ID).update(
            {'name': new_name})
        DBsession.commit()

    DBsession.close()
    return jsonify({'state': responseCode['success']})