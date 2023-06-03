from flask import Flask
from config import Config
from . extensions import db, bcrypt, LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    
    
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from project.models.users import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()
        
    return app
