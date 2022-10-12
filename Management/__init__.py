from flack import Flack



def create_app(): 
    app=Flask(__name__)

    from . import views
    app.register_blueprint(views.mainbp)

    return app