# This program calculates the average amount of rainfall 
# over a given span of time from the user input.

years = int(input('Enter the number of years: '))
total = 0

for year in range(1,years+1):
    for month in range(1,13):
        rainfall = float(input('Enter inches of rainfall this month: '))
        total += rainfall
        mon = years * 12
        avg = total / month
        print(month,avg,total)