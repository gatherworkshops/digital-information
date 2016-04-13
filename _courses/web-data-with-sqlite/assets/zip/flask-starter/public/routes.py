from flask import g
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from public import website
from public import datamanager


# User web pages

@website.route('/')
def index():
    return 'Home page'


@website.route('/login')
def login():
    return render_template('login.html')




'''
The upload method handles the uploading of new images.
Initially an upload form is shown. When submitted, it
processes the image and then redirects to the home page.
'''
@website.route('/upload', methods=['GET', 'POST'])
def upload():

    # upload page
    if request.method == 'GET':

        return render_template('upload.html')

    # upload successful
    if request.method == 'POST':

        uploaded_data = {
            "image": request.form['image'],
            "caption": request.form['caption']
        }

        return redirect(url_for('index'))

    




@website.route('/users/<user_id>')
def profile(user_id):
    return 'User profile page'




# API Pages

@website.route('/api/posts')
def posts():

    raw_data = g.db.execute('select * from test')
    results = raw_data.fetchall()
    posts = []

    for row in results:
        post = {
            'one': row[0],
            'two': row[1]
        }
        posts.append('hi')

    #posts = [dict(title=row[0], text=row[1]) for row in raw_data.fetchall()]

    view = 'hi' + str(len(posts))

    return view

