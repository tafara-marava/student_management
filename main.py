# main.py
from student_operations import add_student, update_student, delete_student, query_students
from database import create_tables

def main():
    create_tables()  # Ensure tables are created before performing any operation

    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. Update a student")
        print("3. Delete a student")
        print("4. Query all students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            birth_date = input("Birth Date (YYYY-MM-DD): ")
            gender = input("Gender: ")
            add_student(first_name, last_name, birth_date, gender)

        elif choice == '2':
            student_id = int(input("Student ID to update: "))
            first_name = input("New First Name: ")
            last_name = input("New Last Name: ")
            update_student(student_id, first_name, last_name)

        elif choice == '3':
            student_id = int(input("Student ID to delete: "))
            delete_student(student_id)

        elif choice == '4':
            query_students()

        elif choice == '5':
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
