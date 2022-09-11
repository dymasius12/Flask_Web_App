from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# create the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    # Make the secret key to make the website encrypted
    app.config['SECRET_KEY'] = 'hello hello world world'
    # configure the database into the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

   
    #registering the views root
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # just importing the models
    from .models import User, Note
    #run the create_database function below
    create_database(app)

    # Use the login manager to tell if you have not login where to redirect?
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # This is just telling flask how we load a user. same as filtered by but instead use primary key.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

#check if the database has existed or not
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')