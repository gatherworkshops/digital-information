---
layout: chapter
title: Web Lists
slides:

  - class: title-slide
    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Web Lists
      _Loading and displaying data_


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

  - content: |

      ### Get all messages and the user who posted

  - content: |

      ### Display username by message






  - content: |

      ## Order and optimise the results

  - content: |

      ### Order messages reverse chrono

  - content: |

      ### Limit to the last hundred messages






## List all users

### Create template

### Create route

### Query users table

### Display using loop

### Check visually






  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Web Lists: Complete!

      [Take me to the next chapter!](web-forms.html)


---
