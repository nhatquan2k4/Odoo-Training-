from input_helpers import (
    input_non_empty,
    input_positive_int,
    input_scores,
    input_yes_no,
)
from display import show_student_detail
from student_service import (
    calculate_average,
    classify_student,
    create_student,
    find_best_student,
    find_student_by_id,
)


def add_student(students):
    student_id = input_non_empty(
        "Nhập mã sinh viên: ",
        "Mã sinh viên không được rỗng.",
    )

    if find_student_by_id(students, student_id) is not None:
        print("Mã sinh viên đã tồn tại.")
        return

    name = input_non_empty(
        "Nhập tên sinh viên: ",
        "Tên sinh viên không được rỗng.",
    )
    age = input_positive_int(
        "Nhập tuổi: ",
        "Tuổi phải là số nguyên lớn hơn 0.",
    )
    scores = input_scores()
    is_active = input_yes_no("Sinh viên còn học không? yes/no: ")

    student = create_student(student_id, name, age, scores, is_active)
    students.append(student)
    print("Thêm sinh viên thành công!")


def view_student_detail(students):
    student_id = input("Nhập mã sinh viên: ").strip()
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Không tìm thấy sinh viên.")
        return

    show_student_detail(student)


def update_scores(students):
    student_id = input("Nhập mã sinh viên: ").strip()
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Không tìm thấy sinh viên.")
        return

    student["scores"] = input_scores("Nhập số lượng điểm mới: ")
    print("Cập nhật điểm thành công!")


def show_student_average(students):
    student_id = input("Nhập mã sinh viên: ").strip()
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Không tìm thấy sinh viên.")
        return

    average = calculate_average(student["scores"])
    print(f"Điểm trung bình của {student['name']} là: {average:.2f}")


def show_best_student(students):
    result = find_best_student(students)

    if result is None:
        print("Chưa có sinh viên nào.")
        return

    student, average = result
    print("Sinh viên có điểm trung bình cao nhất:")
    print(f"Mã: {student['id']}")
    print(f"Tên: {student['name']}")
    print(f"Điểm trung bình: {average:.2f}")


def show_student_rank(students):
    student_id = input("Nhập mã sinh viên: ").strip()
    student = find_student_by_id(students, student_id)

    if student is None:
        print("Không tìm thấy sinh viên.")
        return

    average = calculate_average(student["scores"])
    rank = classify_student(average)
    print(f"{student['name']} có điểm trung bình {average:.2f} - Xếp loại: {rank}")


def search_student_by_name(students):
    keyword = input("Nhập tên cần tìm: ").strip().lower()
    results = []

    for student in students:
        if keyword in student["name"].lower():
            results.append(student)

    if len(results) == 0:
        print("Không tìm thấy sinh viên.")
        return

    print("Kết quả tìm kiếm:")
    for student in results:
        print(f"{student['id']} - {student['name']}")
