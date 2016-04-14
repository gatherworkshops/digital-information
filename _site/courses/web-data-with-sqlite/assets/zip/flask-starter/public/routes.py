from flask import g
from public import website
from public import datamanager


# home/index page
@website.route('/')
def index():
    return 'Home page'


