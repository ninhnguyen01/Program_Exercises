# This program prompts the user to enter their account's present
# value, monthly interest rate, and the number of months that the 
# money will be left in the account to estimate the account's
# future value.

def savings():  
    p = float(input("Enter current bank balance: ")) 
    i = float(input("Enter interest rate: ")) 
    t = float(input("Enter the number of months: ")) 
    total = p * (1 + i)**t
    print(f'${total:,.2f}')

savings()