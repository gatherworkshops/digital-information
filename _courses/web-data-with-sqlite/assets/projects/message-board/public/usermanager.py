import sqlite3
from public import website
from flask.ext import login as flask_login

login_manager = flask_login.LoginManager()
login_manager.init_app(website)

# Our mock database.
users = {'foo@bar.tld': {'pw': 'secret'}}

website.secret_key = 'super secret string'  # Change this!

class User(flask_login.UserMixin):
    pass



'''
It should return None (not raise an exception) 
if the ID is not valid. 
(In that case, the ID will manually be removed 
from the session and processing will continue.)
'''
@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user