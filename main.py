from database import StudentDatabase

db = StudentDatabase()

while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        marks = int(input("Enter marks: "))
        db.add_student(name, roll, marks)

    elif choice == "2":
        db.show_all()
    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")