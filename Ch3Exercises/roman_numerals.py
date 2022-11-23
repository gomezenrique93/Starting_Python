#Prompt the user to enter a number between 1 and 10
#Output the appropriate Roman Numeral

user_number = int(input("Enter a number: "))

if user_number < 1 or user_number > 10:
    print("ERROR, Enter a number between 1 and 10")
else:
    if user_number == 1:
        print("Roman Numeral: I")
    elif user_number == 2:
        print("Roman Numberal: II")
    elif user_number == 3:
        print("Roman Numeral: III")
    elif user_number == 4:
        print("Roman Numeral: IV")
    elif user_number == 5:
        print("Roman Numeral: V")
    elif user_number == 6:
        print("Roman Numeral: VI")
    elif user_number ==7:
        print("Roman Numeral: VII")
    elif user_number == 8:
        print("Roman Numeral: VIII")
    elif user_number == 9:
        print("Roman Numeral: IX")
    elif user_number == 10:
        print("Roman Numeral: X")

