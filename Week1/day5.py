# error handling

while True:
    name = input("Nhập tên của bạn: ")

    if name.strip() == "":
        print("Tên không được để trống.")
    else:
        break
while True:
        try:
            age = int(input("nhap so tuoi: "))
            if age <= 0:
                print("tuoi khong the am")
            if type(age) == float:
                print("tuoi khong the la so thap phan")
            else:
                print(f"Tên của tôi là {name}, tôi {age} tuổi")
            break
        except ValueError:
            print("vui long nhap so")