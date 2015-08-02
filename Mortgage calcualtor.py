__author__ = 'marlon.gray'
# Declare and initialize the variables
monthlyPayment = 0
loanAmount = 0
interestRate = 0
numberOfPayment = 0
loanDurationInYears = 0

StrLoanAmount = input("How much is the loan?")
StrLoanInterest = input("How much is the interest Rate?")
StrLoanDuration  = input ("How many year will it take to pay off the loan?")

loanDurationInYears = float(StrLoanDuration)
loanAmount = float(StrLoanAmount)
interestRate = float(StrLoanInterest)

#Since payments are once per month, number of payments is number of years for the loan * 12
numberOfPayments = loanDurationInYears*12


MonthlyPayment = loanAmount*interestRate*(1+interestRate)*numberOfPayments /((1+interestRate)*numberOfPayments-1)
print("Monthly Payment will be {0:.2f} ".format(MonthlyPayment))