from database import get_db_connection
def create_teachers_table():
    with get_db_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           subject TEXT NOT NULL,
                           email TEXT NOT NULL,
                           years_experience INTEGER NOT NULL,
                           employee_id TEXT NOT NULL
                           )''' )

