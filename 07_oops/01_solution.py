class Car:
    total_car=0
 

    def __init__(self,userbrand,usermodel):
        self.__brand=userbrand
        self.__model=usermodel
        Car.total_car+=1

    def get_brand(self):
        return self.__brand+"!"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transpot"
    

    @property 
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"

my_Tesla=ElectricCar("Tesla","Model S","85KWh")

print(isinstance(my_Tesla,Car))
print(isinstance(my_Tesla,ElectricCar))
# print(my_Tesla.brand)
# print(my_Tesla.fuel_type())

# my_car=Car("Tata","Saffari")
# my_car.model="Citi"
# Car("Tata","Nexon")

# print(my_car.model)
# print(Car.total_car)

# # print(my_car.general_description())
# print(Car.general_description())

# my_car=Car("Toyota","Corola")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car=Car("Tata","Saffari")
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "This is battery info"

class Engine:
    def engine_info(self):
        return "This is engine info"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_new_Tesla=ElectricCarTwo("Tesla","ModelS")
print(my_new_Tesla.engine_info())
print(my_new_Tesla.battery_info())