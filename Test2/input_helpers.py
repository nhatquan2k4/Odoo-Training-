def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Gia tri phai lon hon hoac bang 0.")
                continue
            return value
        except ValueError:
            print("Gia tri phai la so.")


def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("So luong phai lon hon hoac bang 0.")
                continue
            return value
        except ValueError:
            print("So luong phai la so nguyen.")


def input_menu_choice():
    try:
        return int(input("Nhap lua chon: "))
    except ValueError:
        print("Lua chon phai la so.")
        return None
