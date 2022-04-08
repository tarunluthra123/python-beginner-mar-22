a = [5, 2, 9, 10]

# b = list(a)
b = a.copy()
# b = a

b[0] = 1000

print(a)
print(b)


# Empty list
# l = []
# l = list()

b = []
for x in a:
    b.append(x)
