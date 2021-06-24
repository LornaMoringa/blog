import os

class Config:
    BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_GREEN_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
    
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
