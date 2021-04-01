import configparser
import os

basedir = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = "{}/setting.secret.ini".format(basedir)
config = configparser.ConfigParser()
config.sections()
config.read(CONFIG_FILE)

# MySQL
MYSQL_HOST = config.get("mysql", "host")
MYSQL_PORT = config.get("mysql", "port")
MYSQL_DB = config.get("mysql", "db")
MYSQL_USER = config.get("mysql", "user")
MYSQL_PASSWORD = config.get("mysql", "password")

# Redis
REDIS_HOST = config.get("redis", "host")
REDIS_PORT = int(config.get("redis", "port"))
REDIS_DB = int(config.get("redis", "db"))
REDIS_TTL = int(config.get("redis", "ttl"))

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

# App config
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)

# Time config
FULL_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
