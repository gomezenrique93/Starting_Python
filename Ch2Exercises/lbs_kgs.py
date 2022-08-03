#Get lbs from user
#Convert lbs to kgs
#1lb = 0.454 kgs
#Display kgs to user

print("Hello this program will convert pounds to kilograms")
pounds = float(input("Please enter the number of lbs: "))
KILOGRAMS = 0.454
total_kilograms = pounds * KILOGRAMS

print("Total kgs is", format(total_kilograms, ".2f"))
