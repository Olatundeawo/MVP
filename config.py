import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '14b68302993485caa5809ccc'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
            or 'sqlite:///' + os.path.join(basedir, 'project.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
