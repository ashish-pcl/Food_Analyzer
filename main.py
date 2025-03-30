import sys
import os

# Ensure the project root is in the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask
from flask_cors import CORS
from src.api.routes import init_routes
from src.config.dev_config import DevConfig
from src.utils.logging import configure_logging

def create_app(config_class=DevConfig):
    app = Flask(__name__, static_folder="../static", template_folder="templates")
    app.config.from_object(config_class)
    
    CORS(app)
    
    configure_logging()
    
    init_routes(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
