class Config(object):
    TESTING = False


class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    SECRET_KEY = "asdfaweava233423o4u234023482309j2039dj2039du203ur2309r234092340239j"
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://demo_user:demo_password@localhost:5432/demo_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0


class TestingConfig(Config):
    DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
