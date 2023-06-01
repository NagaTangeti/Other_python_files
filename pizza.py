def make_pizza(size, *toppings):
#	"""Print the list of topping that've been requested."""
#	print(toppings)

	"""Summarize the pizza we're about to make."""
	print("\nMaking a {size} - inch pizza with following toppings:")
	for topping in toppings:
		print(f"- {topping}")


