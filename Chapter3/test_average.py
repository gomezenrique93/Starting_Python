# Get the first score
# Get the second score
# Get the third test score
# Calculate the average
# Display the average
# If average is greater than 95:
#   Congratulate user

first_score = float(input('Enter your first score: '))
second_score = float(input('Enter your second score: '))
third_score = float(input('Enter your third score: '))

number_of_scores = 3.0

average = (first_score + second_score + third_score) / number_of_scores

print('Your average is: ', format(average, '.2f'))

if average > 95:
    print('Congratulations your killing it!!')
