from public import website
from public import datamanager
from flask.ext import login as flask_login
from flask.ext.login import login_required




login_manager = flask_login.LoginManager()
login_manager.init_app(website)

# Change this!
website.secret_key = 'super secret string'  




'''
We must have a user class for the flask login
plugin to work correctly. Our User class extends
the flask login class UserMixin which gives it
all the properties and functions it needs
behind the scenes.
'''
class User(flask_login.UserMixin):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.authenticated = False

    # Return the email address to satisfy Flask-Login's requirements.
    def get_id(self):
        return self.username

    # Return True if the user is authenticated
    def is_authenticated(self):
        return self.authenticated

    # All registered users are active
    def is_active(self):
        return True

    # Our app doesn't support anonymous users
    def is_anonymous(self):
        return False

    




'''
It should return None (not raise an exception) 
if the ID is not valid. 
(In that case, the ID will manually be removed 
from the session and processing will continue.)
'''
@login_manager.user_loader
def load_user(username):

    # 1. Fetch against the database a user by their username 
    query_string = (
      'SELECT user_id, username, password, first_name, last_name ' 
      'FROM users '
      'WHERE username = ?'
    )

    query_result = datamanager.query_db(query_string, [username], one=True)

    if query_result == None:
        return

    # 2. Create a new object of `User` class and return it.
    user = User(
        query_result['username'],
        query_result['password']
    )

    user.authenticated = True

    return user





'''
returns true if the username and password
combination exist in the database
'''
def sign_in_user(username, password):

    user = User(username, password)
    flask_login.login_user(user)

    return flask_login.current_user




'''
signs out the current user
'''
def sign_out_user():
    flask_login.logout_user()

    

