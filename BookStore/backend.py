import sqlite3


def connect():
    conn = sqlite3.connect( "books.db" )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)" )
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect( "books.db" )
    cur = conn.cursor()
    cur.execute( "INSERT INTO student VALUES(NULL,?,?,?,?)", (title, author, year, isbn) )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student Where title=? OR author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(" Delete FROM student where id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(" UPDATE student SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn,id))
    conn.commit()
    conn.close()


#connect()
#insert('fdfd', 'dfdfd', 1789, 8798988)
#print(view())
# print(search(author="You"))
#delete(7)
#update(1,"the moon","Ballet",1812,19897)