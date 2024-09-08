import os

import psycopg2

def test_database_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    assert conn is not None

def test_data_insertion():

    # Підключаємося до бази даних
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))

    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'John')")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE id=1")
    result = cursor.fetchone()
    assert result[1] == 'John'