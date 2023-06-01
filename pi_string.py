filename = 'pi_digits.txt'

with open(filename) as file_object:
	#for line in file_object: #read line by line.
	lines = file_object.readlines() #to store in list line after line.

pi_string = ''
for line in lines:
	#pi_string += line.rstrip()
	pi_string += line.strip() #remove whitespaces.

#print(pi_string)
#print(len(pi_string))

birthday = input('Enter ur birthday, in the form mmddyy: ')
if birthday in pi_string:
	print('ur birthday appears in the first million digits of pi!')
else:
	print("ur birthday doesn't appears in the first million digits of pi!")


