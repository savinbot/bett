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

bot = TeleBot('772665816:AAEOQNDmXFd5CHUMX__N6x8m9ErvUtt8r_M')

admins = [435600486, 631997243, 686676371, 647599306, 738551202, 796269232]

WEBHOOK_URL = f''
WEBHOOK_LISTEN = ''
WEBHOOK_PORT = 