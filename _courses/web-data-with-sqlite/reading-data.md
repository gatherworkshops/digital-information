---
title: Reading Data

slides:

  - class: title-slide
    content: |

      # Reading Data
      _Getting data out of your database_





  - content: |

      ## Backup to a text file

      Once you deploy a site, most of your interactions
      will need to be via the command line.

      Text files can also be backed up using version control.


  - content: |

      ### Open and connect database in SQLite Studio


  - content: |

      ### Right click the database in the sidebar


  - content: |

      ### Click export


  - content: |

      ### Select all and tick export data from tables


  - content: |

      ### Continue


  - content: |

      ### Format as SQL and choose file destination


  - content: |

      ### Click Done






  - content: |

      ## Backup to text file using shell


  - content: |

      ### Open database in shell

  - content: |

      ### Set the output

      ```bash
      .output message-board-backup.sql
      ```

  - content: |

      ### Dump the database

      ```bash
      .dump
      ```

  - content: |

      ### Quit sqlite

      ```bash
      .quit
      ```

  - content: |

      ### Check file in text editor

      Look for your table names and check
      that the data appears to be there.






  - content: |

      ## Creating table reports


  - content: |

      ### Set the output mode

      ```bash
      .mode csv
      ```

  - content: |

      ### Set the output file name

      ```bash
      .output user-report.txt
      ```


  - content: |

      ### Execute a table query

      ```sql
      SELECT * FROM users;
      ```


  - content: |

      ### Check the report file

      Open the user-report.txt in your editor
      and check that the information is listed.


  - content: |

      ### Challenge: Create a messages report

      Generate a report containing all messages
      and output it to messages-report.txt






  - content: |

      ## Creating simplified table reports

      You can choose to select just some columns
      from a table's data, keep it relevant!


  - content: |

      ### Set the output mode

      ```bash
      .mode csv
      ```

  - content: |

      ### Set the output file name

      ```bash
      .output user-list.txt
      ```


  - content: |

      ### Execute a table query

      ```sql
      SELECT first_name, last_name, email_address FROM users;
      ```





  - content: |

      ## Creating complex linked reports

      Often you'll need to create detailed reports
      which combine data from multiple tables.


  - content: |

      ### There are three ways to combine table data

      - Inner Join
        Most common
      - Outer Join

      - Cross Join
        Rarely used


  - content: |

      ### Inner Joins

      Combines data from two tables by
      matching up the values in a column.

    notes: |

      An inner join creates result rows for every combination of matching data from the first and second tables.

  
  - content: |

      ### Using an Inner Join

      ```sql
      SELECT *
      FROM messages INNER JOIN users
      USING (user_id);
      ```

  - content: |

      ### Challenge: Message and username

      Modify the query to display every message
      and the first name of the user who created it.

      ```txt
      "Hello from tanya",Tanya
      "Hello back, from Sarah",Sarah
      "Woof woof",Pascal
      ```


  - content: |

      ### Outer Join

      Combines data from two tables by displaying
      all data from the first and any relevant matches
      from the second.


  - content: |

      ### Using an outer join

      ```sql
      SELECT first_name, content
      FROM users LEFT OUTER JOIN messages
      USING (user_id);
      ```





  - content: |

      ## Saving complex reports to file

  - content: |

      ### Set the output mode

      ```bash
      .mode column
      ```

    notes: |

      By default, column width is 10. This means messages longer than 10 characters will be cut off.

      You can change the maximum column width using the sqlite command `.width`.

      eg. `.width 6 12` will make the first column 6 characters and the second column 12 characters wide.

  - content: |

      ### Turn on headers

      ```bash
      .headers on
      ```

  - content: |

      ### Set the output file name

      ```bash
      .output messages-list.txt
      ```

  - content: |

      ### Execute a query 

      ```sql
      PRINT 
      SELECT first_name, last_name 
      FROM users
      WHERE first_name = "Tanya";
      ```

      This query will write to the file.


  - content: |

      ### Execute another query

      ```sql
      SELECT *
      ```

  - content: |

      ### Execute a table query

      ```sql
      SELECT first_name, last_name, email_address 
      FROM users;
      ```









  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Reading Data: Complete!

      [Take me to the next chapter!](flask.html)


---