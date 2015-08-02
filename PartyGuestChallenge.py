__author__ = 'marlon.gray'
guests = []
name = ""
while name != " ":
   name = input("Please enter the  people you would like entering the party? \n(please press the space bar when you are finished!)").capitalize()
   guests.append(name)
if name == " ":
    guests.remove(" ")

guests.sort()
for guest in guests:
    print(guest)