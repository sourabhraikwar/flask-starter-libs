class Config(object):
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    
    SECRET_KEY = 'asdfaweava233423o4u234023482309j2039dj2039du203ur2309r234092340239j'
    DATABASE_URI = "sqlite:////tmp/primary.db"

class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True