#ask user for the total number of students
#ask user how many females there are
#ask user how many males there are
#calculate percentage of males
#calculate percentage of females

total_students = input("How many students are in your class? ")
total_students = int(total_students)

male_students = input("How many of those students are male? ")
male_students = int(male_students)

female_students = input("How many of those students are female? ")
female_students = int(female_students)

male_percentage = (male_students / total_students) * 100
print('Percentage of male students is', format(male_percentage, '.2f'), '%')

female_percentage = (female_students / total_students) * 100
print('Percentage of female students is', format(female_percentage, '.2f'), '%')
