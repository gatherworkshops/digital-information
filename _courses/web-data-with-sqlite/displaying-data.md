---
title: Displaying Data

slides:

  - class: title-slide
    content: |

      # Displaying Data
      _Loading data into a web page_


  - content: |

      ## Displaying a list of messages

      Our home page is going to be a list
      of all messages posted by users.

  - content: |

      ### Write a query to get all messages
      
      ```python
      # home/index page
      @website.route('/')
      def index():
          
          query_string = 'SELECT content FROM messages'

          return render_template('index.html')
      ```

      Find your home page route and create
      a variable describing a query string.

  - content: |

      ### Query the database

      ```python
      # home/index page
      @website.route('/')
      def index():
          
          query_string = 'SELECT content FROM messages'
          query_results = datamanager.query_db(query_string, [], one=False)

          return render_template('index.html')
      ```

      Use the data manager to send the query
      to the database and fetch the results.


  - content: |

      ### Print the query results to check them

      ```python
      # home/index page
      @website.route('/')
      def index():
          
          query_string = 'SELECT content FROM messages'
          query_results = datamanager.query_db(query_string, [], one=False)

          for result in query_results:
              print(result)

          return render_template('index.html')
      ```

      You can optionally print the results
      of the query to the shell.

    notes: |

      The results will only print to the shell when you referesh the page.

      You can see from the shell that each row item is formatted as a set of key:value pairs with curly brackets at each end.

      This is the python format for a dictionary, and means we can access values in each row item by name.

  - content: |

      ### Pass the query results to the template

      ```python
      # home/index page
      @website.route('/')
      def index():
          
          query_string = 'SELECT content FROM messages'
          query_results = datamanager.query_db(query_string, [], one=False)

          return render_template('index.html', messages=query_results)
      ```

      Pass the query results into the template
      under the variable name `messages`.

  - content: |

      ### Loop over messages

      ```html
      <ol>

        {% for message in messages %}
          <li>{{ message['content'] }}</li>
        {% endfor %}

      </ol>
      ```

      In your template, create a loop in the list
      to create a list item for each message.

  - content: |

      ### Check that it worked

      View the home page in your browser
      and check the messages are showing!







  - content: |

      ## Combine user data

      Our messages should also display the 
      username of the user who posted the message.


  - content: |

      ### Modify the query

      ```python
      def index():
          
          query_string = 'SELECT content, username FROM messages INNER JOIN users USING (user_id)'
          query_results = datamanager.query_db(query_string, [], one=False)

          for result in query_results:
              print(result)

          return render_template('index.html', messages=query_results)
      ```

      To get the username for each message,
      we need to join data from two tables.


  - content: |

      ### Tidy up long queries

      ```python
      query_string = (
          'SELECT content, username '
          'FROM messages INNER JOIN users '
          'USING (user_id)'
      )
      
      query_results = datamanager.query_db(query_string, [], one=False)
      ```

      Once queries get longer than about 5 or 6 words,
      you should tidy them by splitting over multiple lines.


  - content: |

      ### Display username by message

      ```html
      {% for message in messages %}
          <li>{{ message['username'] }}: {{ message['content'] }}</li>
      {% endfor %}
      ```

      Modify the index template message loop
      to display the username beside the message.


  - content: |

      ### Challenge: Display the message time

      Modify the query to get the time the message 
      was posted, and modify the template to display it.






  - content: |

      ## Order and optimise the results

      Recent messages should be displayed first,
      and only the last hundred messages should load.

  - content: |

      ### Order messages by time posted

      ```python
      query_string = (
          'SELECT content, username, time_created ' 
          'FROM messages INNER JOIN users '
          'USING (user_id) '
          'ORDER BY time_created DESC'
      )
      ```

      Modify the query to order the results
      based on the `time_created` value.

    notes: |

      Ordering by the time_created with ASC will be ascending order, where the oldest are at the top and the newest are at the bottom.

      DESC or 'descending' will put the newest post at the top and the oldest at the bottom.

  - content: |

      ### Limit to the last hundred messages

      ```python
      query_string = (
          'SELECT content, username, time_created ' 
          'FROM messages INNER JOIN users '
          'USING (user_id) '
          'ORDER BY time_created DESC '
          'LIMIT 100'
      )
      ```

      We should limit the number of messages
      to reduce strain on the website.






## List all users

### Create template

### Create route

### Query users table

### Display using loop

### Check visually




## Create a user profile page






  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Displaying Data: Complete!

      [Take me to the next chapter!](web-forms.html)


---
