a = input()

b = a.split()
# b = ["5", "2","9","3"]

c = []
for x in b:
    # print(x)
    # print(type(x))
    c.append(int(x))

print(c)
print(type(c))
