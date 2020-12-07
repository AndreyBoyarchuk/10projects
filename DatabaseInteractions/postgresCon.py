DB_HOST = "localhost"
DB_NAME = "database1"
DB_USER = "postgres"
DB_PASS = "114164"

import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student(id SERIAL PRIMARY KEY, name VARCHAR)")

conn.commit()

cur.close()

conn.close()