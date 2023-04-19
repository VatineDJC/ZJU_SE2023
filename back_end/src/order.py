from flask import Blueprint, request, jsonify, session
from src.models import Order
from sqlalchemy.orm import sessionmaker

from src.database import bs_db
from src.util import responseCode, login_required

order = Blueprint('order', __name__)

@order.route("/create", methods=["POST"])
@login_required
def createPlace():
    DBsession = sessionmaker(bind=bs_db)()