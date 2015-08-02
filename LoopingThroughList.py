__author__ = 'marlon.gray'

guests = ["Christopher","Susan","Marlon","Alex","Luca","Adrian"]
# option one for looping through a list
nbrValueInList = len(guests)
for steps in range(nbrValueInList):
    print(guests[steps])

# option two for looping through a list
for guest in guests:
    print(guest)

#option for sorting list
guests.sort()
print(guests)