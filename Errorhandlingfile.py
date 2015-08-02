__author__ = 'mmwin8'
fileName = ""
READ = "r"

fileName = input("Please enter the name of the file you would like to read?")
try:
    file = open(fileName,READ)
    filecontent = file.read()
    print(filecontent)
    file.close()
except:
    print("File could not be found")
