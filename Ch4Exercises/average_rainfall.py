# This program will use nested loops to collect rainfall data
# Ask user for number of years
# Loop for number of years
# Inner loop will loop for 12 times

# Prompts user to enter in number of years for rainfall
number_of_years = int(input("How many years would you like to calculate rainfall? "))

# Variable to store total rainfall per year and month
total_rainfall = 0

# Counter variable to count the total number of months
total_months = 0

for i in range(number_of_years):
    print("Year: ", i + 1)
    for j in range(12):
        print("Rainfall for month ", j + 1)

        # This will prompt the user for rainfall per month
        rainfall_per_month = float(input("Enter rainfall: "))

        # This will add the total rainfall per month
        total_rainfall += rainfall_per_month
    
        # This will keep track of the total number of months
        total_months += 1

# Calculation for average rainfall
average_rainfall = total_rainfall / total_months

# Displays total rainfall per year
print("Total rainfall per year is", format(total_rainfall, ".2f"), " inches.")

# Displays average rainfall 
print("Average rainfall is ", format(average_rainfall, ".2f"), " inches.")

