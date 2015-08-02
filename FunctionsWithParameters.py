__author__ = 'marlon.gray'
# parameter is a variable for a function
# inside the function, parameters behave like a variable

def main():
    names = getNames()
    printNames()
    return

def getNames():
    names = ["Christopher","Susan","Danny"]
    newName = input("Enter last guest:")
    names.append(newName)
    return names


def printNames(names):
     for name in names:
         print(name)
     return

main()



# def getMessage(name):
#     message = "Hello, " + name
#     return message
#
# def printMessage(message):
#     print(message)
#     return
# output = getMessage(input("what is your name?"))
# print(output)