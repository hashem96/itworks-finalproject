# __init__.py
import flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db  = SQLAlchemy()
migrate = Migrate()
login_mgr = LoginManager()


app = flask.Flask(__name__) # __name__ is the name of the folder
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)
login_mgr.init_app(app)

from . import views, models

@app.shell_context_processor
def shell_ctx():
    return {
        "models":models,
        "User": models.User,
        "Product" : models.Product,
        "app": app,
        "db": db
    }

@login_mgr.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)


