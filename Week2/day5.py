import json

class Student:
    def __init__(self,name,point):
        self.name = name
        self.point = point

    def show_info(self):
        print(self.name)
        print(self.point)
        if self.pass_info() == True:
            print("Pass")
        else:
            print("No pass")

    def pass_info(self):
        if self.point >= 7:
            return True
        else:
            return False

    def to_dict(self):
        return {
                "name":self.name,
                "point":self.point
                }
    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["point"])

def save_student(students, filename):
        students_data = [student.to_dict() for student in students]
        with open(filename,"w") as file:
            json.dump(students_data,file)

def load_student(filename):
    with open(filename,"r") as file:
        students_data = json.load(file)
    students = [Student.from_dict(data) for data in students_data]



students = []

while True:
    name = input("Dien ten sinh vien, nhap exit de thoat: ")
    if name == "exit":
        break

    try:
        point = int(input("Nhap diem: "))
        if point < 0:
            print("Diem ko duoc am")
    except:
        print("Ban phai dien so")

    student = Student(name,point)
    students.append(student)

save_student(students, "students.json")
load_student = load_student("students.json")
student_info = [student.show_info() for student in students]

print(student_info)