__author__ = 'marlon.gray'
#initialize the variables
FathersName = ""
MothersNAme = ""
FirstSon = ""
FirstSonDescription = ""
SecondSon = ""
GrandFather = ""
GrandMother = ""
Country = ""
# Ask user for input
FirstSonAge = input("Enter First Son's Age")
FathersName = input("Enter Fathers Name")
MothersNAme = input("Enter Mothers Name")
FirstSon = input("Enter FirstSon Name")
FirstSonDescription = input("Enter First Son's Description")
SecondSon = input("Enter SecondSon Name")
GrandFather = input("Enter GrandFather Name")
GrandMother = input("Enter GrandMother Name")
Country = input("Enter Country Name")

print("Hello there my name is " + FathersName.capitalize() + " " + "\nI Have been married for 3 years")
print("My wife's name is " + MothersNAme.capitalize())
print("We have two sons " + "Their names are " + FirstSon + " " + SecondSon)
print(FirstSon + " is very " + FirstSonDescription + " He is " + FirstSonAge)
print("My Second child's name is " + SecondSon )
print("He was born 5 weeks ago" + "It has been a real challenge so far")
print( FirstSon + " loves to play Football " " his grandfather " + GrandFather + "\ntakes him to training.")
print("We are from " + Country + "," + "\nwe will be visiting in easter next year")