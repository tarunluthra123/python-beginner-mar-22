class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def output(self):
        print("{} + {}i".format(self.real, self.imag))
        # print(f"{self.real} + {self.imag}i")


x = Complex(5, 3)
x.output()

y = Complex(12, -2)
y.output()


# def hello(name="Peter Parker"):
#     print("Hello ", name)


# hello()
# hello("Tony Stark")
