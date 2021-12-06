# This program displays a message to indicate the person's age
# group status.

person_age = int(input("Enter a person's age: "))

if person_age <= 1:
    print('Person is an infant.')
elif person_age > 1 and person_age < 13:
    print('Person is a child.')
elif person_age >= 13 and person_age < 20:
    print('Person is a teenager.')
else:
    print('Person is an adult.')