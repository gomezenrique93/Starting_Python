#Prompt user to enter a month in numeric form
user_input_month = int(input("Enter a month in numerical form: "))

#Promt the user to enter a day in numeric form
user_input_day = int(input("Enter a day in numerical form: "))

#Prompt the user to enter a two digit year
user_input_year = int(input("Enter a two digit year: "))

magical_date = user_input_day * user_input_month

if magical_date == user_input_year:
    print("This is a magical date! :)")
else: 
    print("This is not a magiacal date! :(")