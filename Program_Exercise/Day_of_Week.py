# This Program displays the corresponding day of the week.

number = int(input('Enter a number between 1 and 7: '))

if number >= 1 and number <= 7:
    if number == 1:
        print('Monday')
    elif number == 2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number == 4:
        print('Thursday')
    elif number == 5:
        print('Friday')
    elif number == 6:
        print('Saturday')
    elif number == 7:
        print('Sunday')
    else:
        print("You didn't enter a number between 1 and 7!")