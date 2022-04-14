r, c = map(int, input().split())

a = []

for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)


print(a)

for i in range(r):
    for j in range(c):
        print(a[i][j] ** 2, end=" ")
    print()

# 2 3
# 5 9 1
# 2 3 0
