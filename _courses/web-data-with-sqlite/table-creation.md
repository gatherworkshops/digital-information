---
title: Table Creation

slides:

  - class: title-slide
    content: |

      # Table Creation
      _Containers to store your app data_




  - content: |
  
      ## Creating a Table

      Tables can be created using SQLite Studio.


  - content: |

      ### Open a database

      Use SQLite Studio to connect your
      **Message Board** database.


  - content: |

      ### Click the "Create Table" button

      Click the "Create Table" button which is
      a blue and white square with a green plus on it.


  - content: |

      ### Fill in a table name

      Give your table a name, lowercase and plural.
      This one will be the `users` table.


  - content: |

      ### Click the "Add Column" button

      The "Add column" button is a blue and 
      white square with a green stripe.


  - content: |

      ### Fill in the column information

      Specify the relevant column name, data type and size.


  - content: |

      ### Select Primary or Foreign Key if required

      You may select Primary Key or Foreign key if needed.


  - content: |

      ### Click the OK button

      Add the new column to the set of planned
      changes for the database.


  - content: |

      ### Repeat the process for all required columns

      Fill in the relevant information for each
      column needed in the `users` table.


  - content: |

      ### Click the "Apply changes" button

      The changes are not automatically saved,
      you need to apply them.







  - content: |

      ## Creating a table using the shell

      We can also create tables using a predefined script 
      stored in a file, which is helpful for backups.

  - content: |

      ### Create a new file schema.sql in your db folder

      A database schema describes the 
      structure of a database using code.


  - content: |

      ### Create a new transaction

      ```sql
      BEGIN TRANSACTION;

      COMMIT;
      ```

  - content: |

      ### Drop existing table

      If the table already exists, we need to delete it first.

      ```sql
      BEGIN TRANSACTION;

      DROP TABLE IF EXISTS users;

      COMMIT;
      ```


  - content: |

      ### Write a create table statement

      ```sql
      BEGIN TRANSACTION;

      DROP TABLE IF EXISTS users;
      CREATE TABLE users;

      COMMIT;
      ```

  - content: |

      ### Add a row describing the primary key

      ```sql
      BEGIN TRANSACTION;

      DROP TABLE IF EXISTS users;
      CREATE TABLE users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT
      );

      COMMIT;
      ```

  - content: |

      ### Add rows describing the attributes

      ```sql
      CREATE TABLE users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT(30),
        password TEXT(64),
        first_name TEXT(20),
        last_name TEXT(20),
        email TEXT(50),
        photo BLOB(10000)
      );
      ```

  - content: |

      ### Create another table for messages

      ```sql
      CREATE TABLE users(
        ...
      );

      DROP TABLE IF EXISTS messages;
      CREATE TABLE messages(
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT(300),
        time_created TEXT(30),
        user_id INTEGER FOREIGN_KEY
      );
      ```

      Remember to include any required foreign keys

  - content: |

      ### Verify structure of schema

      There should be a "begin transaction" and a "commit"
      with two "drop table" and two "create table" commands between.


  - content: |

      ### Save the file

      Very important, don't forget to save!


  - content: |

      ### Open the database from shell

      ```bash
      sqlite3 message-board.db
      ```

  - content: |

      ### Read and execute your SQL file using SQLite

      ```bash
      .read schema.sql
      ```

  - content: |

      ### Check the database visually

      Open the database in SQLite Studio and refresh,
      you should be able to see your new table structure.




  

  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Table Creation: Complete!

      [Take me to the next chapter!](creating-data.html)


---
