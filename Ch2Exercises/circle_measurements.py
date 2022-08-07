import math

#ask user for radius
radius = input("Enter the radius of your circle: ")
radius = float(radius)

PI = math.pi

#calculate circumference
circumference = PI * (radius ** 2)

#calculate area
area = 2 * PI * radius

print('Circumference: ', circumference)
print('Area: ', area)

