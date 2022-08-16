from flask import Flask
from api.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate
from .user.views import user_namespace
from .task.views import task_namespace
from .auth.views import auth_namespace





db = SQLAlchemy()
migrate = Migrate()



def create_app():    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from api.models import models
    
    migrate.init_app(app, db)
    
    api = Api(app)
    api.add_namespace(user_namespace , path="/user")
    api.add_namespace(task_namespace, path="/task")
    api.add_namespace(auth_namespace, path="/auth")
    
    return app
  
    
app = create_app()


# db.create_all()
# db.drop_all()


    
    