__author__ = 'mmwin8'
# If you are reading a csv file
# there is a csv library taht will help you

import csv
fileName = "challenge.csv"
READ = "r"
# with statement will open a file and close it when done
with open(fileName, READ) as myCSVFile:
    data = csv.reader(myCSVFile)
    for steps in data:
        print(';'.join(steps))
        for steps2 in steps:
            print(steps2)

