#Get the substance temperature
#As long as the temperature is greater than  102.5 degree Celsius:
# a. Tell the technician to turn down the thermostat, wait 5 minutes and then check the temperature
# b Get the substance's temperature
# c After the loop finishes, tell the technician that the temperature is acceptable and check it again in 15 minutes

MAX_TEMP = 102.5

temperature = float(input("Enter the substance's Celsius temperature: "))

while temperature > MAX_TEMP:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')
    temperature = float(input('Enter the new Celsius temperature: '))

print('The temperature is acceptable')
print('Check it again in 15 minutes')