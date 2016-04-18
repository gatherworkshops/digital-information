from public import website
from public import datamanager
from flask.ext import login as flask_login
from flask.ext.login import login_required

website.secret_key = 'super secret string' 

login_manager = flask_login.LoginManager()
login_manager.init_app(website)

login_manager.login_view = "sign_in"


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

    return None