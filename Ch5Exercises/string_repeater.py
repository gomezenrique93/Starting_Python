def main():
    # Prompt the user for the string
    user_string = input("Enter the string that you would like to repeat! ")
    # Prompt the user for the amount of repeats
    user_repeat = int(input("Enter the amount of times you would like to repeat this: "))

    # Call to function
    print(string_repeater(user_string, user_repeat))

def string_repeater(string, repeats):
    # Returns the repeated string
    return string * repeats
main()

