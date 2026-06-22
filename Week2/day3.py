from datetime import datetime

# File handling:
with open ("test.txt", "w") as file:
    file.write("quan dz")

# Options: "w": ghi moi, "r": doc, "a": them vao cuoi, "x": tao moi, loi neu da ton tai
while True:
    info = input("type anything or exit: ")
    if info.lower() == "exit":
        print("stop")
        break

    current_time = datetime.now()
    with open("test.txt", "a") as file:
        file.write(f"{current_time}\n{info}")

    print("write to test.txt")



