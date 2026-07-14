from database import get_db_connection

def add_teacher(name, subject, email, years_experience, employee_id):
    with get_db_connection() as connection:
        connection.execute(
            "INSERT INTO teachers (name, subject, email, years_experience, employee_id) VALUES (?, ?, ?, ?, ?)",
            (name, subject, email, years_experience, employee_id)
        )

def get_teachers():
    with get_db_connection() as connection:
        rows = connection.execute("SELECT * FROM teachers").fetchall()
        return [dict(row) for row in rows]

def update_teacher(employee_id, name, subject, email, years_experience):
    with get_db_connection() as connection:
        connection.execute(
            "UPDATE teachers SET name=?, subject=?, email=?, years_experience=? WHERE employee_id=?",
            (name, subject, email, years_experience, employee_id)
        )

def delete_teacher(employee_id):
    with get_db_connection() as connection:
        connection.execute("DELETE FROM teachers WHERE employee_id=?", (employee_id,))