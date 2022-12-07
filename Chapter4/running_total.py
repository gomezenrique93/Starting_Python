#Calculate the running total of numbers
#Input by a user

MAX = 5

#Accumulator variable set to 0
total = 0

print('Enter up to', MAX, 'numbers')
print("Then I'll add them!!")

for count in range(MAX):
    numbers = int(input('Enter a number: '))

    #Add all values entered
    total += numbers

print(total)


    
        