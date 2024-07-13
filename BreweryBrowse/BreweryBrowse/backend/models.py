from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy(session_options={"expire_on_commit": False})

# class Breweries(db.Model):
#     __tablename__ = "breweries"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.Text, nullable=False)
#     brewery_type = db.Column(db.Text, nullable=True)
#     address_1 = db.Column(db.Text, nullable=True)
#     address_2 = db.Column(db.Text, nullable=True)
#     address_3 = db.Column(db.Text, nullable=True)
#     city = db.Column(db.Text, nullable=True)
#     state_province = db.Column(db.Text, nullable=True)
#     postal_code = db.Column(db.Ineger, nullable=True)
#     country = db.Column(db.Text, nullable=True)
#     longitude = db.Column(db.Integer, nullable=True)
#     latitude = db.Column(db.Integer, nullable=True)
#     phone = db.Column(db.Integer, nullable=True)
#     website_url = db.Column(db.Text, nullable=True)
#     state = db.Column(db.Text, nullable=True)
#     street = db.Column(db.Text, nullable=True)

# ############## CONNECT DB ##############


def connect_db(app):
    db.app = app
    db.init_app(app)