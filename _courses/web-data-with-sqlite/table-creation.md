---
layout: chapter
title: Table Planning
slides:

  - class: title-slide
    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Creating Tables
      _Containers to store your app data_




  - content: |
  
      ## Creating a Table

      

  - content: |

  		### Open SQLite Studio



  - content: |

  		### Create a new database


  - content: |

  		### Click the "Create Table" button


  - content: |

  		### Fill in a table name


  - content: |

  		### Click the "Add Column" button


  - content: |

  		### Fill in the column name, data type and size


  - content: |

  		### Select Primary or Foreign Key if required


  - content: |

  		### Click the OK button


  - content: |

  		### Repeat the process for all required columns





  - content: |

  		## Creating a table using the shell

  - content: |

  		### Create a new text file `schema.sql`

  		A database schema describes the structure
  		of a database using code.

  - content: |

  		### Write a create table statement

  		```sql
  		CREATE TABLE users;
  		```

  - content: |

  		### Add a row describing the primary key

  		```sql
  		CREATE TABLE users(
  			order_id INT AUTO_INCREMENT PRIMARY KEY
  		);
  		```

  - content: |

  		### Add rows describing the attributes

  		```sql
  		CREATE TABLE users(
  			order_id INT AUTO_INCREMENT PRIMARY KEY,
  			customer_id INT,
    		amount DOUBLE
  		);
  		```

  - content: |

  		### Add rows describing the foreign keys

  		```sql
  		CREATE TABLE users(
  			order_id INT AUTO_INCREMENT PRIMARY KEY,
  			customer_id INT,
    		amount DOUBLE,
  		);
  		```


  - content: |

  		### Save the file


  - content: |

  		### Open the database from shell

  		```bash
  		sqlite3 auction.db
  		```

  - content: |

  		### Read and execute your SQL file using SQLite

  		```bash
  		.read create.sql
  		```




---