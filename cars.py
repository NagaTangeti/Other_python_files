cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #permanently sort, losing original list
print(cars)
cars.sort(reverse = True) #permanently sort, losing original list.
print(cars)

cars1 = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars1)) #temporarily sort, preserving original list.
print(cars1)

cars1.reverse()
print(cars1)
print(len(cars1))

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
