ACTIVE_STATUS = {
    True: "Đang học",
    False: "Nghỉ học",
}


def print_menu():
    print()
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Xem chi tiết sinh viên theo mã")
    print("4. Cập nhật điểm sinh viên")
    print("5. Tính điểm trung bình của một sinh viên")
    print("6. Tìm sinh viên có điểm trung bình cao nhất")
    print("7. Xếp loại sinh viên")
    print("8. Tìm sinh viên theo tên")
    print("9. Hiển thị 3 sinh viên đầu tiên")
    print("10. Thống kê lớp học")
    print("0. Thoát")


def format_status(is_active):
    return ACTIVE_STATUS[is_active]


def show_student_summary(index, student):
    status = format_status(student["is_active"])
    print(
        f"{index}. {student['id']} - {student['name']} - "
        f"Tuổi: {student['age']} - Trạng thái: {status}"
    )


def show_students(students):
    if len(students) == 0:
        print("Chưa có sinh viên nào.")
        return

    print("Danh sách sinh viên:")
    for index, student in enumerate(students, start=1):
        show_student_summary(index, student)


def show_student_detail(student):
    status = format_status(student["is_active"])

    print(f"Mã sinh viên: {student['id']}")
    print(f"Tên: {student['name']}")
    print(f"Tuổi: {student['age']}")
    print(f"Điểm: {student['scores']}")

    if len(student["scores"]) > 0:
        print(f"Điểm đầu tiên: {student['scores'][0]}")
        print(f"Điểm cuối cùng: {student['scores'][-1]}")
    else:
        print("Sinh viên chưa có điểm.")

    print(f"Trạng thái: {status}")


def show_first_three_students(students):
    first_three_students = students[:3]

    if len(first_three_students) == 0:
        print("Chưa có sinh viên nào.")
        return

    print("3 sinh viên đầu tiên:")
    for index, student in enumerate(first_three_students, start=1):
        show_student_summary(index, student)


def show_statistics(students):
    total_students = len(students)
    active_count = 0
    total_age = 0
    total_score = 0
    score_count = 0

    for student in students:
        total_age += student["age"]

        if student["is_active"]:
            active_count += 1

        for score in student["scores"]:
            total_score += score
            score_count += 1

    inactive_count = total_students - active_count
    average_age = 0
    class_average = 0

    if total_students > 0:
        average_age = total_age / total_students

    if score_count > 0:
        class_average = total_score / score_count

    print("===== THỐNG KÊ LỚP HỌC =====")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đang học: {active_count}")
    print(f"Số sinh viên đã nghỉ: {inactive_count}")
    print(f"Tuổi trung bình: {average_age:.1f}")
    print(f"Điểm trung bình cả lớp: {class_average:.2f}")
