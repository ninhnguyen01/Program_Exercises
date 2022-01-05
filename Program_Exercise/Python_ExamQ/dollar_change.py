# This program gives you the change from a dollar amount
# between 0.01 and 0.99.
# This program was a question on a midterm for a programming
# course.
# This program is a modification and a correction from the 
# original program that was not completely correct in output.

dollar_amount = float(input('Please enter a dollar amount between 0.01 and 0.99: '))

conversion = dollar_amount * 100
dollar = int(conversion)

quarter = 25
quarters = dollar // quarter
dollar = dollar % quarter

nickel = 5
nickels = dollar // nickel
dollar = dollar % nickel


penny = 1
pennies = dollar // penny

print(f'Your change is: {quarters} quarters, {nickels} nickels, and {pennies} pennies. ')

# End