# run this file to start the program
from students import student_menu
from courses import course_information_menu
from grades import grades_menu
from schedule import schedule_menu
from registration import registration_menu


def main_menu():
    """Display and drive the top-level Main Menu."""
    while True:
        print("\n=== Main Menu ===")
        print("1 - Student Information")
        print("2 - Course Information")
        print("3 - Grades")
        print("4 - Schedule")
        print("5 - Registration")
        print("9 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_information_menu()
        elif choice == "3":
            grades_menu()
        elif choice == "4":
            schedule_menu()
        elif choice == "5":
            registration_menu()
        elif choice == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
