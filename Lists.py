__author__ = 'marlon.gray'
guests = ["Christopher","Susan","Marlon","Alex"]
print(guests[0])

#update value in the list
guests[0] = "Steve"
print(guests[0])

#to add value to the list
guests.append("Jamie")
print(guests[-1])


#remove value from the list
guests.remove("Jamie")
print(guests[-1])

#delete items from the list
del guests[0]
print(guests[0])

print(guests.index("Marlon"))