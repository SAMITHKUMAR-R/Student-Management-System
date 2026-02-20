# Student Management System
import json
FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    students = load_data()
    student = {}
    student["id"] = input("Enter Student ID: ")
    student["name"] = input("Enter Name: ")
    student["age"] = input("Enter Age: ")
    student["course"] = input("Enter Course: ")
    students.append(student)
    save_data(students)
    print("Student added successfully!")

def view_students():
    students = load_data()
    if students:
        for s in students:
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    else:
        print("No student records found.")
def update_student():
    students = load_data()
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter New Name: ")
            s["age"] = input("Enter New Age: ")
            s["course"] = input("Enter New Course: ")
            save_data(students)
            print("Student updated successfully!")
            return
    print("Student not found.")
def delete_student():
    students = load_data()
    sid = input("Enter Student ID to delete: ")
    new_students = [s for s in students if s["id"] != sid]
    if len(new_students) != len(students):
        save_data(new_students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Main menu
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

