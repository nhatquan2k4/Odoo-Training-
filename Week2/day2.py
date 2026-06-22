# module random
import random
from datetime import datetime

number = random.randint(1, 100)

names = ["Quan", "Danh", "Nguyen", "Quang", "Tu"]
random_name = random.choice(names)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print("So ngau nhiem:", number)
print("Ten ngay nhien:", random_name)
print(numbers)


#module datetime
now = datetime.now()
print("Current datetime:", now)

now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

birthday = datetime(2004, 10, 20)
print("Birthday:", birthday)
