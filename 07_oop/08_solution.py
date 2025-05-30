class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model

my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)
# my_car.model = "Canello"
print(my_car.model)







