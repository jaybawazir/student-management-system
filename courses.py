# Course Information menu
from data import courses


def display_all_courses():
    """Print a formatted table of all courses."""
    if not courses:
        print("\nNo courses available.")
        return

    print("\n{:<10} | {}".format("Code", "Title"))
    print("-" * 40)
    for course in courses:
        print("{:<10} | {}".format(course[0], course[1]))
    print()


def add_course():
    """Prompt for details and add a new course, rejecting duplicate codes."""
    code = input("Enter new Course Code: ").strip()
    title = input("Enter Course Title: ").strip()

    if not code or not title:
        print("Course code and title cannot be empty.")
        return

    for course in courses:
        if course[0].lower() == code.lower():
            print("Course code already exists. Course not added.")
            return

    courses.append([code, title])
    print("Course added successfully.")


def delete_course():
    """Remove a course by code, with a confirmation prompt."""
    code = input("Enter Course Code to delete: ").strip()

    for i, course in enumerate(courses):
        if course[0].lower() == code.lower():
            confirm = input(
                f"Are you sure you want to delete {course[0]} - {course[1]}? (y/n): "
            ).strip().lower()
            if confirm == "y":
                del courses[i]
                print("Course deleted successfully.")
            else:
                print("Deletion canceled.")
            return

    print("Course code not found. No course deleted.")


def edit_course():
    """Edit the title of an existing course."""
    code = input("Enter Course Code to edit: ").strip()

    for course in courses:
        if course[0].lower() == code.lower():
            print(f"Current Title: {course[1]}")
            new_title = input("Enter new Course Title: ").strip()
            if new_title:
                course[1] = new_title
                print("Course title updated successfully.")
            else:
                print("Title cannot be empty. Update canceled.")
            return

    print("Course code not found. No course updated.")


def course_information_menu():
    """Display and drive the Course Information submenu."""
    while True:
        print("\nCourse Information Menu")
        print("1 - Display all Courses")
        print("2 - Add Course")
        print("3 - Delete Course")
        print("4 - Edit Course")
        print("0 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_all_courses()
        elif choice == "2":
            add_course()
        elif choice == "3":
            delete_course()
        elif choice == "4":
            edit_course()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
