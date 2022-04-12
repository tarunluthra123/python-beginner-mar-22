# a = (2, 4, 10, 20, 19, 28)
a = tuple(map(int, input().split()))
n = len(a)

ans = "Yes"

for i in range(n - 1):
    if a[i] > a[i + 1]:
        ans = "No"
        break

print(ans)
