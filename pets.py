def describe_pets(pet_name, animal_type = 'dog'):
	"""Display information about a pet."""
	print(f"\nI've a {animal_type}.")
	print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pets(animal_type = 'hamster', pet_name = 'harry')
describe_pets(pet_name = 'willie', animal_type = 'dog')
describe_pets('mickey')

