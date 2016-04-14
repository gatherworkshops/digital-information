import sqlite3
from public import website
from flask import g


DATABASE = 'db/database-name.db'


def connect_db():
    return sqlite3.connect(DATABASE)



def init_db():
    with website.app_context():
        db = get_db()
        with website.open_resource('/db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@website.before_request
def before_request():
    g.db = connect_db()



@website.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()



def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

