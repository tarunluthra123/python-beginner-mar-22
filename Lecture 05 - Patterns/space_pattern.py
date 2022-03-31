n = 6

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
