#-*- coding:utf-8 -*-

from app import db
from flask_login import UserMixin
from  . import login_manager


ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique=True)
    email = db.Column(db.String(120), unique=True, index = True)
    role =db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @classmethod
    def login_check(cls,user_name):
        user = cls.query.filter(db.or_(User.nickname == user_name, User.email == user_name)).first()
        if not user:
            return None
        return user


    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
