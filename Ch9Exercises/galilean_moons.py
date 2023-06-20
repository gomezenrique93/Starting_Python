user_choice = input("Enter a choice to see the Galilean moons: ")

galilean_moons = { 'Io': [1821.6, 1.796, 1.769], 'Europa': [1560.8, 1.314, 3.551], 
                  'Ganymede': [2634.1, 1.428, 7.154], 'Calliso': [2410.3, 1.235, 16.689]}

if user_choice == 'Io':
    print(galilean_moons['Io'])
elif user_choice == 'Europa':
    print(galilean_moons['Europa'])
elif user_choice == 'Ganymde':
    print(galilean_moons['Ganymede'])
elif user_choice == 'Calliso':
    print(galilean_moons['Calliso'])
