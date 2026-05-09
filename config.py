import os

class Config:
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/taskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
