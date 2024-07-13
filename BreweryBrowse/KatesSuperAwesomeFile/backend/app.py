import os
from flask import (
    Flask
)
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager
)
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from models import db, connect_db
from routes.breweries import breweries_bp
from routes.brewery import brewery_bp

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "postgresql:///breweries",
)
app.config["SCHEDULER_API_ENABLED"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config["SECRET_KEY"] = os.getenv("secret_key")

toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(breweries_bp)
app.register_blueprint(brewery_bp)

connect_db(app)
with app.app_context():
    db.create_all()
    db.session.commit()