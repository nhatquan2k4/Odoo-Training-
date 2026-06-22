class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

    def is_passed(self):
        return self.grade >= 5


name = input("Enter student name: ")
grade = float(input("Enter student grade: "))

student = Student(name, grade)

student.display_info()

if student.is_passed():
    print("Result: Passed")
else:
    print("Result: Failed")