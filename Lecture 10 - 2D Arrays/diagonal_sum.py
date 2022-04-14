a = [[4, 7], [6, 10]]

size = len(a)  # 2

s = 0

# i -> [0, size-1]
for i in range(size):
    s += a[i][i]

print(s)
