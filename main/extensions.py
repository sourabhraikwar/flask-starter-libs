from flask_migrate import Migrate
from flask_redis import Redis
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
redis = Redis()
