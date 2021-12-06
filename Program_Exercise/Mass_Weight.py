# This program asks the user to enter an object's mass
# to calculate its weight.

mass = float(input("Enter an object's mass: " ))

weight = mass * 9.8
print(weight)

newtons1 = 500
newtons2 = 100

if weight > newtons1:
    print('Object is too heavy.')

if weight < newtons2: 
        print('Object is too light.')