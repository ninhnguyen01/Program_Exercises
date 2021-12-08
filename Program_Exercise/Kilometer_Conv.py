# This program asks the user to enter a distance in kilometers,
# then converts that distance to miles.

distance = float(input('Enter distance in kilometer: '))

def distance_convert():
    conversion = 0.6214
    miles = distance * conversion    
    print(f'{miles:.1f}')

distance_convert()