# Get the desired value
# Get the annual interest rate
# Get the number of years that the money will sit in the account.
# Calculate the amount that will have to be deposied.
    #present_value = future_value / (1 + rate)**years
# Display the result of the calculation in step 4.

future_value = float(input("Please enter your future value: "))
rate = float(input("Please enter your current interest rate: "))
years = int(input("Please enter the years you will leave the money in the account: "))

present_value = future_value / (1 + rate)**years

print("In order to obtain ", future_value, " you need to input", present_value)
