# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import *

app = Flask(__name__)
app.config.from_object('micblog.config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = '/login'
login_manager.init_app(app)

from app import views,models
