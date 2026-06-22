# List Comprehension
# tao 1 list moi tu list co san

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

square = [ x ** 2 for x in numbers ]
even_number = [x for x in numbers if x % 2 == 0]
new_list = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(numbers)
print(f"binh phuong {square}")
print(f"So chan {even_number}")
print(f"list moi {new_list}")


#lambda functions
add = lambda a,b: a + b
square = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

students = [
    {"name": "quan", "score": 10},
    {"name": "danh", "score": 6},
    {"name": "nguyen", "score": 9}
]
sorted_students = sorted(students, key=lambda student: student["score"])

print(add(3,4))
print(square)
print(even_numbers)
print(sorted_students)

