---
title: Updating Data

slides:

  - class: title-slide
    content: |

      # Updating Data
      _Saving changes to existing data_







  - content: |

      ## Editing a message

      To demonstrate editing an existing item
      in the database we can edit a message.

  - content: |

      ### Create a template for editing a message

      ```html
      <form action="edit-message" method="post">

          <label>Message</label>
          <input name="message" type="text">

          <input type="submit" value="Save">

      </form>
      ```

      Write a new template called edit-message.html
      which contains a form for editable fields.


  - content: |

      ### Include a hidden field for the id

      ```html
      <form action="edit-message" method="post">

          <label>Message</label>
          <input name="message" type="text">

          <input name="message_id" type="hidden">

          <input type="submit" value="Save">

      </form>
      ```

      This will help us know which table row
      to update when the form is submitted.


  - content: |

      ### Route for editing a message

      ```python
      # edit message page
      @website.route('/edit-message')
      @usermanager.login_required
      def edit_message():
          return render_template('edit-message.html')
      ```

      Create a new route for the message editor
      and display the correct template for it.


  - content: |

      ### Set up the GET and POST methods

      ```python
      # edit message page
      @website.route('/edit-message', methods=['GET', 'POST'])
      @usermanager.login_required
      def edit_message():

          if request.method == 'GET':
              return render_template('edit-message.html')

          elif request.method == 'POST':
              return redirect('/')
      ```



  - content: |

      ### Pass the message id to the edit-message route

      ```python
      # edit message page
      @website.route('/edit-message/<message_id>', methods=['GET', 'POST'])
      @usermanager.login_required
      def edit_message(message_id):

          if request.method == 'GET':
              return render_template('edit-message.html')

          elif request.method == 'POST':
              return redirect('/')
      ```


  - content: |

      ### Load the message data in the route

      ```python
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

          return render_template('edit-message.html')
      ```


  - content: |

      ### Pass the message data to the template

      ```python
      return render_template('edit-message.html', message=query_result)
      ```

      Pass the query result to the template
      under the variable name **message**.


  - content: |

      ### Display the message data in the form

      ```html
      <form action="edit-message" method="post">

          <label>Message</label>
          <input name="message" type="text" value="{{ message.content }}">

          <input name="message_id" type="hidden" value="{{ message.message_id }}">

          <input type="submit" value="Save">

      </form>
      ```


  - content: |

      ### Check that the form data shows up

      ```bash
      localhost:5000/edit-message/1
      ```

      Browse to the edit-message url in your
      browser and check that the message is showing.






  - content: |

      ## Saving the modified form data

      The user can now make changes to the form
      but the changes also need to be saved.


  - content: |

      ### Make the message id optional so we can post

      ```python
      # edit message page
      @website.route('/edit-message/<message_id>', methods=['GET', 'POST'])
      @usermanager.login_required
      def edit_message(message_id = None):

          ...
      ```


  - content: |

      ### Write the POST processing

      ```python
      if request.method == 'POST':

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

          return redirect('/')
      ```


  - content: |

      ### Check that it works

      Edit a message in the browser
      and check that it saves correctly.









  - content: |

      ## Linking to an edit page

      We can add a link to messages
      that the user can click to edit.


  - content: |

      ### Retrieve the message id for home page messages

      ```python
      @website.route('/')
      def index():

          query_string = (
            'SELECT message_id, content, username, time_created ' 
            'FROM messages INNER JOIN users '
            'USING (user_id) '
            'ORDER BY time_created DESC'
          )
      ```

      Update the query to load the message_id
      so we can use it for our edit link.



  - content: |

      ### Add a link to the message HTML

      ```html
      {% for message in messages %}
          <li>
              {{ message['username'] }}: {{ message['content'] }}
              <a href="{{ url_for('edit_message', message_id = message['message_id']) }}">Edit</a>
          </li>
      {% endfor %}
      ```

      Modify the **index.html** template to
      include an **edit** link on the message.


  - content: |

      ### Only show the edit link for the message owner

      ```html
      {% for message in messages %}
          <li>
              {{ message['username'] }}: {{ message['content'] }}
              {% if current_user.username == message['username'] %}
              <a href="{{ url_for('edit_message', message_id = message['message_id']) }}">Edit</a>
              {% endif %}
          </li>
      {% endfor %}
      ```

      Users should only be able to edit their
      own messages, not messages by other people!




  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Updating Data: Complete!

      [Take me to the next chapter!](deleting-data.html)


---