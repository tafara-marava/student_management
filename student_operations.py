# student_operations.py #
from database import create_connection

def add_student(first_name, last_name, birth_date, gender):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO Students (FirstName, LastName, BirthDate, Gender)
                      VALUES (?, ?, ?, ?)''', (first_name, last_name, birth_date, gender))

    conn.commit()
    conn.close()

def update_student(student_id, first_name, last_name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''UPDATE Students 
                      SET FirstName = ?, LastName = ?
                      WHERE StudentID = ?''', (first_name, last_name, student_id))

    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM Students WHERE StudentID = ?''', (student_id,))

    conn.commit()
    conn.close()

def query_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM Students''')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
