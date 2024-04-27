from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.views import views
from website.auth import auth

db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bam adebayo'  # secret key for the app, no matter
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # we are saying that our SQLALCHEMY DB is located at ...
db.init_app(app)


app.register_blueprint(views, url_prefix='/views')
app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)  # debug=True means that every time we change the code, the server get a refresh,
    # so we don't have to rerun manually
