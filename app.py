from flask import Flask

from telebot import TeleBot

from flask_sqlalchemy import SQLAlchemy


from FreeKassa import FK

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///main.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

kassa = FK()

bot = TeleBot('982289200:AAGs-xuy7PHgsEXDQui4uFATxgOpKHtMlSw')

admins = [865473632]

WEBHOOK_URL = f''
WEBHOOK_LISTEN = ''
WEBHOOK_PORT = 
