#ask user to input charge for food
#calculate total
#display sales tax
#display tip 
#display total

food = input('How much did your food cost? ')
food_input = float(food)

#calculate sales tax
SALES_TAX = 0.07
tax = food_input * SALES_TAX

#calculate 18% tip
tip = food_input * 0.18

#calculate grand total
grand_total = food_input + tip + tax

print('Tax ', '$', format(tax, '.2f'), sep = '')
print('Tip ', '$', format(tip, '.2f'), sep = '')
print('Grand Total: ', '$', format(grand_total, '.2f'), sep = '')
