user_number = int(input("Enter a number: "))

factorial = 1

for i in range(1, user_number + 1):
    factorial = factorial * i

print(factorial)
