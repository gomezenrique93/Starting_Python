# "V" is the number of grape vines that will fit in a row
# "R" is the length of the row, in feet.
# "E" is the amount of space, in feet, used by an end-post assebmly.
# S is the space between vines, in feet.

#V = (R-(2*E))/S

#Prompt the user to enter the length of the row "V"
R = int(input("Enter the length of the row in feet: "))
E = int(input("Enter the amount of space between the end post assembly: "))
S = int(input("Enter the amount of space between the vines: "))

V = (R-(2*E))/S

print("Total number of grapevines ", V)

