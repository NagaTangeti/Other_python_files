#from car import Car, ElectricCar

#my_beetle = Car('volkswagen', 'beetle', 2018)
#print(my_beetle.get_descriptive_name())

#my_tesla = ElectricCar('tesla', 'model S', 2020)
#print(my_tesla.get_descriptive_name())

import car

my_beetle = car.Car('volkswagen', 'beetle', 2018)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'model S', 2020)
print(my_tesla.get_descriptive_name())
