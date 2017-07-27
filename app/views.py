# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.forms import LoginForm
from flask import flash
from flask import redirect


user = { 'nickname' : 'Miguel' }

@app.route('/')
@app.route('/index')
def index():
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

@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user['nickname'] = form.name.data
        flash('Login requested for Name: '+form.name.data)
        flash('passwd: '+str(form.password.data))
        flash('remember_me: '+str(form.remember_me.data))
        #print("form ok!")
        return redirect('/index')
    #print("form wrong!")
    return render_template("login.html",form = form)
