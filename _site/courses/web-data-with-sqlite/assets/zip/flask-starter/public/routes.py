from flask import g
from flask import render_template
from public import website
from public import datamanager


# home/index page
@website.route('/')
def index():
    return render_template('index.html')


