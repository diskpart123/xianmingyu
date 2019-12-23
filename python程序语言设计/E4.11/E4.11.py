year = eval(input("Enter a year:"))
month = eval(input("Enter a month:"))

isleapyear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
day1 = ( month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or \
    month == 10 or month == 12 )
day2 = (month == 2)

if day1:
    print(year, "years", month, "month has 31 days")
elif ( day2 and isleapyear ):
    print(year, "years", month,"month has 29 days")
elif ( day2 and ( not isleapyear ) ):
    print(year, "years", month,"month has 28 days")
else:
    print(year, "years", month, "month has 30 days")