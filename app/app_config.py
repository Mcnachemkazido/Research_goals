from dotenv import load_dotenv
import os
load_dotenv()

class AppConfig:

    @staticmethod
    def get_host():
        if os.getenv("SQL_HOST"):
            return os.getenv("SQL_HOST")
        return False

    @staticmethod
    def get_port():
        if os.getenv("SQL_PORT"):
            return os.getenv("SQL_PORT")
        return False

    @staticmethod
    def get_user():
        if os.getenv("SQL_USER"):
            return os.getenv("SQL_USER")
        return False

    @staticmethod
    def get_password():
        if os.getenv("SQL_PASSWORD"):
            return os.getenv("SQL_PASSWORD")
        return False

    @staticmethod
    def get_db():
        if os.getenv("SQL_DB"):
            return os.getenv("SQL_DB")
        return False