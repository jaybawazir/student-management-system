# Registration menu
from data import registrations


def registration_menu():
    """Display and drive the Registration submenu."""
    while True:
        print("\n--- Registration Menu ---")
        print("1 - Display student's registered courses")
        print("2 - Register student in a course")
        print("0 - Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            found = False
            for reg in registrations:
                if reg[0] == sid:
                    print(f"{reg[1]} - Section {reg[2]}")
                    found = True
            if not found:
                print("No registrations found for that student.")

        elif choice == "2":
            sid = input("Enter Student ID: ").strip()
            cid = input("Enter Course Code: ").strip()
            sec = input("Enter Section: ").strip()
            registrations.append([sid, cid, sec])
            print("Student registered successfully.")

        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
