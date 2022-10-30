from flask import Flask 
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()


def create_app(): 
    app=Flask(__name__)
    app.debug = True
    app.secret_key="12345"

    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///eventManagement.sqlite'

    #initialize db with flask app
    db.init_app(app)

    #we use this utility module to display forms quickly
    bootstrap = Bootstrap5(app)

    #initialize the login manager
    login_manager = LoginManager()


    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from . import views
    app.register_blueprint(views.mainbp)
 
    from . import event
    app.register_blueprint(event.bp)

    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
    