BEGIN TRANSACTION;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT(30),
	password TEXT(64),
	first_name TEXT(20),
	last_name TEXT(20),
	email TEXT(50),
	photo BLOB(10000)
);

DROP TABLE IF EXISTS messages;
CREATE TABLE messages(
	message_id INTEGER PRIMARY KEY AUTOINCREMENT,
	content TEXT(300),
	time_created TEXT(30),
	user_id INTEGER FOREIGN_KEY
);

COMMIT;
