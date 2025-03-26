from src.config.base_config import Config

class ProdConfig(Config):
    DEBUG = False
    ENV = "production"
