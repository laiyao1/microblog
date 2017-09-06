# -*- coding: utf-8 -*-
from flask import render_template
from app import app,login_manager,db
from app.models import User
from app.forms import LoginForm
from flask import flash,request,session
from flask import redirect
from flask_login import login_required,login_user,logout_user

#user = { 'nickname' : 'Miguel' }
user_now = {'nickname':'Guest'}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
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
    print(session.get('nickname'))
    return render_template("index.html",user = session.get('nickname'),posts= posts)

@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #user_now['nickname'] = form.name.data
        user = User.login_check(form.name.data)
        if user:
            login_user(user)
            #print(type(user))
            session['nickname'] = form.name.data
            #try:
            #    db.session.add(user)
            #    db.session.commit()
            #except:
            #    flash("The database error!")
            #    return redirect('/login')
            flash('Login requested for Name: '+form.name.data)
            flash('passwd: '+str(form.password.data))
            flash('remember_me: '+str(form.remember_me.data))
            #print("form ok!")
            #测试post-重定向-get技巧
            #不使用重定向时,将action='/index',最后一次操作是POST,每次刷新网页都会出现提示信息
            return redirect(request.args.get('next') or '/index')
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')
    return render_template("login.html",form = form)

#def logout_user():
#    user_now['nickname']='Guest'

@app.route('/logout')
def logout():
    logout_user()
    session.pop('nickname')
    flash('You have been logged out.')
    return redirect('/index')


@app.route('/secret')
@login_required
def secret():
    return render_template("secret.html")
