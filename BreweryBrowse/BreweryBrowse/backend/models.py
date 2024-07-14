from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy(session_options={"expire_on_commit": False})

def connect_db(app):
    db.app = app
    db.init_app(app)