# Grades menu
from data import grades


def grades_menu():
    """Display and drive the Grades submenu."""
    while True:
        print("\n--- Grades Menu ---")
        print("1 - Display one student's grade for one course")
        print("2 - Display one student's grades for all courses")
        print("3 - Display all students' grades in one course")
        print("0 - Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            cid = input("Enter Course Code: ").strip()
            found = False
            for g in grades:
                if g[0] == sid and g[1] == cid:
                    print(f"Student {sid} got grade {g[2]} in course {cid}")
                    found = True
            if not found:
                print("No grade found for that student in that course.")

        elif choice == "2":
            sid = input("Enter Student ID: ").strip()
            found = False
            for g in grades:
                if g[0] == sid:
                    print(f"{g[1]}: {g[2]}")
                    found = True
            if not found:
                print("No grades found for that student.")

        elif choice == "3":
            cid = input("Enter Course Code: ").strip()
            found = False
            for g in grades:
                if g[1] == cid:
                    print(f"Student {g[0]}: Grade {g[2]}")
                    found = True
            if not found:
                print("No grades found for that course.")

        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
