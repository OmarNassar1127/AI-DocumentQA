# __init__.py

from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object('config.settings')

    # Set the secret key
    app.secret_key = os.environ.get('SECRET_KEY')

    # Register Blueprints
    from app.controllers.chat_controller import chat_bp
    from app.controllers.pdf_controller import pdf_bp
    app.register_blueprint(chat_bp)
    app.register_blueprint(pdf_bp)

    return app