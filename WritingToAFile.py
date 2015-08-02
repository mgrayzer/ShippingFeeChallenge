__author__ = 'marlon.gray'
# C:\Users\marlon.gray\PycharmProjects\untitled2\Python practice\WritingToAFile.py

# access modes in python r = read the file w = write to the file a = Append to the existing file content b = open a binary file

#example for text files
fileName = "marlon.txt"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"

file = open(fileName, mode = APPEND)
file.write("\nHello how are you doing?\n")
file.write("What are you doing this weekend?")

file.close()
print("file written successfully :).")

# example for csv files
fileName = "example.csv"

file = open(fileName, mode = APPEND)
file.write("\nMarlon,30\n")
file.write("ken,33\n")
file.write("will,33")
file.close()