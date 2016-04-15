from functools import wraps
from flask import request, Response
from public import datamanager
from public import website
import flask.ext.login as flask_login


login_manager = flask_login.LoginManager()
login_manager.init_app(website)


def sign_in(username, password):

    # create an empty user object
    user = User()

    # get the user's info from the database
    query_string = (
      'SELECT user_id, username, first_name, last_name ' 
      'FROM users '
      'WHERE username = "tanya" '
      'AND password = "test"'
    )

    query_result = datamanager.query_db(query_string, [], one=True)

    # if the details were wrong print nope
    print("user details incorrect")

    # apply the loaded details to the user object
    user.id = query_result['user_id']
    user.username = query_result['username']
    user.first_name = query_result['first_name']
    user.last_name = query_result['last_name']

    # start a session for the user
    flask_login.login_user(user)




def sign_out():
    flask_login.logout_user()




# doesn't appear to work
def current_user():
    return flask_login.current_user






class User(flask_login.UserMixin):

    id = 0
    username = None
    first_name = None
    last_name = None

    def __init__(self):
        pass




@login_manager.user_loader
def user_loader(username):

    query_string = (
      'SELECT user_id, username, first_name, last_name ' 
      'FROM users '
      'WHERE username = "tanya" '
      'AND password = "test"'
    )

    query_result = datamanager.query_db(query_string, [], one=True)

    if query_result == Null:
        return

    user = User()
    user.id = query_result['user_id']
    user.username = query_result['username']
    user.first_name = query_result['first_name']
    user.last_name = query_result['last_name']

    return user


'''
@login_manager.request_loader
def request_loader(request):
    #user_id = request.form.get('user_id')
    #if email not in users:
    #    return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = False #request.form['pw'] == users[email]['pw']

    return user
'''





'''def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print("hello")
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
    '''


















'''
returns true if the username and password
combination exist in the database
'''
def check_auth(username, password):

    query_string = (
      'SELECT username, password ' 
      'FROM users '
      'WHERE username = "tanya" '
      'AND password = "test"'
    )

    query_result = datamanager.query_db(query_string, [], one=True)

    if query_result["username"] == username and query_result["password"] == password:
        auth_successful = True
    else:
        auth_successful = False

    return auth_successful




'''
def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})



def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
'''