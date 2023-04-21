from os import urandom
from flask import Flask
from src.account import account
from src.item import item
from src.order import order
from src.picture import picture
# from src.place import place
# from src.room import room
# from src.device import device
# from src.files import files

app = Flask(__name__)
app.secret_key = urandom(32)

app.register_blueprint(account, url_prefix='/user')
app.register_blueprint(item, url_prefix='/item')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(picture, url_prefix='/picture')
# app.register_blueprint(place, url_prefix='/place')
# app.register_blueprint(device, url_prefix='/device')
# app.register_blueprint(room, url_prefix='/room')
# app.register_blueprint(files, url_prefix='/files')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=8886,
        host="0.0.0.0"
    )