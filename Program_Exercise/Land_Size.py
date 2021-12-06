# This program calculates the number of acres in a tract.

acre = 43560
square_feet_input = input('Enter the total square feet in a land: ')
square_feet = float(square_feet_input)
total_acre = square_feet / acre
print(f'{total_acre:,.2f}')