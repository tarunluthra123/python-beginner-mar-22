n = 36

# Range - 1 to N

for i in range(1, n + 1):
    # Check if N is divisible by i
    if n % i == 0:
        print(i, end=" ")
