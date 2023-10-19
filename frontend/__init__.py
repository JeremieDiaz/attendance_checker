from flask import Flask

#I installed mysql-connector-python for the connection of database but i can't seem to get it connected.
#if the connection is not possible try sqlalchemy?

def create_app():
    app = Flask(__name__)
    app.secret_key = "checker"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

#this is connected to the views and auth.py files and it will pass it along to main hence why you must run main.