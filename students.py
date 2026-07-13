# Student Information menu
from data import students


def display_students():
    """Print a formatted table of all students."""
    if not students:
        print("No students available.")
        return

    print(f"\n{'ID':<10} {'First Name':<15} {'Last Name':<15} {'Email':<35} {'Phone':<12}")
    print("-" * 90)
    for student in students:
        print(f"{student[0]:<10} {student[1]:<15} {student[2]:<15} "
              f"{student[3]:<35} {student[4]:<12}")
    print()


def add_student():
    """Prompt for details and add a new student, rejecting duplicate IDs."""
    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student[0] == student_id:
            print("Student ID already exists.")
            return

    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    email = input("Enter Email Address: ").strip()
    phone = input("Enter Phone Number: ").strip()

    students.append([student_id, first_name, last_name, email, phone])
    print("Student added successfully.")


def delete_student():
    """Remove a student by ID."""
    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student[0] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student ID not found.")


def edit_student():
    """Edit one or more fields of an existing student."""
    student_id = input("Enter Student ID to edit: ").strip()

    for student in students:
        if student[0] == student_id:
            while True:
                print("\nWhat would you like to edit?")
                print("1 - First Name")
                print("2 - Last Name")
                print("3 - Email")
                print("4 - Phone")
                print("0 - Cancel edit")
                choice = input("Choose field to edit: ").strip()

                if choice == "1":
                    student[1] = input("Enter new First Name: ").strip()
                    print("First name updated.")
                elif choice == "2":
                    student[2] = input("Enter new Last Name: ").strip()
                    print("Last name updated.")
                elif choice == "3":
                    student[3] = input("Enter new Email: ").strip()
                    print("Email updated.")
                elif choice == "4":
                    student[4] = input("Enter new Phone: ").strip()
                    print("Phone updated.")
                elif choice == "0":
                    print("Edit cancelled.")
                    return
                else:
                    print("Invalid choice.")
                    continue

                more = input("Edit another field for this student? (y/n): ").strip().lower()
                if more != "y":
                    break
            return

    print("Student ID not found.")


def student_menu():
    """Display and drive the Student Information submenu."""
    while True:
        print("\n--- Student Information Menu ---")
        print("1 - Display all student information")
        print("2 - Add student")
        print("3 - Delete student")
        print("4 - Edit student information")
        print("0 - Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            edit_student()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
