from flask import (
    Blueprint
)
from sqlalchemy.exc import IntegrityError
from models import db, Breweries
from ..apiClient import get_breweries_list

breweries_bp = Blueprint("breweries", __name__, url_prefix="/breweries")

def get_breweries_list():
    get_breweries_list()