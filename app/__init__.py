from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object('config.settings')

    # Register Blueprints
    from app.controllers.chat_controller import chat_bp
    from app.controllers.pdf_controller import pdf_bp
    app.register_blueprint(chat_bp)
    app.register_blueprint(pdf_bp)

    return app
