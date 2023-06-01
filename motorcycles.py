motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)

motorcycles[-1] = 'suzuki'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles1 = []

motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('ducati')
motorcycles1.append('suzuki')
print(motorcycles1)
motorcycles1.insert(0,'bentley')
print(motorcycles1)
del motorcycles1[1]
print(motorcycles1)
print(motorcycles1.pop())
print(motorcycles1)
print(f"The last motorcycle I owned was {motorcycles1.pop().title()}")
print(f"The first motorcycle I owned was {motorcycles1.pop(0).title()}")
print(motorcycles1)
motorcycles1.remove('yamaha')
print(motorcycles1)