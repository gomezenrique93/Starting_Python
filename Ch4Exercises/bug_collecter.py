#This program will collect bugs for five days

#Number of days that bugs will be collected
total_days = 5

#Accumulator variable for total_bugs
total_bugs = 0

for days in range(total_days):
    print('--------------')
    print('Day: ', days + 1)
    bugs = int(input('How many bugs did you collect? '))
    total_bugs += bugs

print('\n')
print('Total bugs collected is ', total_bugs)