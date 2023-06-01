# list that holds numbers
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# Empty list to store valid values
valid_numbers = []

# For loop to check which
# numbers are valid
for i in range(len(numbers)):
    if numbers[i] >= 0 and numbers[i] <= 100:
        # Appends valid numbers to valid_numbers list
        valid_numbers.append(numbers[i])

# Displays the list with
# values between 0 and 100
print(valid_numbers)
