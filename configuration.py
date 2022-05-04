import os
class Configuration:
  APP_MONGO_DB = os.environ.get("APP_MONGO_DB", "db")
  APP_MONGO_URI = os.environ.get("APP_MONGO_URI", "mongodb://user:password@localhost/db")
  APP_DEBUG = os.environ.get("APP_DEBUG", "true").lower() == "true"
  APP_BASIC_AUTH_USERNAME = os.environ.get("APP_BASIC_AUTH_USERNAME", "username")
  APP_BASIC_AUTH_PASSWORD = os.environ.get("APP_BASIC_AUTH_PASSWORD", "password")