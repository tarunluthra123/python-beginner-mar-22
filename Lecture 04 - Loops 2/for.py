# print(list(range(-1, 10, 2)))

for i in range(-1, 10, 2):
    print(i * i, end=" ")

print()

j = 0
r = range(-1, 10, 2)
while j < len(r):
    print(r[j] * r[j], end=" ")
    j += 1
