BEGIN TRANSACTION;

DELETE FROM messages;
DELETE FROM users;

-- Tanya
INSERT INTO users VALUES(
  NULL, 
  'tanya', 
  'test', 
  'Tanya', 
  'Gray', 
  'tanya@gathergather.co.nz', 
  NULL
);

INSERT INTO messages VALUES (
  NULL,
  'Hello from tanya',
  julianday('now'),
  last_insert_rowid()
);


-- Sarah
INSERT INTO users VALUES(
  NULL, 
  'sarah', 
  'test', 
  'Sarah', 
  'Gray', 
  'sarah@gathergather.co.nz', 
  NULL
);

INSERT INTO messages VALUES (
  NULL,
  'Hello back, from Sarah',
  julianday('now'),
  last_insert_rowid()
);


-- Pascal
INSERT INTO users VALUES(
  NULL, 
  'pascal', 
  'test', 
  'Pascal', 
  'Gray', 
  'pascal@gathergather.co.nz', 
  NULL
);

INSERT INTO messages VALUES (
  NULL,
  'Woof woof',
  julianday('now'),
  last_insert_rowid()
);

COMMIT;