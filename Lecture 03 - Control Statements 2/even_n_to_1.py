n = int(input())

# Initialisation
if n % 2 == 0:
    i = n
else:
    i = n - 1

# condition
while i >= 2:
    print(i)
    i = i - 2
