from flask import Flask
from flask_cors import CORS
from src.api.routes import init_routes
from src.config.dev_config import DevConfig
from src.utils.logging import configure_logging

def create_app(config_class=DevConfig):
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    
    # Configure logging
    configure_logging()
    
    # Register routes
    init_routes(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
