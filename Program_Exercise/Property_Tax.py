# This program asks for the actual value of a piece of
# property and displays the assessment value and property
# tax.

actual_val = float(input("Enter the property's actual value: "))

def property_val():
    # assessment value is 60%.
    assess_val = actual_val * 60 / 100 

    # property tax is 72 cents for each $100 of the assessment value.
    property_tax = (assess_val / 100) * 0.72 
    print(assess_val)
    print(f'${property_tax:.2f}')

property_val()