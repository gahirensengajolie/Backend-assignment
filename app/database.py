import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL UNIQUE
                           )''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           subject TEXT NOT NULL,
                           email TEXT NOT NULL,
                           years_experience INTEGER NOT NULL,
                           employee_id TEXT NOT NULL UNIQUE
                           )''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           code TEXT NOT NULL UNIQUE,
                           credits INTEGER NOT NULL,
                           department TEXT NOT NULL,
                           description TEXT
                           )''')
