RANK_LEVELS = ("Yếu", "Trung bình", "Khá", "Giỏi", "Xuất sắc")


def create_student(student_id, name, age, scores, is_active):
    return {
        "id": student_id,
        "name": name,
        "age": age,
        "scores": scores,
        "is_active": is_active,
    }


def find_student_by_id(students, student_id):
    normalized_id = student_id.strip().lower()

    for student in students:
        if student["id"].lower() == normalized_id:
            return student

    return None


def calculate_total(scores):
    total = 0

    for score in scores:
        total += score

    return total


def calculate_average(scores):
    if len(scores) == 0:
        return 0

    total = calculate_total(scores)
    return round(total / len(scores), 2)


def find_best_student(students):
    best_student = None
    best_average = -1

    for student in students:
        average = calculate_average(student["scores"])

        if average > best_average:
            best_student = student
            best_average = average

    if best_student is None:
        return None

    return best_student, best_average


def classify_student(average):
    if average >= 9.0:
        return RANK_LEVELS[4]
    if average >= 8.0:
        return RANK_LEVELS[3]
    if average >= 6.5:
        return RANK_LEVELS[2]
    if average >= 5.0:
        return RANK_LEVELS[1]

    return RANK_LEVELS[0]
