#"A" is the amount after the specified number of years (float)
#"P" is the principal amount that was originally deposited (float)
#"r" is the annual interest rate/100 (float)
#"n" is the number of times per year that the interest rate is compounded (int)
#"t" is the specified number of years (int)

#USER INPUT

#take in principal amount deposited
P = float(input("Enter your principal amount: "))
#take in the annual interest rate
r = float(input("Enter your annual interest rate: "))
#take in the amount of times interest will be compounded per year
n = int(input("How many times will interest rate be compounded?: "))
#take in the number of years the account will be left to accrue interest
t = int(input("How many years do you want to leave your money " + 
        " in your savings account?: "))

#ALGORITHM FOR CALCULATIONS
A = P*(1+((r/100)/n))**(n*t)

#print calculations
print('Total money accumulated $', format(A, '.2f'), sep='')



