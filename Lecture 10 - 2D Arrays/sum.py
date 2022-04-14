a = [[2, 3], [4, 5]]

b = [[0, -9], [2, 8]]

r = 2
c = 2

res = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(a[i][j] + b[i][j])
    res.append(row)

print(res)
