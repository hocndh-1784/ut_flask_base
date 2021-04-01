from settings.common import *

# SQLAlchemy override
SQLALCHEMY_DATABASE_URI = "mysql://test:123123@ip:3306/db_name"

# Redis override
REDIS_DB = 0
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_TTL = 60
