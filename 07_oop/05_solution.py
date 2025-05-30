class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Diesel or Petrol"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
    

electric_car = ElectricCar("Tesla", "Model S", "85kWh")
my_car = Car("Toyota", "Fortuner")

print(electric_car.fuel_type())
print(my_car.fuel_type())