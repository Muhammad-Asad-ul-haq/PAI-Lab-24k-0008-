students = {}

while True:
    print("\n--- Student Management System ---")
    print("--------------------------------")
    print("1. Add any Student")
    print("2. Update the Marks")
    print("3. Delete any Student")
    print("4. Find the Topper")
    print("5. Show All the Students")
    print("6. Exit")
    print("--------------------------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        students[name] = marks
        print("Student added")

    elif choice == "2":
        name = input("Enter name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated")
        else:
            print("Student not found")

    elif choice == "3":
        name = input("Enter name: ")
        if name in students:
            del students[name]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == "4":
        if students:
            topper = max(students, key=students.get)
            print("Topper:", topper, "with marks", students[topper])
        else:
            print("No students yet")

    elif choice == "5":
        print("All Students:", students)

    elif choice == "6":
        print("Thanyou for visiting")
        break

    else:
        print("Invalid choice")
