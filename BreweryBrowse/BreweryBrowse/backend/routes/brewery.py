from flask import (
    Blueprint,
    request,
    jsonify
)
from sqlalchemy.exc import IntegrityError
from models import db, Breweries
from ..apiClient import get_single_brewery

brewery_bp = Blueprint("brewery", __name__, url_prefix="/brewery")

def get_brewery():
    data = request.json
    id = data.get("id")
    return jsonify(get_single_brewery(id))