a = [[1, 0], [0, 1]]

ans = "Identity Matrix"


for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j and a[i][j] == 1:
            continue
        elif i != j and a[i][j] == 0:
            continue
        else:
            ans = "Not an Identity Matrix"
            break

print(ans)
