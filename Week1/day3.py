# control structures
secret_number = 7

guess = int(input("nhap 1 so: "))

while guess != secret_number:
    if guess < secret_number:
        print("so cua ban qua thap")
    else:
        print("so cua ban qua cao")

    guess = int(input("nhap lai 1 so: "))

print("ban da doan dung")