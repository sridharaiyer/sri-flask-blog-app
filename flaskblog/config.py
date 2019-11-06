import os
import json

with open('/etc/sri-flask-blog-app-config.json') as config_file:
    config = json.load(config_file)


class Config:
    """docstring for Config."""

    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('SRI_GOOGLEAPI_USER')
    MAIL_PASSWORD = config.get('SRI_GOOGLEAPI_PWD')
