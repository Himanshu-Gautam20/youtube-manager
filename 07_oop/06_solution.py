class Car:
    total_car = 0
    def __init__(self, brand):
        self.brand = brand
        Car.total_car += 1


Car("Tata")
Car("Toyota")
Car("Mercedes")

print(Car.total_car)
