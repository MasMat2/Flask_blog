import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)
    
class Config:
    # app.config['SECRET_KEY'] = 'eae53a1856e74a4921707289b162f3d9'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')