n = 8


for i in range(1, n + 1):
    # Print n-i spaces
    for j in range(n - i):
        print(" ", end="")

    # Print i stars
    for j in range(i):
        print("*", end="")
    print()
