from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import User, Note
from .views import views
from .auth import auth
from os import path


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bam adebayo'  # secret key for the app, no matter
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # we are saying that our SQLALCHEMY DB is located at ...
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/views')
    app.register_blueprint(auth, url_prefix='/auth')

    create_database(app)

    return app


def create_database(app):
    # check if the db already exists otherwise create it
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
