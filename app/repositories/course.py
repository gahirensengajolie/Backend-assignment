from database import get_db_connection

def add_course(title, code, credits, department, description):
    with get_db_connection() as connection:
        connection.execute(
            "INSERT INTO courses (title, code, credits, department, description) VALUES (?, ?, ?, ?, ?)",
            (title, code, credits, department, description)
        )

def get_courses():
    with get_db_connection() as connection:
        rows = connection.execute("SELECT * FROM courses").fetchall()
        return [dict(row) for row in rows]


def update_course(code, title, credits, department, description):
    with get_db_connection() as connection:
        connection.execute(
            "UPDATE courses SET title=?, credits=?, department=?, description=? WHERE code=?",
            (title, credits, department, description, code)
        )

def delete_course(code):
    with get_db_connection() as connection:
        connection.execute("DELETE FROM courses WHERE code=?", (code))