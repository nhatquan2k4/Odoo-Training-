from actions import (
    add_student,
    search_student_by_name,
    show_best_student,
    show_student_average,
    show_student_rank,
    update_scores,
    view_student_detail,
)
from display import (
    print_menu,
    show_first_three_students,
    show_statistics,
    show_students,
)
from input_helpers import input_menu_choice


def main():
    students = []

    while True:
        print_menu()
        choice = input_menu_choice()

        if choice is None:
            continue
        if choice == 1:
            add_student(students)
        elif choice == 2:
            show_students(students)
        elif choice == 3:
            view_student_detail(students)
        elif choice == 4:
            update_scores(students)
        elif choice == 5:
            show_student_average(students)
        elif choice == 6:
            show_best_student(students)
        elif choice == 7:
            show_student_rank(students)
        elif choice == 8:
            search_student_by_name(students)
        elif choice == 9:
            show_first_three_students(students)
        elif choice == 10:
            show_statistics(students)
        elif choice == 0:
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
