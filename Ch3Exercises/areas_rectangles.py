#ask for the length of first rectangle
#ask for the width of the first rectangle
#ask for the length of second rectangle
#ask for the width of the second rectangle

length_one = float(input("Enter length for first rectangle: "))
width_one = float(input("Enter width for first rectangle: "))

length_two = float(input("Enter length for second rectangle: "))
width_two = float(input("Enter width for second rectangle: "))

area_one = length_one * width_one
area_two = length_two * width_two

if area_one > area_two:
    print("Area one is greater than area two")
elif area_two > area_one:
    print("Area two is greater than area one")
elif area_two == area_one: 
    print("Area one is equal to area two")
