---
title: Databases

slides:

  - class: title-slide
    content: |

      # Databases
      _Storing your app data_




  - content: |
  
      ## Creating a Database

      First step, creating a thing!


  - content: |

      ### Create a project folder

      Create a folder called **message-board** in a 
      safe place where you usually save projects.


  - content: |

      ### Open SQLite Studio

      ![SQLite Studio main screen](assets/images/sqlite-studio-main-screen.png){:height="350"}

      [SQLite Studio](http://sqlitestudio.pl/?act=download){:target="_blank"} should already be installed.
      Open it up so we can get started!


  - content: |

      ### Click "Add a database"

      ![The "Add Database" button is a small grey cylinder with a green plus sign on it](assets/images/sqlite-studio-add-database-button.png){:height="350"}

      Click the "Add a database" button 
      at the top left of the app.


  - content: |

      ### Click "Create new database file"

      ![The button to create a new database is a green circle with a plus sign](assets/images/sqlite-studio-create-database-button.png){:height="350"}

      Click the "Create a new database file" button
      to the right of the File input box.


  - content: |

      ### Navigate to your project folder

      ![Find the folder you are using for your project and navigate inside it](assets/images/sqlite-studio-navigate-to-project.png){:height="350"}

      Use the file explorer to find your project
      and navigate inside the project folder.


  - content: |

      ### Enter a file name for your database

      ![Enter a file name with the file extension .db](assets/images/sqlite-studio-name-database-file.png){:height="350"}

      Enter a name for your database file,
      using the file extension `.db`.


  - content: |

      ### Save the file

      ![The save button at the bottom right of the window](assets/images/sqlite-studio-file-save-button.png){:height="350"}

      Click the "Save" button to save your new database file.


  - content: |

      ### Press OK

      ![The OK button is at the bottom right of the window](assets/images/sqlite-studio-open-database-ok-button.png){:height="350"}

      Click the "OK" button at the bottom right
      to open the database in SQLite Studio


  - content: |

      ### Select your database in the sidebar

      ![Databases are listed down the left of the window](assets/images/sqlite-studio-database-list.png){:height="350"}

      Click on your database in the sidebar to select it.


  - content: |

      ### Connect to the database

      ![The connect button is the first icon in the top button bar](assets/images/sqlite-studio-connect-db-button.png){:height="350"}

      Once the database is selected, 
      click the "Connect" button.

    notes: |

      Alternatively, you can double-click the database name in the sidebar.


  - content: |

      ### The "Tables" and "Views" options should be visible

      ![A connected database will have Tables and Views listed beneath it](assets/images/sqlite-studio-connected-db.png){:height="350"}

      A connected database will display the Tables and Views
      under the database name in the sidebar.


  - content: |

      ### Disconnecting the database

      ![The disconnect button is the second icon in the top button bar](assets/images/sqlite-studio-disconnect-db.png){:height="350"}

      Select the database in the sidebar, 
      then click the "Disconnect" button.






  - content: |

      ## Creating a database using the shell

      We can do the same database creation process 
      using the command line, which can be a lot faster 
      once you get used to it.


  - content: |

      ### Open the command line

      Open the Command Line app (cmd),
      or Terminal if you're using OSX.


  - content: |

      ### Navigate to your project folder

      Use `cd folder-name/` to change directory into your project folder.


  - content: |

      ### Open the new database

      ```bash
      sqlite3 messenger.db
      ```
      {:.big-code}

      Type `sqlite3` followed by the database file name
      you would like to use, and press enter.

    notes: |

      This command opens a connection to the file you specify, but it doesn't permanently save the file.

      Executing this command only expresses your _intention_ to create a new database. The database file you specify will be a temp file until you execute an additional command to initialise the database.


  - content: |

      ### Initialise the database

      ```bash
      .databases
      ```
      {:.big-code}

      Type `.databases` and press enter to initialise the database.

    notes: |
      This step creates the permanent database file and confirms its location.

      The `.databases` command is optional - if we immediately ran a query, such as creating a table, it would have the same effect of permanently saving the database.

      Sqlite does not automatically allow us to create an empty database by default.

      Using this command simply allows us to save the database without anything in it.

      


  - content: |

      ### Close the connection

      ```bash
      .exit
      ```

      Type `.exit` and press enter 
      to close the database connection.



  - content: |

      ### Check that the file exists

      ```bash
      ls
      ```

      Type `ls` on OSX or `dir` on Windows and press enter.
      The file `messenger.db` should be listed.






  - content: |

      ## Naming your Database

      Use file naming consistent with the rest of your project,
      most likely `hyphenated-names` or `underscore_names`.


    notes: |

      For the database file name you should use naming conventions consistent with the rest of your project.

      For a web project, that means `hyphenated-names` or `underscore_names`.

      HTML and JavaScript usually use hyphenated naming, while Python projects often use underscores. Since a database is more on the Python side of our project, it would be logical to use underscores rather than hyphens.

      In the end this decision is up to you, just make sure you're consistent!

      Different rules apply once we get _inside_ the database! We'll get to those rules shortly.


  - content: |

      ### Use a name relevant to the project

      Your database file name should be based on your project name.

      Try to avoid generic names like `database.db` or `mydata.db`.

    notes: |

      To decide if your database name is a good one, try asking the question:

      "If I found this database file on my desktop in 6 months would I know which project it was from?"

      Use a name which makes your database identifiable with or without the project.


  - content: |

      ### Names should be alphanumeric

      Use letters with underscores or hyphens only.

      Numbers can be used, but should be avoided where possible!

    notes: |

      Some examples of good database names:

      - `messenger.db`
      - `local-user-data.db`
      - `sports_day_planner.db`

      You may use a number if it is part of the project name:

      - `things2do.db`
      - `4sale.db`

      But don't keep multiple versions of your databases:

      - `party_planner_v2.db` - no!
      - `booking-system-final.db` - yuck!
      - `treasure-hunter2.db` - don't do it!


  - content: |

      ### Names should be all lowercase

      No capital letters here! Use all lowercase letters.

    notes: |

      Your database will still work fine if you don't follow this rule, but it's good practice to be consistent.

      When programming, one of the most common typos is forgetting to match the capitalisation of file names in the code with the actual file name. Using all lowercase all the time helps to avoid this issue.

      Also, some operating systems ignore letter case while others are very specific!

      Consistency helps us minimise potential problems or errors.


  - content: |

      ### Use underscores or hyphens instead of spaces

      For the database file name you should use naming
      conventions consistent with the rest of your project.






  - content: |

      ## Structural Overview

      Let's look briefly at how a SQLite database 
      works and what is stored inside it.


  - content: |

      ### SQLite databases are a standalone file

      This means you can copy it, paste it, delete it,
      email it, just like any other file.


  - content: |

      ### Use one database per project

      All the data for your whole app is stored in a 
      single database, with organised data inside.


  - content: |

      ### A single database has many tables

      A database is a collection of tables. 
      Each table stores a specific type of data.
    
    notes: |

      Data is not stored directly inside the database, 
      but always another level down, inside a table.

      All data in a database must be stored inside a table.


  - content: |

      ### Data can be treated independently of the database

      The structure of a database is defined 
      independently of the data stored within it.







  - content: |

      ## Access Permissions

      Protecting a SQLite database with a password
      encrypts all the data stored inside.


  - content: |

      ### There is no password protection by default

      SQLite databases are open and unencrypted by default.


  - content: |

      ### A password can be added using Python

      Encryption can only be enabled by reading the file
      from a script and including a command.


  - content: |

      ### SQLite Studio can not open encrypted databases

      A very sad side effect of encrypting your database
      is that free SQLite GUI programs can't open them.





  - content: |

      ## Challenge: New project with SQLite Studio

      **Use SQLite Studio** to create a new project called 
      "SuperChat" containing a new SQLite database.

      Make sure to use correct naming conventions!




  - content: |

      ## Challenge: New project with the shell

      Use shell commands to create a new project called 
      "Bake Sale Manager" containing a new SQLite database.

      Make sure to use correct naming conventions!


  - content: |

      ## Challenge: Edit with SQLite Studio

      Use SQLite Studio to open and connect to your 
      "Bake Sale Manager" database created using the shell.




  - content: |

      ## What we learned about databases

      - **Creating**
        We can create using the command line or SQLite Studio.
      - **Naming**
        File name should be consistent with other project files.
      - **Structure**
        A database contains tables which contain actual data.
      - **Permissions**
        Password protecting a SQLite database is frustrating.
      {:.flex-list}







  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Databases: Complete!

      [Take me to the next chapter!](table-planning.html)







---
