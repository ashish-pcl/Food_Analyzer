from src.config.base_config import Config

class DevConfig(Config):
    DEBUG = True
    ENV = "development"
