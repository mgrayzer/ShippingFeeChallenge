__author__ = 'marlon.gray'
import datetime

CurrentDate = datetime.date.today()
print(CurrentDate)

DeadLine = input("When is your project deadline? (YYYY/MM/DD)")

DeadLine = datetime.datetime.strptime(DeadLine, '%Y/%m/%d').date()
TimeRemaining = DeadLine - CurrentDate
NmbrWeeks = TimeRemaining.days/7
#print(TimeRemaining.days)
#print(NmbrWeeks)
print("You have {0:.1f} weeks ".format(NmbrWeeks)+\
      "or {0:.0f} days remaining to deadline".format(TimeRemaining.days) )