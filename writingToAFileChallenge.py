__author__ = 'marlon.gray'
WRITE = "w"
APPEND = "a"
names = ""
guests = []



fileName = "challenge.csv"
file = open(fileName,mode = WRITE)
file.write("Doyle Mcarty,27\n")
file.write("Jodi Mills,25\n")
file.write("Nicholas Rose,32\n")
file.write("Kian Goddard,36\n")
file.write("Zuha Hanania,26")

file.close()
print("File written sucessfully")

