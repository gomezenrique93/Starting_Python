# This program will loop repeatedly and will tell the user to enter a word
# Once the user is tired of entering words, they should enter a space
# to signal that they are done entering words

# Will hold the total characters in a word
total = 0

truthy = True

total_inputs = 0

average = 0
# Will make sure that the user does not enter a space
while truthy == True:
    user_word = input("Please enter a word:")
    word_length = len(user_word)
    total += word_length
    total_inputs += 1
    if user_word == " ":
        truthy = False
        total_inputs -= 1

    average = total / total_inputs
print(total_inputs)
print(average)
   
