---
title: Creating Data

slides:

  - class: title-slide
    content: |

      # Creating Data
      _Getting data into your database_



  - content: |
      ## Adding a row

      Each item stored in a database
      is a single row in a table.

  - content: |

      ### Open the table in SQLite Studio

      Double click the `users` table in the sidebar.

  - content: |

      ### Switch to the data tab

      Click the data tab at the top of the window.

  - content: |

      ### Click the "Insert Row" button

      The button to insert a row is the
      green square with a plus sign on it.


  - content: |

      ### Fill in the row data

      Click a cell and then start typing.
      Leave `user_id` and `photo` as `NULL`.


  - content: |
      ### Commit your changes

      Click the green tick button to save
      your changes to the table data.

    notes: |

      The user_id should have been filled in automatically, because the column is set to autoincrement.

      The photo will still be null, as we didn't specify that this cell was a required one.






  - content: |

      ## Adding rows from the shell

      We can also script the creation of data.
      This is helpful for creating dummy data.

    notes: |

      For example, it can be helpful to have a set of dummy data which can be used to recreate your database in its entirety if anything were to go wrong.

      It can also be an easy way to switch between different sets of data to test your database with different data combinations.


  - content: |

      ### Create a new file dummy-data.sql

      Create a new file called dummy-data.sql 
      in the db folder and open it in your editor.

  - content: |

      ### Create a transaction

      ```sql
      BEGIN TRANSACTION;

      COMMIT;
      ```

  - content: |

      ### Delete all existing users

      ```sql
      BEGIN TRANSACTION;

      DELETE FROM users;

      COMMIT;
      ```

  - content: |

      ### Write an insert statement

      ```sql
      BEGIN TRANSACTION;

      DELETE FROM users;

      INSERT INTO users VALUES(
        NULL, 
        'tanya', 
        'test', 
        'Tanya', 
        'Gray', 
        'tanya@gathergather.co.nz', 
        NULL
      );

      COMMIT;
      ```

  - content: |

      ### Open the database in the shell

      ```sql
      sqlite3 message-board.db
      ```


  - content: |

      ### Execute the dummy data script

      ```sql
      .read dummy-data.sql
      ```

  - content: |

      ### Visually check the result

      Open the table in SQLite Studio and refresh
      to see the new rows you've added.

  - content: |

      ### Challenge: Additional users

      Add at least two extra fake users to 
      your dummy data script and execute it.




  - content: |
      ## Scripting complex data

      Many times we want to include data
      which goes beyond just plain text.


  - content: |

      ### Current date or time

      date('now')

      time('now')

      datetime('now')

      julianday('now')


  - content: |

      ### Specific date or time

      date('YYYY-MM-DD')

      time('HH:MM:SS')

      datetime('YYYY-MM-DD HH:MM:SS')

      julianday('123456789')


  - content: |

      ### Images

      Stored as a BLOB, which needs to be Hex format.

      You can convert images to Hex [here](motobit.com/util/binary-file-to-sql-hexstring.asp)


  - content: |

      ### Random numbers

      random() % (:high  - :low) + :low

      random() % (10  - 5) + 5





  - content: |
      ## Inserting linked data

      Most tables will have some form of linked data,
      and we need to script these relationships too.


  - content: |

      ### Decide correct order of creation

      Rows which "own" other rows need to be created first.

      For example, a user needs to be created before their posts 
      so that we can apply the user_id to the posts.
  

  - content: |
      
      ###  Write an independent insert statement

      Write a top-level insert statement which doesn't
      require foreign key data, such as a user.


  - content: |

      ### Write dependent insert statements

      Write an insert statement for a row which
      depends on the previously created row.


  - content: |

      ### Use the last row ID as the foreign key

      ```sql
      INSERT INTO messages VALUES (
        NULL,
        'Hello',
        datetime('now'),
        last_insert_rowid()
      );
      ```

  - content: |

      ### Execute the script in the shell

      ```sql
      .read dummy-data.sql
      ```

  - content: |

      ### Visually check the result

      Open the table in SQLite Studio and refresh
      to see the new rows you've added.

  - content: |

      ### Challenge: Additional messages

      Add a message for each of your users
      by adding to your dummy-data script.







  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Creating Data: Complete!

      [Take me to the next chapter!](reading-data.html)


---