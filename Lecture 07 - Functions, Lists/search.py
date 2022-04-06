a = [10, 20, 30, 40, 50, 30, 20]


print(a.index(20))  # 1

# print(a.index(1000))  # Error


print(a.index(30))
print(a.index(20))


b = [10, 20, [21, 22, 23], 30, 40]

# print(b.index(22))   -> Error
print(b[2].index(22))
