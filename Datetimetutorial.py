__author__ = 'marlon.gray'
# The datetime class allows us to get the current date and time
# The import Statement gives us access to
# the functionality of the datetime class
import datetime


currentDate = datetime.date.today()
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

# strftime allows you to specify the date format
print(currentDate.strftime('%Y/%m/%d'))

# Please attend our event Sunday, July 20 in the year 1997

#print(currentDate.strftime
      #('Please attend our event %A, %B %d in the year %Y'))

# The Strptime function allows you to convert a string to date
birthday = input("What is your birthday? (mm/dd/yyyy)")
birthdate = datetime.datetime.strptime(birthday,"%m/%d/%Y").date()

# why did we list datetime twice?
# because we are calling the strptime function
# which is part of the datetime class
# which is in the datetime module

print("Your birth date is " + birthdate.strftime('%Y/%m/%d'))

#days = birthdate - currentDate
#print(days)

currentDate = datetime.datetime.now()
print(datetime.datetime.strftime(currentDate,'%H:%M'))
print(currentDate.minute)