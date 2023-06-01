class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initiate name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate a dog rolling over in response to a command."""
		print(f"{self.name} roled over!")

my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"{your_dog.name} is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()



