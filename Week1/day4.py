# functions and modular code
number = int(input("nhap 1 so: "))

if number < 0:
    print("khong duoc la so am")
else:
    sum = 0
    factorial = 1

    for i in range(1, number + 1):
        sum += i
        factorial *= i

    print("tong tu 1 den", number, "la:", sum)
    print("giai thua cua", number, "la:", factorial)
