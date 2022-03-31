n = 5

for i in range(1, n + 1):
    # Print i-1 spaces
    for j in range(i - 1):
        print(" ", end="")

    # Print n+1-i stars
    for j in range(n + 1 - i):
        print("*", end="")
    print()
