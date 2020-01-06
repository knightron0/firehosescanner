import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()

def create():
    c.execute("""CREATE TABLE posts (
        sno integer PRIMARY KEY AUTOINCREMENT,
        title text,
        id integer,
        user text,
        topic text
    )
    """)
    conn.commit()
    c.execute("""CREATE TABLE votes (
        sno integer PRIMARY KEY AUTOINCREMENT,
        title text,
        id integer,
        user text,
        postid integer,
        topic text
    )
    """)
    conn.commit()
    c.execute("""CREATE TABLE comments (
        sno integer PRIMARY KEY AUTOINCREMENT,
        title text,
        id integer,
        user text,
        postid integer,
        topic text
    )
    """)
    conn.commit()
    c.execute("""CREATE TABLE problems (
        sno integer PRIMARY KEY AUTOINCREMENT,
        title text,
        id integer,
        user text,
        postid integer,
        topic text
    )
    """)
    conn.commit()
def addposts(id, user, title, topic):
    c.execute("INSERT INTO posts (id, user, title, topic) VALUES(?, ?, ?, ?)", (id, user, title, topic))
    conn.commit()

def addcomment(id, user, title, topic):
    cmd = "SELECT * FROM posts WHERE title="
    cmd += "'" + title + "'"
    c.execute(cmd)
    rws = c.fetchall()
    if len(rws) != 0:     
        postid = rws[0][0]
        c.execute("INSERT INTO comments (title, id, user, postid, topic) VALUES(?, ?, ?, ?, ?)", (title, id, user, postid))
        conn.commit()

def addvote(id, user, title, topic):
    cmd = "SELECT * FROM posts WHERE title="
    cmd += "'" + title + "'"
    c.execute(cmd)
    rws = c.fetchall()
    if len(rws) != 0:     
        postid = rws[0][0]
        c.execute("INSERT INTO votes (title, id, user, postid) VALUES(?, ?, ?, ?, ?)", (title, id, user, postid, topic))
        conn.commit()

def addproblem(id, user, title, topic):
    cmd = "SELECT * FROM posts WHERE title="
    cmd += "'" + title + "'"
    c.execute(cmd)
    rws = c.fetchall()
    if len(rws) != 0:     
        postid = rws[0][0]
        c.execute("INSERT INTO problems (title, id, user, postid, topic) VALUES(?, ?, ?, ?, ?)", (title, id, user, postid))
        conn.commit()

# create()
conn.commit()