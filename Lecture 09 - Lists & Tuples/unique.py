a = [1, 6, 3, 2, 3, 8, 6, 1, 2]


def findUnique(a):
    for i in range(len(a)):
        print(a[i], a.index(a[i], i + 1))


print(findUnique(a))
