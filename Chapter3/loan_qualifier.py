# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0  # the minimum salary
MIN_YEARS = 2  # the minimum years on the job

salary = float(input('Enter your annual salary: '))

years_on_job = int(input('Enter the number of' + 'years employed: '))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed',
              'for at least', MIN_YEARS,
              'years to qualify.')
else:
    print('You must earn at least $',
          format(MIN_SALARY, ',.2f'),
          ' per year to qualify.', sep='')
