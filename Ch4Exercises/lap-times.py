#prompt user to enter the amount of times that they have run around a race track
laps = int(input("How many laps have you run? "))
total_time = 0
#use a loop to prompt the user to enter their lap time for each of their laps  
for i in range(laps):
    print("------------")
    print("Lap :", i + 1) 
    lap_time = float(input("Enter your lap time: ")) 
    total_time += lap_time
#when the loop finishes the program should display the time for the fastest lap,
#the time for their slowest lap
#their average lap time
