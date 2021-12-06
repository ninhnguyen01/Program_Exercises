# This program keeps a running total of the number of bugs
# collected in a duration of 5 days.

MAX = 5
total_bugs = 0

for b in range(MAX):
    day_bugs = int(input('Enter the number of bugs discovered today: '))
    total_bugs += day_bugs
    print(total_bugs)