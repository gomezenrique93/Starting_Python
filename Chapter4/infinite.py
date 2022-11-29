#This program demonstrates an infinite loop

keep_going = 'y'

#Warning this is the infinite loop
while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    commission = sales * comm_rate

    print('The commission is $',
            format(commission, '.2f'), sep='')