from flask import g
from flask import render_template
from public import website
from public import datamanager


# home/index page
@website.route('/')
def index():
    
    messages = datamanager.query_db('select * from messages', [], one=False)
    print(messages)

    return render_template('index.html', messages=messages)


# new message page
@website.route('/new-message')
def new_message():
    return render_template('new-message.html')


# sign in page
@website.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')


# sign out page
@website.route('/sign-out')
def sign_out():
    return render_template('sign-out.html')