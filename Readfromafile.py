__author__ = 'mmwin8'
#Read all file content read
READ = "r"
fileName = "challenge.csv"
file = open(fileName, mode=READ)
fileContent = file.read()
print(fileContent)

#Read just tone row at a time readline
file = open(fileName, mode=READ)
firstRow = file.readline()
print(firstRow)
secondRow = file.readline()
print(secondRow)
file.close()

