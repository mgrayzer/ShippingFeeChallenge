__author__ = 'marlon.gray'
country = ""
province = ""
totalWoTax = 0
totalWTax = 0

GST = .05
HST = .13
PST = .06

totalWoTax = float(input("How much is your order total?"))
country = input("Which country are you ordering from?").upper()


if country == "CANADA":
    province = input("Which province are you from?").upper()

if country == "CANADA":
    if province == "ALBERTA":
        totalWTax = totalWoTax * GST + totalWoTax
    elif province == "ONTARIO" or province == "NEW BRUNSWICK" or province == "NOVA SCOTIA":
        totalWTax = totalWoTax * HST + totalWoTax
    else:
        totalWTax = totalWoTax * GST + totalWoTax * PST + totalWoTax

if country != "CANADA":
    totalWTax =totalWoTax
print("Your Total including taxes comes to ${0:.2f}".format(totalWTax))

