from flask import g
from flask import render_template
from public import website
from public import datamanager


# home/index page
@website.route('/')
def index():
    
    query_string = 'select * from messages'
    query_results = datamanager.query_db(query_string, [], one=False)

    return render_template('index.html', messages=query_results)


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