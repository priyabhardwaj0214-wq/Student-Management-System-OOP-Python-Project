from student import Student

class StudentDatabase:
    def _init_(self):
        self.students = []

    def add_student(self, name, roll, marks):
        new_student = Student(name, roll, marks)
        self.students.append(new_student)
        print("Student added successfully!")

    def show_all(self):
        if not self.students:
            print("No students available.")
        for s in self.students:
            print(s.display(), "| Grade:", s.grade())