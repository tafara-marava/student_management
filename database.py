# database.py
import sqlite3

def create_connection():
    # Connects to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('student_management.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create tables for the Student Management System
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                        StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
                        FirstName TEXT,
                        LastName TEXT,
                        BirthDate TEXT,
                        Gender TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                        CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CourseName TEXT,
                        CourseCode TEXT,
                        Credits INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                        EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                        StudentID INTEGER,
                        CourseID INTEGER,
                        EnrollmentDate TEXT,
                        FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
                        FOREIGN KEY(CourseID) REFERENCES Courses(CourseID))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
                        GradeID INTEGER PRIMARY KEY AUTOINCREMENT,
                        EnrollmentID INTEGER,
                        Grade TEXT,
                        FOREIGN KEY(EnrollmentID) REFERENCES Enrollments(EnrollmentID))''')

    conn.commit()
    conn.close()
