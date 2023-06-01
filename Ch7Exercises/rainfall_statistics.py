def main():
    # Holds total months per year
    TOTAL_MONTHS = 12

    # Initialized empty list
    rainfall = [0] * TOTAL_MONTHS

    # For loop to collect rainfall per month
    for i in range(TOTAL_MONTHS):
        print("Enter rainfall for month:", i+1) 
        rainfall[i] = float(input("Enter rainfall: "))
       
    # Holds total rainfall per year
    rainfall_per_year = calculate_total(rainfall)

    # Holds average rainfall per year
    rainfall_average = calculate_average(rainfall_per_year, TOTAL_MONTHS)

def calculate_total(total_rainfall):
    # Accumulator to hold total
    total = 0

    # For loop to accumulate totals
    for i in range(len(total_rainfall)):
        total += total_rainfall[i]

    # Returning total rainfall per year
    return total

def calculate_average(total_rainfaill, MONTHS):
    # Average calculation
    average = total_rainfaill / MONTHS

    # Returning average
    return average

main()
