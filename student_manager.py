import json
import os

DATA_FILE = "students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)


def add_student(students):
    student_id = input("Enter student ID: ").strip()
    for s in students:
        if s["id"] == student_id:
            print("Student with this ID already exists.")
            return

    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    })
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f'ID: {s["id"]}, Name: {s["name"]}, Age: {s["age"]}, Course: {s["course"]}')


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    for s in students:
        if s["id"] == student_id:
            s["name"] = input(f'New name ({s["name"]}): ') or s["name"]
            s["age"] = input(f'New age ({s["age"]}): ') or s["age"]
            s["course"] = input(f'New course ({s["course"]}): ') or s["course"]
            save_students(students)
            print("Student updated successfully.")
            return
    print("Student not found.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    for i, s in enumerate(students):
        if s["id"] == student_id:
            students.pop(i)
            save_students(students)
            print("Student deleted successfully.")
            return
    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
