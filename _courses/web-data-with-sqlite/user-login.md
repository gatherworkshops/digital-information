---
title: User Login

slides:

  - class: title-slide
    content: |

      # User Login
      _Authenticating users_




  - content: |

      ## Setting up Flask-Login

      This plugin will make it super easy
      for us to log users in and out.


  - content: |

      ### Install the flask-login plugin

      ```bash
      pip install flask-login
      ```

      Python plugins need to be 
      installed from the shell.



  - content: |

      ### Ready for use

      We can now use it by importing the 
      **flask-login** package wherever we need.



  - content: |

      ### Create a usermanager file

      In your website's public folder,
      create a new file **usermanager.py**



  - content: |

      ### Import your website

      ```python
      from public import website
      ```

      Import your message-board Flask website
      at the top of your **usermanager.py** file.


  - content: |

      ### Import flask login

      ```python
      from public import website
      from flask.ext import login as flask_login
      ```

      Also import the **flask-login** plugin
      so we can use the additional functionality.


  - content: |

      ### Add a secret key

      ```python
      from public import website
      from flask.ext import login as flask_login

      website.secret_key = 'super secret string' 
      ```

      This is a requirement of flask-login
      which we need to avoid errors.


  - content: |

      ### Initialise flask login

      ```python
      from public import website
      from flask.ext import login as flask_login

      website.secret_key = 'super secret string' 

      login_manager = flask_login.LoginManager()
      login_manager.init_app(website)
      ```

      Create an instance of the login manager
      and pass it a reference to your web app.


  - content: |

      ### Check website works

      Open your website in the browser and
      click through pages to check they still work.

      Your site should work, with nothing changed.
      {:.checkpoint}







  - content: |

      ## Create a User class

      The flask-login plugin requires that we have
      a User class with a set of predefined functions.


  - content: |

      ### Create a User class

      ```python
      login_manager = flask_login.LoginManager()
      login_manager.init_app(website)

      class User(flask_login.UserMixin):

          def __init__(self, username, password):
              self.username = username
              self.password = password
              self.authenticated = False
      ```

      In your **user manager** after the login manager setup code, 
      create a **User** class which requires a username and password.


  - content: |

      ### Add a function to get the id

      ```python
      class User(flask_login.UserMixin):

          def __init__(self, username, password):
              self.username = username
              self.password = password
              self.authenticated = False

          def get_id(self):
              return self.username

      ```

      The flask-login plugin needs to be able to
      access a unique id for every user.


  - content: |

      ### Add a function to check authentication

      ```python
          def __init__(self, username, password):
              self.username = username
              self.password = password
              self.authenticated = False

          def get_id(self):
              return self.username

          def is_authenticated(self):
              return self.authenticated
      ```

      In our app, if we find a user in the database
      we assume they are authenticated so always return True.



  - content: |

      ### Add a function to check if a user is active

      ```python
          def __init__(self, username, password):
              self.username = username
              self.password = password
              self.authenticated = False
              
          def get_id(self):
              return self.username

          def is_authenticated(self):
              return self.authenticated

          def is_active(self):
              return True
      ```

      In our app, every user who exists can be treated
      as an "active" user, so always return true.


  - content: |

      ### Add a function to check if a user is anonymous

      ```python
      def get_id(self):
          return self.username

      def is_authenticated(self):
          return self.authenticated

      def is_active(self):
          return True

      def is_anonymous(self):
          return False

      ```

      Our app doesn't support anonymous users,
      so this function always returns False.

  - content: |

      ### Check your User class structure is correct


      ```python
      class User(flask_login.UserMixin):

          def __init__(self, username, password):
              self.username = username
              self.password = password
              self.authenticated = False

          def get_id(self):
              return self.username

          def is_authenticated(self):
              return self.authenticated

          def is_active(self):
              return True

          def is_anonymous(self):
              return False
      ```
      {:style="font-size:40%"}

      Your finished User class should look like this.
      {:.checkpoint}










  - content: |

      ## Create a user loader function

      The flask-login plugin also requires us to have a 
      function which can load a user based on their username.


  - content: |

      ### Create a dummy user loader function

      ```python
      @login_manager.user_loader
      def load_user(username):
          return None
      ```

      In your usermanager file, create a placeholder 
      function called load_user which returns None.

  - content: |

      ### Site should work

      Open your site in the browser and check
      that everything is still working.

      Your site should work, but still no change!
      {:.checkpoint}






  - content: |

      ## Restrict access to pages

      We can make certain pages of our site
      only accessible for logged in users.


  - content: |

      ### Import the "login required" mixin

      ```python
      from flask.ext.login import login_required
      ```

      In the usermanager import **login_required**, 
      a mixin we can apply to routes to restrict access.

  - content: |

      ### Import the user manager into routes

      ```python
      from public import usermanager
      ```

      This will allow us to use the **login_required** mixin
      and other functions we defined in the usermanager.


  - content: |

      ### Add "login required" to the new message page

      ```python
      @website.route('/new-message')
      @usermanager.login_required
      def new_message():
          return render_template('new-message.html')
      ```

      This tells Flask that login is required
      to access the new_message route.

  - content: |

      ### Check access is restricted

      Navigate to the new-message page in your browser
      to check that access is restricted.

      You should see an "Unauthorized" notice.
      {:.checkpoint}


  - content: |

      ### Set the login page

      ```python
      login_manager = flask_login.LoginManager()
      login_manager.init_app(website)

      login_manager.login_view = "sign_in"
      ```

      This tells the flask-login plugin where people
      should be sent if they are not logged in and
      try to access a restricted page.

  - content: |

      ### Check the login redirect works

      Try to navigate to the restricted "new message" page
      and check that you are redirected to the login page.

      Restricted pages should redirect to the login page.
      {:.checkpoint}














  - content: |

      ## Create function to sign in users

      This function in **usermanager** will take a 
      username and password, then return a signed in user.

  - content: |

      ### Add the "sign_in_user" function to usermanager

      ```python
      def sign_in_user(username, password):

          user = load_user(username)

          if user and user.password == password:
            user.authenticated = True
            flask_login.login_user(user)

          return flask_login.current_user
      ```

      This function creates an actual **User** object
      and logs that user in using **flask-login**.


  - content: |

      ### Check your app runs

      Run your website and click around
      to check for any new errors.

      Your website should run and be error-free.
      {:.checkpoint}






  - content: |

      ## Authenticate the user

      When the user signs in, we need to process the 
      username and password they entered in the form.


  - content: |

      ### Use the username and password to authenticate

      ```python
      if request.method == 'POST':

          username = request.form.get('username')
          password = request.form.get('password')

          user = usermanager.sign_in_user(username, password)
      ```

      Modify your sign-in route to pass the username 
      and password to the `sign_in_user` function.


  - content: |

      ### Redirect based on the result

      ```python
      if request.method == 'POST':

          username = request.form.get('username')
          password = request.form.get('password')

          user = usermanager.sign_in_user(username, password)

          if user.is_authenticated():
              return redirect('/')
          else:
              return render_template('sign-in.html')
      ```

      If the user exists, they will be authenticated
      and we can redirect them to the home page.

      If they don't exist, we keep them on the sign in page.


  - content: |

      ### Import the redirect package

      ```python
      from flask import redirect
      ```

      Import the redirect package
      at the top of **routes.py**

  - content: |

      ### Check your site works

      Everything should work as normal, except that
      signing in will always keep you on the sign in page.








  - content: |

      ## Implement the user loader function

      We have a function to load a user but it
      always returns None, it should return a user.


  - content: |

      ### Import the datamanager into the usermanager

      ```python
      from public import datamanager
      ```

      Import the data manager so that we can 
      access the database to look up a user.


  - content: |

      ### Write a query to find the user

      ```python
      @login_manager.user_loader
      def load_user(username):

          query_string = (
            'SELECT user_id, username, password, first_name, last_name ' 
            'FROM users '
            'WHERE username = ?'
          )
      ```

      The query is fairly straightforward, but we also
      included a question mark so we can pass in a username.


  - content: |

      ### Run the query, passing it the username parameter

      ```python
      @login_manager.user_loader
      def load_user(username):

          query_string = (
            'SELECT user_id, username, password, first_name, last_name ' 
            'FROM users '
            'WHERE username = ?'
          )

          query_result = datamanager.query_db(query_string, [username], one=True)
      ```


  - content: |

      ### If the query fails then return None

      ```python
      @login_manager.user_loader
      def load_user(username):

          query_string = (
            'SELECT user_id, username, password, first_name, last_name ' 
            'FROM users '
            'WHERE username = ?'
          )

          query_result = datamanager.query_db(query_string, [username], one=True)

          if query_result == None:
              return None
      ```


  - content: |

      ### If the query succeeds then create and return a User

      ```python
          query_result = datamanager.query_db(query_string, [username], one=True)

          if query_result == None:
              return None

          else:
              user = User(
                  query_result['username'],
                  query_result['password']
              )

              return user
      ```


  - content: |

      ### Attach the additional optional user info

      ```python
      query_result = datamanager.query_db(query_string, [username], one=True)

      if query_result == None:
          return None

      else:
          user = User(
              query_result['username'],
              query_result['password']
          )

          user.user_id = query_result['user_id']
          user.first_name = query_result['first_name']
          user.last_name = query_result['last_name']

          return user
      ```

      We can also store the user's user_id
      and their first and last name on the User.
      


  - content: |

      ### Site should be working

      Check your site is working
      and sign in is supported.

      You should be able to log in to your website.
      {:.checkpoint}


  - content: |

      ### Signing in should allow access to new messages

      Check that once you've signed in
      you can access the **new message** page.








  








  







  - content: |
      
      ## Sign out user

      Now we can also add functionality
      for a user to sign out.


  - content: |

      ### Create sign out route

      ```python
      # sign out page
      @website.route('/sign-out')
      def sign_out():
          return render_template('sign-out.html')
      ```


  - content: |

      ### Create sign_out_user function

      In usermanager.py:

      ```python
      def sign_out_user():
          flask_login.logout_user()
      ```

  - content: |

      ### Call sign out function from route

      ```python
      # sign out page
      @website.route('/sign-out')
      def sign_out():
          usermanager.sign_out_user()
          return render_template('sign-out.html')
      ```


  - content: |

      ### Test that you can sign in and sign out







  - content: |

      ## Password encryption
      
      You should totes encrypt passwords
      but we're not doing it today







  - content: |

      ## Using user data in templates

      We can display user data, or use their info
      to show and hide elements on a page.


  - content: |

      ### Displaying a username

      ```html
      {% if current_user.is_authenticated %}
          Hello {{ current_user.username }}
      {% endif %}
      ```

  - content: |

      ### Smart sign in / sign out links

      ```html
      <nav>

          <a href="/">Home</a>
          <a href="/new-message">New Message</a>

          {% if current_user.is_authenticated %}
            <a href="/sign-out">Sign out</a>
          {% else %}
            <a href="/sign-in">Sign in</a>
          {% endif %}

      </nav>
      ```







  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## User Login: Complete!

      [Take me to the next chapter!](authenticated-forms.html)


---