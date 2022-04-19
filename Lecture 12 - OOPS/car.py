class Car:
    model = "Hatchback"
    color = "Black"
    price = 100000
    isLocked = False

    def drive(self):
        print("Zoom zoom zoom")

    def lock(self):
        self.isLocked = True
        print("Car is now locked")

    def unlock(self):
        self.isLocked = False
        print("Car is now unlocked")


# Main part of the program
c1 = Car()
c2 = Car()

c1.lock()
print(c1.isLocked)  # True

c2.unlock()
print(c2.isLocked)  # False

# print(c1.color)  # Black
# print(c1.model)  # Hatchback
# print(c1.price)  # 100000

# c2.color = "Red"
# print(c2.color)  # Red

# c2.fuel = "CNG"
# print(c2.fuel)  # CNG

# c1.drive()
# c2.drive()

# c1.lock()
# c2.lock()

# c1.unlock()
# c2.unlock()


def hello(name):
    print("Hello", name)


hello("Tony Stark")
