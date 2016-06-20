---
title: Web Forms

slides:

  - class: title-slide
    content: |

      # Web Forms
      _Capturing user input_









  - content: |

      ## Prepare the sign in form

      We need the form on the sign-in 
      page to be set up correctly.


  - content: |

      ### Set the form action to sign-in

      ```html
      <form action="sign-in">
      ```

      The form "action" is the URL or route
      where the form data should be submitted.


  - content: |

      ### Set the form method to post

      ```html
      <form action="sign-in" method="post">
      ```

      Setting the method to "post" allows us to
      easily access the data from within Python.


  - content: |

      ### Name all form inputs

      ```html
      <form action="sign-in" method="post">

        <label>Username</label>
        <input name="username" type="text">

        <label>Password</label>
        <input name="password" type="password">

        <input type="submit" value="Sign in">

      </form>
      ```

      Form inputs must have a name attribute
      for their data to be posted to the server.









  - content: |

      ## Modify the sign in route

      Our **sign-in** route now needs to process sign ins
      as well as display the sign in form to users.

  - content: |

      ### Import Flask's request package

      ```python
      from flask import request
      ```

      At the top of **routes.py**, import the
      request package to allow us to process forms.


  - content: |

      ### Define which methods are enabled for the route

      ```python
      @website.route('/sign-in', methods=['GET', 'POST'])
      def sign_in():
          return render_template('sign-in.html')
      ```

      The **GET** method is for viewing the web page,
      and the **POST** method is for processing form data.

  - content: |

      ### Do different things based on the method used

      ```python
      @website.route('/sign-in', methods=['GET', 'POST'])
      def sign_in():

          if request.method == 'GET':
              return render_template('sign-in.html')

          if request.method == 'POST':
              return 'log in the user'

      ```

      For a **GET** request we want to display the form,
      but for **POST** we want to log in the user.


  - content: |

      ### Check that both GET and POST are supported

      Browse to the sign in page and ensue that
      you get a different page when clicking sign in.


  - content: |

      ### Get the posted username and password

      ```python
      if request.method == 'POST':

          username = request.form.get('username')
          password = request.form.get('password')

      ```

      We can get the values entered in the form
      by using the names we specified in the HTML.

  - content: |

      ### Check the form fields in the shell

      ```python
      if request.method == 'POST':

          username = request.form.get('username')
          password = request.form.get('password')

          print('username:', username)
          print('password:', password)
      ```

      Sign in with a username and password,
      then check that they printed in the shell.




  


  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Web Forms: Complete!

      [Take me to the next chapter!](user-login.html)


---