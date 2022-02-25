#Have the user enter amounts for 5 items
#Display the sub_total
#Calculate sales_tax = sub_total * tax_percentage
#Display sales_tax
#Display final_total = sub_total - sales_tax 

item_1 = float(input('Please enter the amount for item 1'))
item_2 = float(input('Please enter the amount for item 2'))
item_3 = float(input('Please enter the amount for item 3'))
item_4 = float(input('Please enter the amount for item 4'))
item_5 = float(input('Please enter the amount for item 5'))

#Calculating sub total
sub_total = item_1 + item_2 + item_3 + item_4 + item_5

#Calculating sales tax
TAX_PERCENTAGE = 0.7 
sales_tax = sub_total * TAX_PERCENTAGE

#Calculating final total 
final_total = sub_total - sales_tax





