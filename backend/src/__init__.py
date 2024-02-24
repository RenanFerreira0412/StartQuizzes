from flask import Flask
from flask_cors import CORS

from .api.public.auth import auth_bp
from .api.authenticated.user import user_bp
from .api.authenticated.quiz import quiz_bp


def create_app():
    app = Flask(__name__)

    CORS(app)

    # registrando os blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(quiz_bp)

    return app
