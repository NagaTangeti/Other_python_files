import math
def primality(number):
    if number < 2:
        print('False')
    elif number == 2:
        print('True')
    else:
        for i in range(2, int(number ** 0.5) + 1):
        #for i in range(2, math.ceil(number/2)+1):
            if number % i == 0:
                print('False')


number = int(input("Enter the number you want to check for primality: "))

primality(number)
