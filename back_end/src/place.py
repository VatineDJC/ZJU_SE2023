from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import sessionmaker

from src.database import bs_db
from src.models import Place, User
from src.util import responseCode, login_required

place = Blueprint('scene', __name__)


@place.route("/create", methods=["POST"])
@login_required
def createPlace():
    DBsession = sessionmaker(bind=bs_db)()
    name = request.values.get('name')
    userID = session.get('ID')
    description = request.values.get('description')
    query = DBsession.query(User).filter(User.ID == userID).all()

    if query:
        newPlace = Place()
        newPlace.name = name
        newPlace.userID = userID
        newPlace.description = description

        DBsession.add(newPlace)
        placeID = 0
        placename = newPlace.name

        query = DBsession.query(Place).filter(Place.userID == userID).filter(
            Place.name == name).order_by(
            Place.ID.desc()).all()
        for i in query:
            placeID = i.ID
            break

        DBsession.commit()
        DBsession.close()

        return jsonify({
            'code': responseCode['success'],
            'info': {
                'id': placeID,
                'name': placename
            }
        })
    else:
        DBsession.close()
        return jsonify({'state': responseCode['user_doesnot_exist']})


@place.route("/remove", methods=["POST"])
@login_required
def deletePlace():
    DBsession = sessionmaker(bind=bs_db)()
    placeID = request.values.get('id')
    query = DBsession.query(Place).filter(Place.ID == placeID).all()
    if query:
        DBsession.query(Place).filter(Place.ID == placeID).delete()
        DBsession.commit()
        DBsession.close()
        return jsonify({'code': responseCode['success']})
    else:
        DBsession.close()
        return jsonify({'code': responseCode['scene_doesnot_exist']})


@place.route("/list", methods=["GET", "POST"])
@login_required
def listPlace():
    DBsession = sessionmaker(bind=bs_db)()
    userID = session.get('ID')
    print(userID)
    if not userID:
        DBsession.close()
        return jsonify({'state': responseCode['invalid_args']})

    places = DBsession.query(Place).filter(Place.userID == userID).all()
    res = []
    for p in places:
        scene_info = {
            'id': p.ID,
            'name': p.name
        }
        res.append(scene_info)
    DBsession.close()
    return jsonify({'data': res})


@place.route("/modifyinfo", methods=["POST"])
@login_required
def updatePlaceInfo():
    DBsession = sessionmaker(bind=bs_db)()

    ID = request.values.get("id")
    new_name = request.values.get("name")
    new_description = request.values.get("description")

    if ID is None:
        DBsession.close()
        return jsonify([{'code': responseCode['error']}])

    if new_name is None and new_description is None:
        DBsession.close()
        return jsonify([{'code': responseCode['error']}])

    query = DBsession.query(Place).filter(Place.ID == ID).all()

    if not query:
        DBsession.close()
        return jsonify({'code': responseCode['scene_doesnot_exist']})
    else:
        if not new_name is None:
            DBsession.query(Place).filter(Place.ID == ID).update(
                {'name': new_name})
        if not new_description is None:
            DBsession.query(Place).filter(Place.ID == ID).update(
                {'description': new_description})
        DBsession.commit()

    DBsession.close()
    return jsonify({'code': responseCode['success']})


@place.route("/getinfo", methods=["POST"])
@login_required
def getPlaceInfo():
    DBsession = sessionmaker(bind=bs_db)()

    ID = request.values.get("placeid")

    if ID is None:
        DBsession.close()
        return jsonify([{'code': responseCode['error']}])

    query = DBsession.query(Place).filter(Place.ID == ID).all()

    if not query:
        DBsession.close()
        return jsonify({'code': responseCode['scene_doesnot_exist']})

    DBsession.close()
    return jsonify({'code': responseCode['success'], "name": query[0].name, "description": query[0].description})
