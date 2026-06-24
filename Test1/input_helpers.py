def input_non_empty(input_message, error_message):
    while True:
        value = input(input_message).strip()

        if value:
            return value

        print(error_message)


def input_positive_int(input_message, error_message):
    while True:
        try:
            number = int(input(input_message))
            if number > 0:
                return number

            print(error_message)
        except ValueError:
            print(error_message)


def input_score(input_message):
    while True:
        try:
            score = float(input(input_message))
            if 0 <= score <= 10:
                return score

            print("Điểm phải nằm trong khoảng từ 0 đến 10.")
        except ValueError:
            print("Điểm phải là số thực.")


def input_scores(count_input_message="Nhập số lượng điểm: "):
    score_count = input_positive_int(
        count_input_message,
        "Số lượng điểm phải là số nguyên lớn hơn 0.",
    )
    scores = []

    for index in range(1, score_count + 1):
        score = input_score(f"Nhập điểm {index}: ")
        scores.append(score)

    return scores


def input_yes_no(input_message):
    while True:
        value = input(input_message).strip().lower()

        if value == "yes":
            return True
        if value == "no":
            return False

        print("Vui lòng nhập yes hoặc no.")


def input_menu_choice():
    try:
        return int(input("Chọn chức năng: "))
    except ValueError:
        print("Lựa chọn phải là số.")
        return None
