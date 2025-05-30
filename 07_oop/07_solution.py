class Car:
    total_car = 0
    def __init__(self, brand):
        self.brand = brand
        Car.total_car += 1

    @staticmethod
    def general_discreption():
        return "Car is mean by transport"

my_car = Car("Toyota")
print(Car.general_discreption())