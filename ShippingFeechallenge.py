__author__ = 'mmwin8'

totalPurchase = 0
shippingFee = 10
totalPurchase = input("Please enter your purchase amount")
if float(totalPurchase) < 50:
    Total = float(totalPurchase) + float(shippingFee)
else:
    Total = float(totalPurchase)
print("Your total bill comes to ${0:.2f}".format(Total))

