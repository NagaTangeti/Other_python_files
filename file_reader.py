#with open('pi_digits.txt') as file_object:
#	contents = file_object.read()
#print(contents)
#print(contents.rstrip())

filename = 'pi_digits.txt'

with open(filename) as file_object:
	#for line in file_object: #read line by line.
	lines = file_object.readlines() #to store in list line after line.

for line in lines: 
	print(line.rstrip())