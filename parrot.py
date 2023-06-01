prompt = "\nTell me something, and I'll repeat it back:"
prompt += "\nEnter 'quit' to end the program. "

message = " "
while message != 'quit':
	message = input(prompt)
	print(message)