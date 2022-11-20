#If the user enters either 1-3 this is first quarter
#If the user enters either 4-6 this is second quarter
#If the user enters either 7-9 this is third quarter
#If the user enters either 10-12 this is fourth quarter
#If the number is not between 1 & 12, the program should dispaly an error

#Capture user input
user_input = int(input("Enter a number from 1 to 12: "))

if user_input > 1 and user_input <=3:
    print("This is quarter one!")
elif user_input > 3 and user_input <= 6:
    print("This is quarter two!")
elif user_input > 6 and user_input <= 9:
    print("This is quarter three!")
elif user_input > 9 and user_input <= 12:
    print("This is quarter four!")
elif user_input < 1 or user_input > 12:
    print("ERROR your number should be between 1 and 12!!")
