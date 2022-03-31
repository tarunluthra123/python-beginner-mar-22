import random


while True:
    x = random.randint(1, 10)

    if x % 4 == 0:
        continue

    print(x, end=" ")

    if x == 5:
        break
