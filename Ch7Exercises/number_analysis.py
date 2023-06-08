def main():
    # values holds the 
    # list from collect_values() 
    values = collect_values()

    # lowest_value holds the lowest
    # value from the list
    lowest_value = find_lowest(values)
    print("Lowest value is: ", lowest_value)

    ## maximum_value holds the lowest
    # value from the list
    maximum_value = find_highest(values)
    print("Maximum value is: ", maximum_value)

    # calculated_total holds the
    # total from numbers in list values
    calculated_total = calculate_total(values)

    # calculated_aversage holds the 
    # average from the numbers in the list
    calculated_average = calculate_average(calculated_total, len(values))
    print("Average value is: ", calculated_average)

def collect_values():
    # Empty list
    user_values = []

    # Prompts user for value 20 times
    for i in range(20):
        # Collect values from user
        val = int(input("Collect user values: "))

        # Adds values to the 
        # user_vallues list
        user_values.append(val)
    
    # returns list of user values
    return user_values

# function to find the lowest number
def find_lowest(val):
    
    # Variable to hold minimum value
    minimum_value = min(val)

    # Returns the smallest value
    return minimum_value

# function to find the highest number
def find_highest(val):

    # Variable to hold max value
    maximum_value = max(val)

    # Returns the maximum value
    return maximum_value

# Calculates the total numbers in a list
def calculate_total(val):

    # Accumulator variable
    total = 0

    # Loop to calculate total
    for i in range(len(val)):
        total += val[i]

    # returns running total
    return total

# Calculates the average numbers of the list 
def calculate_average(total, length):

    # Average calculation
    average = total / length 

    # Returns average value
    return average

main()
