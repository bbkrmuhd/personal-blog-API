import os
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Config:
    BLOG_ADMIN = os.environ.get('BLOG_ADMIN')
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or 60 * 60 * 24 * 7
    JWT_COOKIE_SECURE = True
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    UPLOADED_PHOTOS_DEST = os.path.join(str(BASE_DIR / 'static/img'))
    S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
    S3_LOCATION = os.environ.get("S3_LOCATION")


    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'test.db')


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')


config = {
    'testing': TestConfig,
    'development': DevConfig,
    'production': ProdConfig
}
