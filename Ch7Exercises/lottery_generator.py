import random

# Empty list to store lottery numbers
lottery_number = []

for i in range(7):
    # Generating random numbers 
    number = random.randrange(10)
    # Appends number to lottery_number
    lottery_number.append(number)

for i in range(len(lottery_number)):
    print(lottery_number[i])
