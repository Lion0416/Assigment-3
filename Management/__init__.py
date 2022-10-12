from flack import Flack
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def create_app(): 
    app=Flask(__name__)
    app.debug = True
    app.secret_key="12345"
    db.init_app(app)

    bootstrap = Bootstrap5(app)

    login_manager = LoginManager()

    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    from . import views
    app.register_blueprint(views.bp)

    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
    