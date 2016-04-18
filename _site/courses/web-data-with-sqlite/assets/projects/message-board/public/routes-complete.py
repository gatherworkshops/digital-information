from flask import g
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from public import website
from public import datamanager
from public import usermanager


# home/index page
@website.route('/')
def index():

    #if usermanager.login_manager.current_user.is_authenticated:
    #    print(usermanager.login_manager.current_user.id)

    query_string = (
      'SELECT content, username, time_created ' 
      'FROM messages INNER JOIN users '
      'USING (user_id) '
      'ORDER BY time_created DESC'
    )

    query_results = datamanager.query_db(query_string, [], one=False)

    for result in query_results:
        print(result)

    return render_template('index.html', messages=query_results)





# new message page
@website.route('/new-message')
@usermanager.login_required
def new_message():
    return render_template('new-message.html')




# sign in page
@website.route('/sign-in', methods=["GET", "POST"])
def sign_in():

    # sign in page
    if request.method == 'GET':

        return render_template('sign-in.html')


    # form submit handler
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        user = usermanager.sign_in_user(username, password)

        if user.is_authenticated:
            next_page = url_for('index')
        else:
            next_page = url_for('sign_in')

        return redirect(next_page)

    


# sign out page
@website.route('/sign-out')
def sign_out():

    usermanager.sign_out_user()

    return render_template('sign-out.html')



