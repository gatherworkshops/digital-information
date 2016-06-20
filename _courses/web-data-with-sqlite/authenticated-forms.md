---
title: Authenticated Forms

slides:

  - class: title-slide
    content: |

      # Authenticated Forms
      _Associating form data with a user_





  - content: |

      ## Posting a message

      Only logged in users should be able to post,
      and their username should be associated.


  - content: |

      ### Ensure the form is formatted correctly

      Add the form action and form method,
      plus names for all form inputs.

  - content: |

      ### Allow POST data for new message route

      ```python
      @website.route('/new-message', methods=['GET', 'POST'])
      @usermanager.login_required
      def new_message():
          return render_template('new-message.html')
      ```

      Add both POST and GET method options
      to the **new message** route.


  - content: |

      ### Handle both GET and POST methods

      ```python
      def new_message():

          if request.method == 'GET':
              return render_template('new-message.html')

          elif request.method == 'POST':
              return redirect('/')

      ```

      Modify the `new_message` function 
      to handle both request types.

  - content: |

      ### Get form data

      ```python
      def new_message():

          if request.method == 'GET':
              return render_template('new-message.html')

          elif request.method == 'POST':

              content = request.form.get('message')

              return redirect('/')

      ```

      Get the message content from the form.



  - content: |

      ### Import datetime so we can get the current time

      ```python
      from datetime import datetime
      ```

      Import the dattime module at 
      the top of your routes file.

  - content: |

      ### Generate current time

      ```python
      def new_message():

          if request.method == 'GET':
              return render_template('new-message.html')

          elif request.method == 'POST':

              content = request.form.get('message')
              current_time = datetime.now()

              return redirect('/')

      ```

      Generate the current time.

  - content: |

      ### Get logged in user id

      ```python
      def new_message():

          if request.method == 'GET':
              return render_template('new-message.html')

          elif request.method == 'POST':

              content = request.form.get('message')
              current_time = datetime.now()
              user_id = usermanager.current_user.user_id

              return redirect('/')

      ```
  
  - content: |

      ### Write query

      ```python
      elif request.method == 'POST':

          content = request.form.get('message')
          current_time = datetime.now()
          user_id = usermanager.current_user.user_id

          query_string = (
            'INSERT INTO messages( content, time_created, user_id ) '
            'VALUES (?,?,?)'
          )

          return redirect('/')

      ```

  - content: |

      ### Submit query with parameters

      ```python
      query_string = (
        'INSERT INTO messages( content, time_created, user_id ) '
        'VALUES (?,?,?)'
      )

      query_result = datamanager.query_db(
          query_string, 
          [content, current_time, user_id], 
          one=True
      )

      return redirect('/')

      ```
  
  - content: |

      ### Check result is valid

      ```python
      query_result = datamanager.query_db(
          query_string, 
          [content, current_time, user_id], 
          one=True
      )

      if query_result == None:
          print('error')
      else:
          print('success')

      return redirect('/')

      ```


  - content: |

      ### Check in browser

      Try posting a message and check
      that it shows up on the home page.




  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Authenticated Forms: Complete!

      [Take me to the next chapter!](updating-data.html)


---