# Prints the square of a number

# Prints the square of a number
def square(x):
    print(x * x)


# Prints the sum of two numbers
def sum(a, b):
    print(a + b)


# Prints the square of all numbers from x to y
def helper(x, y):
    for i in range(x, y + 1):
        square(i)


# 9 16 25 36 49 64 81 100
helper(3, 10)


# square(5)
# square(8)
# square(9)


# sum(5, 2)
# sum(9, 3)
