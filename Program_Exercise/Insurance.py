# This program asks the user to enter the replacement cost 
# of a building, then displays the minimum amount of insurance
# they should buy for the property.

# Based on the insurance advice of at least 80%.

cost = float(input('Enter the replacement cost for the building: '))

def estimate():
    insurance = cost * 80 /100
    print(f'Minimum recommended insurance: {insurance:,.2f} ')

estimate() 