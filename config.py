__author__ = 'hanyuen'

import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "hano"
    SQLALCHEMY_DATABASE_URI= os.environ["POSTGRES_DATABASE_URL"]


class DevelopmentConfig(BaseConfig):
    DEBUG = True

