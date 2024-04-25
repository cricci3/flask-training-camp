from flask import Flask
from website.views import views
from website.auth import  auth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bam adebayo'  # secret key for the app, no matter

app.register_blueprint(views, url_prefix='/views')
app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)  # debug=True means that every time we change the code, the server get a refresh,
    # so we don't have to rerun manually
