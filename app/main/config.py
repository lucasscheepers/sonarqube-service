import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
VERSION = os.getenv('VERSION')
SONARQUBE_API = os.getenv('SONARQUBE_API')
SONARQUBE_TOKEN = os.getenv('SONARQUBE_TOKEN')
