# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'Miguel' }
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Ths Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",user = user,posts= posts)

