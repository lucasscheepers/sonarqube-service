import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    VERSION = os.getenv('VERSION')


class DevelopmentConfig(Config):
    SONARQUBE_API = os.getenv('SONARQUBE_API_DEV')
    SONARQUBE_TOKEN = os.getenv('SONARQUBE_TOKEN_DEV')
    LOGGING_LEVEL = 'DEBUG'
    DEBUG = True


class TestingConfig(Config):
    SONARQUBE_API = os.getenv('SONARQUBE_API_TEST')
    SONARQUBE_TOKEN = os.getenv('SONARQUBE_TOKEN_TEST')
    LOGGING_LEVEL = 'DEBUG'
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    SONARQUBE_API = os.getenv('SONARQUBE_API_PROD')
    SONARQUBE_TOKEN = os.getenv('SONARQUBE_TOKEN_PROD')
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL')
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

CONFIG = config_by_name['prod']
