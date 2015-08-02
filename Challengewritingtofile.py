__author__ = 'marlon.gray'

def writeText(data, fileName):
    file = open(fileName, mode = "w")
    file.write(data)
    return

writeText("marlon", "marlon.txt")