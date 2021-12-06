# This program displays the following information of
# a person's stock transaction.

# Purchase
shares_purchased = 2000
price_per_share = 40.00

money_paid = shares_purchased * price_per_share
commission_fee = 0.03
commission_paid = (shares_purchased * price_per_share) * commission_fee
total_paid = money_paid + commission_paid

# Sold
shares_sold = 2000
price_per_share_sold = 42.75

money_paid2 = shares_sold * price_per_share_sold
commission_fee2 = 0.03
commission_paid2 = (shares_sold * price_per_share) * commission_fee2
total_sold = money_paid2 - commission_paid2

total_money = total_sold - total_paid
print(total_money)