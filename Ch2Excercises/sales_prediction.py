#Collect total amount of sales from the user
#Calculate annual profit
#Annual profit is total sales * 23% of sales

total_sales = float(input("Enter the total amount of sales: "))
PERCENT_SALES = 0.23
annual_profit = total_sales * PERCENT_SALES

print("Total sales $",format(annual_profit, ",.2f"))
