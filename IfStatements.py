__author__ = 'marlon.gray'
#python is case sensitive
# Answer = input("Would you like express shipping?")
# if Answer == "Yes":
#     print("That will be an extra $10")
# if Answer == "No":
#      print("There will be no shipment cost")
#
# favouriteTeam = input("What is your favourite football team?")
# if favouriteTeam.capitalize() == "Eagles":
#     print("Fight eagles fight")
# print("It's Okay if you prefer football/soccer")

#You Can use boolean variables to remember if a condition is true or false
# if with numbers

deposit = int(input("How much do you want to deposit?"))
if deposit > 100:
    print("Enjoy your toaster!")
else:
    print("Enjoy your mug!")
print("Have a nice day")

freeToaster = False
deposit = int(input("How much do you want to deposit?"))
if deposit > 100:
    freeToaster = True
if freeToaster:
    print("enjoy your toaster")
else:
    print("Have a nice day")