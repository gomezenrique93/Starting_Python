# Get the number of hours worked
# Get the hourly pay rate.
# If the employee worked more than 40 hours:
# Calculate and display the gross pay with overtime.
# Else:
#   Calculate and display the gross pay as usual.
BASE_HOURS = 40
OT_MULTIPLIER = 1.5

hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    gross_pay = hours * pay_rate
else:
    gross_pay = hours * pay_rate

print('The gross pay is $', format(gross_pay, ',.2f'), sep='')
