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

    query_string = (
      'SELECT message_id, content, username, time_created ' 
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




# new message page
@website.route('/edit-message/<message_id>', methods=['GET', 'POST'])
@usermanager.login_required
def edit_message(message_id = None):

    if request.method == 'GET':

        query_string = (
            'SELECT message_id, content, user_id '
            'FROM messages '
            'WHERE message_id = ?'
        )

        query_result = datamanager.query_db(
            query_string, 
            [message_id],
            one=True
        )

        return render_template('edit-message.html', message=query_result)

    elif request.method == 'POST':

        message_content = request.form.get('message')
        message_id = request.form.get('message_id')

        query_string = (
          'UPDATE messages '
          'SET content = ? '
          'WHERE message_id = ?'
        )

        query_result = datamanager.query_db(
            query_string, 
            [message_content, message_id],
            one=True
        )

        print('result:', query_result)

        return redirect('/')



# sign in page
@website.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    if request.method == 'GET':
        return render_template('sign-in.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = usermanager.sign_in_user(username, password)

        if user.is_authenticated:
            return redirect('/')
        else:
            return render_template('sign-in.html')

    


# sign out page
@website.route('/sign-out')
def sign_out():
    usermanager.sign_out_user()
    return render_template('sign-out.html')



