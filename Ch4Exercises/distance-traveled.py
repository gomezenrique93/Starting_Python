#This program will ask the user for the speed of a vehicle(in miles per hour)
#It should then ask the user how many hours they've travelled
#Use a loop to display the distance the vehicle has travelled

#Prompt user for speed of the vehicle
speed = int(input("What is the speed of the vehicle in mph? "))

#Prompt the user for the travel time
hours = int(input("How many hours has it traveled? "))

#Initialize accumulator to store distance
distance = 0

print("Hour\tDistance Travelled")
for time in range(hours):
    #Algorithm to calculate distance
    distance = speed * (time + 1)

    #Will print distance and time for variable
    print(time+1,"\t",distance)
