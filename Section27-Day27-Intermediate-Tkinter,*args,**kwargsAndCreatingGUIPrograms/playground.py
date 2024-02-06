def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# print(add(1, 2, 3, 4, 5, 6, 7))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("model")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(model="GT-R")
print(my_car.model)
