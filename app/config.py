import os
basedir = os.path.abspath(os.path.dirname(__file__))
print ("basedir->", basedir)

class Config(object):
    EMAIL_LIST = []
    EMAIL_SERVER_LOGIN = ""
    EMAIL_SERVER_LOGIN_PASS = ""
    EMAIL_SENDER =  ""
    RESULTS_SIMPLE_FILE_PATH = os.path.join('app', 'static', 'results')
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev_tasker.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME_CONNECTION = os.path.join(os.getcwd(), 'app',  'dev_tasker.sqlite')
    ENV = 'development'
    COLOR_BACKGROUND_CLASS = "bg-primary"
    COLOR_TEXT_CLASS = "text-light"
    SERVER_ENV = "(Desarrollo)"

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_tasker.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME_CONNECTION = os.path.join(os.getcwd(), 'app', 'test_tasker.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COLOR_BACKGROUND_CLASS = "bg-warning"
    COLOR_TEXT_CLASS = "text-dark"
    SERVER_ENV = "(Testing)"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = ""
    DB_NAME_CONNECTION = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COLOR_BACKGROUND_CLASS = "bg-dark"

