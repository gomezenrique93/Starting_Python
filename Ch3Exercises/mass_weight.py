#Prompt the user to enter the objects mass
mass = float(input("Enter your mass: "))

#Convert the users mass to weight
gravity = 9.80

weight = mass * gravity

if weight > 500:
    print("Your object weighs more than 500 newtons")
    print("It is too heavy")
elif weight < 100:
    print("Your object weighs less than 100 newtons")
    print("It is too light")


