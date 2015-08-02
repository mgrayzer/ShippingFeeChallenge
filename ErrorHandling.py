__author__ = 'marlon.gray'

import sys
first = input("enter first number: ")
second = input("enter second number ")

try:
    firstNumber = float(first)
except:
    sys.exc_info()[0]
    sys.exc_info()

try:
    secondNumber = float(second)
    # code in the except only runs if there is an error
except:
    print(sys.exc_info()[0])
    sys.exit()


# code in the except only runs if there is an error
try:
    result = firstNumber/ secondNumber
    print(result)
except ZeroDivisionError:
    print("the answer is infinity")
except:
    error  = sys.exc_info()[0]
    sys.exit()
    print("I am sorry something went wrong")
    print(error)
finally:
    print("I am sorry something went wrong")

