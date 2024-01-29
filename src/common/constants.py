import os


class Configuration:

    PORT = int(os.getenv("PORT", 3000))
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
    MONGODB_URL = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000"
