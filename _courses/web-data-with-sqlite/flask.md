---
layout: chapter
title: Flask
slides:

  - class: title-slide
    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Flask
      _Running a Python website_





  - content: |

      ![Flask Logo](assets/images/flask-logo.png){:height="200"}

      ## What the heck is Flask?

      We will be using Flask to run a website
      where we can interact with our database.

  - content: |

      ### Flask is a Python framework for websites

      This means it is a bunch of Python code that
      someone else wrote to do common website tasks.

    notes: |

      Flask is a framework for Python in the same way that these other projects are frameworks for their base languages:

      - jQuery is a framework for JavaScript
      - Sass is a framework for CSS
      - Laravel is a framework for PHP
      - Symfony is a framework for PHP

      A framework provides a library of existing code in the target language, along with some recommended ways of structuring your program.

      Frameworks allow developers to work together more easily by having a set of "design rules" for their code.

      Frameworks also allow us to achieve outcomes faster, as we don't need to write as much code.

  - content: |

      ### An HTML and CSS website run with Python

      A Flask website still uses HTML and CSS,
      but pages can also display data from Python.

  - content: |

      ### Allows you to run code before displaying a page

      Every Flask page is processed in Python
      before being displayed to the user.

  - content: |

      ### Allows you to re-use code across pages

      Flask support templates and includes,
      so you can write code once and re-use it.

  - content: |

      ### Built in support for database access

      We can use Python to access our database
      and then pass the results into an HTML page.





  - content: |
      
      ## Set up new project from starter

      Download and unzip the Flask starter kit.
      [Download Flask Starter](assets/zip/flask-starter.zip){:target="_blank"}

  - content: |

      ### Copy the public folder

      Copy the whole folder called "public"
      which is inside the flask-starter.

  - content: |

      ### Paste 'public' into your project folder

      You should now have two folders in your project:
      the `db` folder, and a new `public` folder.

  



  - content: |
      
      ## Flask tour

      Let's take a quick look at what
      we have included in the starter.


  - content: |

      ### The assets folder

      This is where you keep all of your images
      and also any CSS of JavaScript you need.

    notes: |

      We've included a starter CSS file, a few images, and jQuery.

      You will need to modify these assets as you develop your project.


  - content: |

      ### Includes folder

      This is where you keep pieces of HTML code
      you'd like to use on more than one page.

      eg. header, footer, navigation

    notes: |

      You will need to modify these includes as you develop your project.


  - content: |

      ### Templates folder

      In Flask, a template is the HTML layout
      for a page in your website.

      eg. index, user-profile, contact, generic-page

    notes: |

      You can use the same template across multiple pages, or you can have a separate layout for every page - it's up to you!

      The point is that you could for example design your home page to have a unique design, but have every other page have a consistent layout with only the page's content changing.

      You will need to modify these templates as you develop your project.

  - content: |

      ### Random Python init file

      This file is required by Python so that
      it knows to look here for project files.

    notes: |

      This init file is a pain, but you need it in any folder where you have python files which need to be included in the project, otherwise the app won't be able to find them.

      This init file also contains some code which the app needs when it first launches.

      You do not need to modify this file.


  - content: |

      ### The data manager handles database connections

      This file contains some helper functions to
      keep our database connected on every page.

    notes: |

      The database manager is not a default part of Flask, it's something Gather has written for you to make working with databases in Flask even easier.

      You need to change the name of the database referenced in this file.

      Once you've set the right database file path you do not need to modify this file again.


  - content: |

      ### The routes file manages your site's pages

      Maps web page URLs to Python functions.
      Most of your Python code will go in here!






  - content: |
      
      ## Run project

      A Flask website is a Python app,
      so we need to start it running.

  - content: |

      ### Set the correct database name

      ```python
      DATABASE = 'db/message-board.db'
      ```

      Open the file **datamanager.py** and 
      update the database file path.

  - content: |

      ### Create a run script

      ```python
      from public import website
      website.run(debug=True)
      ```

      Create a new file in your project
      called **runserver.py** with the code above.

    notes: |

      This file should be directly inside your project folder.

      The means your project should now contain the two folders **db** and **public** plus a new file called **runserver.py**.

      This Python script imports the information from **__init__.py** in the public folder, which includes a variable called **website** which is an instance of Flask.

      It then executes the **run** function on the website, which starts the app and makes it accessible from the browser.

      The parameter **debug=True** makes the Flask site automatically restart any time you make changes to the website files.


  - content: |
      
      ### Execute the 'run server' script from the shell

      ```bash
      python runserver.py
      ```

      Some text should be displayed
      to confirm the app is running.


  - content: |

      ### Open the site in a browser

      Open your web browser and navigate to 
      the url `localhost:5000` to see your site.







  - content: |

      ## Create routes and templates

      We have a home page, but we need
      to set up some other pages too.

  - content: |
      
      ### Page to post a new message

      We need a page where a user can
      type in and submit a new message.

  - content: |

      ### Template for new message

      ```html
      <h1>Post a new message</h1>

      <form>

        <label>What's happening?</label>
        <input type="text">

        <input type="submit" value="Post message">

      </form>
      ```

      Create a template called `new-message.html`
      containing the HTML code provided.

  - content: |
      
      ### Route for new message

      ```python
      # new message page
      @website.route('/new-message')
      def new_message():
          return render_template('new-message.html')
      ```

      Add a new route to `routes.py` which shows 
      the template `new-message` for the url `/new-message`.

  - content: |

      ### Check new message page works

      Navigate to the "new message" page 
      in your browser and check it exists!

  - content: |
      
      ### Template for sign in

      ```html
      <h1>Sign in</h1>

      <form>

        <label>Username</label>
        <input type="text">

        <label>Password</label>
        <input type="text">

        <input type="submit" value="Log in">

      </form>
      ```

      Create a template called `sign-in.html`
      which contains a simple sign in form.

  - content: |

      ### Route for sign in

      ```python
      # sign in page
      @website.route('/sign-in')
      def sign_in():
          return render_template('sign-in.html')
      ```

      Add a new route to which shows the
      sign in template at the url `/sign-in`.


  - content: |

      ### Check sign in page works

      Navigate to the "sign in" page 
      in your browser to check it exists!


  - content: |

      ### Challenge: Sign out page

      Create a new template and route
      for the site url `/sign-out`.

      It should just say "You are signed out".


  - content: |

      ### Challenge: Test Site

      Write a list of all your routes
      then test each in the browser.

      Tick them off if they work correctly!






  - content: |
      
      ## Create navigation

      We can use an **include** to store
      a menu bar for use on every page.

  - content: |

      ### Create nav bar include

      ```html
      <nav>
        <a href="/">Home</a>
        <a href="/new-message">New Message</a>
        <a href="/sign-in">Sign in</a>
        <a href="/sign-out">Sign out</a>
      </nav>
      ```

      Create a new file in the **includes** folder
      called **navbar.html**, containing the code provided.

  - content: |
      
      ### Include in all templates

      ```html
      {% include navbar.html %}
      ```

      At the top of each page template,
      add a line of code to include the nav.

    notes: |

      New syntax! Woo! The curly brackets with percentage signs are how we run small pieces of Python code within an HTML page.

      Look out for more of this as we go on!

  - content: |

      ### Test your navigation

      Reload your site in the browser
      and click to each page to test it.






  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Flask: Complete!

      [Take me to the next chapter!](web-lists.html)

---