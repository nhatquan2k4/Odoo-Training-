# Write a Python program that:
#Takes user input for a list of numbers.
#Uses a function to calculate the average and maximum of the list.
#Handles invalid inputs (e.g., non-numeric values) with try-except.
#Outputs the results in a formatted string.


def average_calculate(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

def maximum_calculate(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
        return maximum

try:
    numbers = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))

    if len(numbers) == 0:
        print("Bạn chưa nhập số nào.")
    else:
        average = average_calculate(numbers)
        maximum = maximum_calculate(numbers)

        print(f"Các số vừa nhập là {numbers}")
        print(f"Giá trị trung bình của danh sách là: {average:.2f}")
        print(f"Giá trị lớn nhất của danh sách là: {maximum}")

except ValueError:
    print("Lỗi: Bạn chỉ được nhập các giá trị số.")









