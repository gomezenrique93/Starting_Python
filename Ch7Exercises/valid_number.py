def main():
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

    # Holds calculated total
    total = calculate_total(valid_numbers)
    print(total)

    # Holds calculated average
    average = calculate_average(total, len(valid_numbers))
    print(average)

def calculate_total(valid_values):

    # Accumulator variable
    sum = 0

    # Loop to accumulate values
    for i in range(len(valid_values)):
        sum += valid_values[i]
    
    # Returns accumulated sum
    return sum

def calculate_average(total, length):

    # Calculates average
    average = total / length

    # returns average
    return average

main()
