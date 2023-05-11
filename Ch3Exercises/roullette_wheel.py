# Prompt the user for a number from 0 to 36
user_input = int(input("Hello please enter a number between 0 and 36: "))

# Checks user input to make sure that 
# value is between 0 and 36
while user_input < 0 or user_input > 36:
    print("Please enter a value between 0 and 36")
    user_input = int(input("Hello please enter a number between 0 and 36: "))
   
if user_input == 0:
    print("Pocket is green")
elif user_input >= 1 and user_input <= 10:
    if user_input % 2 == 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif user_input >= 11 and user_input <= 18:
    if user_input % 2 == 0:
        print("The pocket is red")
    else:
        print("The pocket is black")
elif user_input >= 19 and user_input <= 28:
    if user_input % 2 == 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif user_input >= 29 and user_input <= 36:
    if user_input % 2 == 0:
        print("The pocket is red")
    else:
        print("The pocket is black")


