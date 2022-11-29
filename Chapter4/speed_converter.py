START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

#Print the table headings
print('KPH\t\MPH')
print('---------')

for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))