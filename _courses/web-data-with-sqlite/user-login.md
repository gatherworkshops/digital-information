---
layout: chapter
title: User Login
slides:

  - class: title-slide
    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # User Login
      _Authenticating users_




  - content: |

      ## Flask Login Setup


  - content: |

      ### Install it

      pip install flask-login



  - content: |

      ### Ready for use

      We can now use it by importing the class wherever we need



  - content: |

      ### New file usermanager.py



  - content: |

      ### Import the flask website

      ```python
      from public import website
      ```


  - content: |

      ### Import flask login

      ```python
      from public import website
      from flask.ext import login as flask_login
      ```


  - content: |

      ### Add a secret key

      ```python
      from public import website
      from flask.ext import login as flask_login

      website.secret_key = 'super secret string' 
      ```


  - content: |

      ### Initialise flask login

      ```python
      from public import website
      from flask.ext import login as flask_login

      website.secret_key = 'super secret string' 

      login_manager = flask_login.LoginManager()
      login_manager.init_app(website)
      ```


  - content: |

      ### Check website works

      Click to all pages to see if they still work







  - content: |

      ## Implement required flask login stuff


  - content: |

      ### Add the user class to usermanager

      ```python
      class User(flask_login.UserMixin):

          def __init__(self, username, password):
              self.username = username
              self.password = password

          # Return the email address to satisfy Flask-Login's requirements.
          def get_id(self):
              return self.username

          # All existing users are authenticated
          def is_authenticated(self):
              return True

          # All registered users are active
          def is_active(self):
              return True

          # Our app doesn't support anonymous users
          def is_anonymous(self):
              return False
      ```

  - content: |

      ### Create a dummy user loader function

      ```python
      @login_manager.user_loader
      def load_user(username):

          return None
      ```

  - content: |

      ### Site should work






  - content: |

      ## Restrict access to pages


  - content: |

      ### Import login_required to usermanager

      ```python
      from flask.ext.login import login_required
      ```

  - content: |

      ### Import usermanager into routes

      ```python
      from public import usermanager
      ```


  - content: |

      ### Add mixin to new message page

      ```python
      @website.route('/new-message')
      @usermanager.login_required
      def new_message():
          return render_template('new-message.html')
      ```

  - content: |

      ### Check access is restricted


  - content: |

      ### Set the login page

      ```python
      login_manager.login_view = "users.login"
      ```

  - content: |

      ### Check the login redirect works








  - content: |

      ## Sign in form


  - content: |

      ### form action = sign-in

      ```html
      <form action="sign-in">
      ```


  - content: |

      ### form method = post

      ```html
      <form action="sign-in" method="post">
      ```

  - content: |

      ### form input names

      ```html
      <form action="sign-in" method="post">

        <label>Username</label>
        <input name="username" type="text">

        <label>Password</label>
        <input name="password" type="text">

        <input type="submit" value="Sign in">

      </form>
      ```

      Form inputs must have a name attribute
      for their data to be posted to the server.









  - content: |

      ## sign in route

  - content: |

      ### sign in method allow get and post

      ```python
      # sign in page
      @website.route('/sign-in', methods=["GET", "POST"])
      def sign_in():

          return render_template('sign-in.html')
      ```

  - content: |

      ### sign in method handle get and post

      ```python
      # sign in page
      if request.method == 'GET':

          return render_template('sign-in.html')


      # form submit handler
      if request.method == 'POST':

          print('log in the user')

      ```


  - content: |

      ### get the posted username and pass

      ```python
      #form submit handler
      if request.method == 'POST':

          username = request.form.get('username')
          password = request.form.get('password')

          user = usermanager.sign_in_user(username, password)

          return render_template()
      ```


  - content: |

      ### use them to authenticate


  - content: |

      ### redirect based on the result











  - content: |

      ## Implement the user loader function


  - content: |

      ### Import the datamanager

      So we can access the database
      to look up a user

  - content: |

      ### Add it to your usermanager file

      ```python
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

          return user
      ```


  - content: |

      ### Site should be working








  








  







  - content: |
      
      ## Sign out user


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

      In usermanager.py

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

      ## Display username


  - content: |

      ### Show username

      ```html
      {% if current_user.is_authenticated %}
      Hello {% if current_user.username %}
      {% endif %}
      ```







  - content: |

      ## Smart sign in / sign out links


  - content: |

      ### Use template vars to show things

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

      [Take me to the next chapter!](updating-data.html)


---