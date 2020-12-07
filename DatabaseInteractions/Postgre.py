
DB_HOST = "localhost"
DB_NAME = "database1"
DB_USER = "postgres"
DB_PASS = "114164"

import psycopg2


def create_table():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store2 (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


create_table()
