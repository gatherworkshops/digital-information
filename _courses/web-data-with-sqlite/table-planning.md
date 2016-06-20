---
title: Table Planning

slides:

  - class: title-slide
    content: |

      # Table Planning
      _Mapping your data structure_




  - content: |

      ## Database Diagrams

      The first step in building a database
      is creating a map of the data.


  - content: |

      ### Tables contain rows of data

      A table should contain information 
      about a single set of data, eg:

      `people`, `cities`, `purchases`, `users`, `scores`


  - content: |

      ### Table columns describe the data

      Each table contains a number of columns.
      A column stores an attribute of the table item.

      The table `people` might have attributes
      `first_name`, `last_name`, `birth_date`, `email`


  - content: |

      ### Names use lowercase and underscores

      Table and column names should be all lowercase
      and use underscores instead of spaces.

      Table names are always plural.

  - content: |

      ### Use table diagrams to plan

      To plan a table visually, write the name of the table
      and list the table's attributes underneath.

  - content: |

      ### Challenge: Attributes

      Choose one or more of the following tables 
      and draw a visual plan for its structure:

      `users`, `scores`, `todo_items`





  - content: |

      ## Data Types

      Table columns each have a defined data type
      to restrict the information which can be stored.


  - content: |

      ### SQLite has only five data types

      In SQLite3, the available data types are:

      `text`, `numeric`, `integer`, `real`, `blob`

    notes: |

      In SQLite, giving a table column one of these types is known as giving it an "affinity".

      An affinity is a column's recommended data type, but any type of data can still be stored in it.


  - content: |

      ### Use `text` to store strings

      - **Name**
        First names, last names, pet names, celebrity crush names.
      - **Address**
        Stored text can have spaces, so could store a street address.
      - **Long Text**
        Can also store paragraphs of text, like someone's personal bio.
      - **Date**
        Stored as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS")
      {:.flex-list}

    notes: |

      The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).


  - content: |

      ### Use `integer` to store whole numbers

      - **Boolean**
        Stored using 1 for true and 0 for false
      - **Score**
        A number from 0 to something really big
      - **Stock Count**
        Positive or negative whole number
      - **Date**
        Stored as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.
      {:.flex-list}

    notes: |

      In an `integer` column, the value stored is a signed integer.

      The value will be stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.


  - content: |

      ### Use `real` to store decimals

      - **Date**
        Stored as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
      - **Bank Balance**
        Positive or negative number with decimal places
      {:.flex-list}

    notes: |

      The value is a floating point value, stored as an 8-byte IEEE floating point number.


  - content: |

      ### Use `numeric` to store numbers

      Use to store a mix of integer and real numbers


  - content: |

      ### Use `blob` to store other weird data

      - **Photos**
        Can be stored as hex data, though it's not ideal.
      - **Documents**
        Can be stored as binary data, but a bad idea.
      {:.flex-list}


    notes: |

      The value is a blob of data, stored exactly as it was input.


  - content: |

      ### Challenge: Data Types

      Assign a data type to each of your table columns, from:

      `text`, `numeric`, `integer`, `real`, `blob`





  - content: |

      ## Relationships between tables

      We can represent how data links together, for example:

      - A parent **has** children.
      - A person **has** an address.
      - A customer **has** purchases.
      - A user **has** friends.


  - content: |

      ### There are three types of relationships

      - **One to One**
        A user has a profile page, and a profile page belongs to only one user.
      - **One to Many**
        A customer has many purchases, but a purchase belongs to only one customer.
      - **Many to Many**
        A purchase has many bought items, and an item can be in many purchases.
      {:.flex-list}


  - content: |

      ### Relationships are drawn as lines between tables

      A table can have one, none, or many 
      lines going to other tables.


  - content: |

      ### Every table needs a unique ID column

      This column is called the **Primary Key**.
      Its type is `integer` and its value is auto-generated.


  - content: |

      ### Linked data is stored using the row's ID

      A linked data column is know as a **Foreign Key**.
      Its type is `integer` and you must specify the ID to store.


  - content: |

      ### Challenge: Relationship Diagrams

      Draw these tables, their attributes 
      and map their relationships:

      users, friendships, photos, albums


  - content: |

      ### Challenge: Identify Primary and Foreign Keys

      Mark the primary key column with (PK),
      and mark the foreign key columns with (FK)




  - content: |

      ## What we learned about table planning

      - **Planning**
        Tables are planned using table maps and visual lines between.
      - **Relationships**
        Tables can have related data using primary and foreign keys.
      - **Primary Keys**
        Are columns which uniquely identify a row item.
      - **Foreign Keys**
        Are columns which store the primary key of an item in another table.
      {:.flex-list}


  - content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## Table Planning: Complete!

      [Take me to the next chapter!](table-creation.html)


---
