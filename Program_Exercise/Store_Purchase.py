# This program calculates a customer's store purchase.

item_price = float(input('Enter the price for each item: '))
sub_total = item_price
sales_tax = .07
total = sub_total * sales_tax
print(total)