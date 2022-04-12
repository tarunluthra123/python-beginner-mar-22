def square(x):
    return x**2


a = [2, 4, 6, 9, 1]


b = tuple(map(square, a))


print(b)
