user_number = int(input("Enter a non-negative number: "))

factorial = 0

for i in range(user_number + 1):
    factorial = i * (user_number - 1)

print(factorial)
