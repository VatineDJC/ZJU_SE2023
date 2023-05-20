from random import randint, random
from flask import Blueprint, request, jsonify
from src.models import Picture,Item
from sqlalchemy.orm import sessionmaker
from src.database import bs_db
from src.util import responseCode, login_required
import os, calendar, time
from PIL import Image
import io

files = Blueprint('files', __name__)


@files.route('/upload', methods=['POST'])
def send_file():
    db_session = sessionmaker(bind=bs_db)()

    file = request.files.get('file')
    itemID = request.values.get('itemID')
    if file is None :
        return jsonify({'state': responseCode['error']})

    file_name = file.filename
    suffix = os.path.splitext(file_name)[-1]
    basePath = os.path.dirname(__file__)
    nowTime = calendar.timegm(time.gmtime())
    upload_path = os.path.join(basePath, '../upload', str(nowTime))
    upload_path = os.path.abspath(upload_path)
    print(upload_path)
    file.save(upload_path + str(nowTime) + suffix)
    save_file_name = str(nowTime) + str(nowTime) + suffix

    pic = Picture()
    pic.path = save_file_name
    pic.itemID = itemID

    db_session.add(pic)
    db_session.flush()  # 刷新会话以获取新记录的主键值
    ID = pic.ID
    db_session.commit()

    query = db_session.query(Picture).filter(Picture.ID == ID).all()

    if query:
        return jsonify({'code': responseCode['success'], 'file_name': save_file_name})
    else:
        return jsonify({'code': responseCode['error']})


@files.route('/download', methods=['GET', 'POST'])
def get_layout():
    # try:
    print("in download")
    file_name = request.args['file_name']
    if not file_name:
        return jsonify({'state': responseCode['error']})
    print(file_name)


    basePath = os.path.dirname(__file__)
    upload_path = os.path.join(basePath, '../upload', file_name)
    upload_path = os.path.abspath(upload_path)

    layout_path = os.path.abspath(upload_path)
    image = open(layout_path, 'rb').read()
    image = io.BytesIO(image)
    image = Image.open(image)

    image_byte_arr = io.BytesIO()
    image.save(image_byte_arr, format='PNG')
    image_byte_arr = image_byte_arr.getvalue()

    return image_byte_arr


