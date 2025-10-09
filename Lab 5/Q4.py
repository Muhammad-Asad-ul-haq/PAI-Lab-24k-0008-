try:
    name = input("Enter name: ")
    cnic = input("Enter CNIC number: ")
    age = input("Enter age: ")
    salary = input("Enter salary: ")
    with open("employee.txt", "w") as f:
        f.write(f"Name: {name}\nCNIC: {cnic}\nAge: {age}\nSalary: {salary}\n")
    contact = input("Enter contact number: ")
    with open("employee.txt", "a") as f:
        f.write(f"Contact: {contact}\n")
    with open("employee.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("Error:", e)
