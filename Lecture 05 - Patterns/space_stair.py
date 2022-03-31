n = 5


for i in range(1, n + 1):
    print("*", end="")

    for j in range(n + 1 - i):
        print(" ", end="")

    print("*", end="")
    print()
