from flask import Flask

from app.config import Config
from app.extensions import db, login_manager, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.auth.routes import auth
    from app.member.routes import member
    from app.admin.routes import admin

    app.register_blueprint(auth)
    app.register_blueprint(member)
    app.register_blueprint(admin)

    return app