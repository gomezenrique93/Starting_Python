#The maximum number
MAX = 5

#Initialize an accumulator variable
total = 0.0

#Explain what we are doing.
print("This program calcules the sum of")
print(MAX, "numbers you will enter.")

#Get the numbers and accumulate them.
for counter in range(MAX):
    numbers = int(input("Enter a number: "))
    total += numbers

#Display the total of the numbers.
print("The total is", total)