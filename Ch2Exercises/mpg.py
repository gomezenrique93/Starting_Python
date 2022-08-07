miles_driven = input("Enter the number of miles you drove: ")
gallons_used = input("Enter the number of gallons you used: ")

miles_driven = int(miles_driven)
gallons_used = int(gallons_used)

MPG = miles_driven / gallons_used
print('Your MPG: ', format(MPG, ',.2f'))
