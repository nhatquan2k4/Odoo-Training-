#list, tuples, dictionaries
#list
a = [1,2,3,4]
a.append(5)
a[2] = 6
print(a)
print(type(a))
print(a[1:3])
print(a[:3])
print(a[-2:])
print(a[2:])
print(a[::2])

#tuple
b = (1,2,3,4)
print(b)
print(type(b))
print(len(b))
print(2 in b)

#dictionary
c={
    "name": "quan",
    "age": 25
    }
print(c)
print(type(c))
print(c.get("name"))

c["age"] = 22
c["gender"] = "male"
print(c)

del c["gender"]
c.pop("age")
print(c)