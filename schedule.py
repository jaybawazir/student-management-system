# Schedule menu
from data import schedules, registrations


def schedule_menu():
    """Display and drive the Schedule submenu."""
    while True:
        print("\n--- Schedule Menu ---")
        print("1 - Display one student's schedule")
        print("2 - Add to student schedule")
        print("0 - Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            found = False
            for reg in registrations:
                if reg[0] == sid:
                    for sched in schedules:
                        if sched[0] == reg[1] and sched[1] == reg[2]:
                            print(f"{sched[0]} Section {sched[1]}: {sched[2]}, {sched[3]}")
                            found = True
            if not found:
                print("No schedule found for that student.")

        elif choice == "2":
            sid = input("Enter Student ID: ").strip()
            cid = input("Enter Course Code: ").strip()
            section = input("Enter Section: ").strip()
            registrations.append([sid, cid, section])
            print("Schedule added successfully.")

        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
