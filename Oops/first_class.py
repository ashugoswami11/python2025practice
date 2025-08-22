class Car: #naming convention first letter of class must be capital
    def __init__(self, brand,model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def func_name(self):
        return f"brand is {self.__brand} and model is {self.__model}"

    def fuel_type(self):
        return "petrol or diesel"

    #static method
    @staticmethod
    def general_description():
        return "cars are means of transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electricity"


class Engine():
    def on(self):
        print("Engine is on")

class Battery():
    def charged(self):
        print("Battery is charged")

class Cartwo(Car, Engine, Battery):
    pass

newone = Cartwo("hyundai", "verna")

print(newone.func_name())

#object of the class
electric_car = ElectricCar("mg", "windsor", "60kWH")

#example use of isinstance() method
print(isinstance(electric_car, ElectricCar))
print(isinstance(electric_car, Car))




# print(electric_car.get_brand())
# print(electric_car.fuel_type())
#
#
# car1 = Car("maruti","estilo")
# # print(car1.model()) #this can't be used after property decorator
# print(car1.get_brand(), car1.model)
# print(car1.func_name())
# print(car1.fuel_type())
#
# print(Car.general_description())
