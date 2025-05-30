class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def batter_info(self):
        return "I am battery"

class Engine:
    def engine_info(self):
        return "I am engine"

class ElectricCar(Battery, Engine, Car):
    pass

my_tesla = ElectricCar("Tesla", "Model S")
print(my_tesla.batter_info())
print(my_tesla.engine_info())