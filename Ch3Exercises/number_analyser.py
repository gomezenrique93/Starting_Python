#ask the user for an integer
#if number is greater than 0 print "Positive"
#if number is less than 0 print "Negative"
#if number is equal to 0 print "Zero"
#if number is even display "Even"
#if number is odd display "Odd"

user_number = input("Enter an integer ")

user_number = int(user_number)

if user_number < 0:
    print("Negative")
if user_number > 0:
    print("Positive")
if user_number == 0:
    print("Zero")
elif user_number % 2 == 0:
    print("Even")
elif user_number % 3 == 0:
    print("Odd")

