# This program will loop repeatedly and will tell the user to enter a word
# Once the user is tired of entering words, they should enter a space
# to signal that they are done entering words

# Will hold the total characters in a word
total = 0

# Holds default value to run loop
truthy = True

# Records total input
total_inputs = 0

# Will hold average
average = 0

# Will make sure that the user does not enter a space
while truthy == True:

    #Prompts user for the word
    user_word = input("Please enter a word:")

    # Will hold the length of the word
    word_length = len(user_word)

    # Will hold total word length
    total += word_length

    # Will record total length
    total_inputs += 1

    # Will check for a space
    if user_word == " ":
        truthy = False
        total_inputs -= 1

    # Calculates the average
    average = total // total_inputs

# Prints average word length
print("Average word length is",average)
   
