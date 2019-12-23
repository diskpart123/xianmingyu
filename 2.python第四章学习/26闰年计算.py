year = eval(input("year:"))
month = eval(input("month:"))
day = ""
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if month == 2:
        day = 29
        print(year, "年", month, "月份有", day, "天")
else:
    if month == 1:
        day = 31
        print(year, "年", month, "月份有", day, "天")
    elif month == 2:
        day = 28
        print(year, "年", month, "月份有", day, "天")
    elif month == 3:
        day = 31
        print(year, "年", month, "月份有", day, "天")
    elif month == 4:
        day = 30
        print(year, "年", month, "月份有", day, "天")
    elif month == 5:
        day = 31
        print(year, "年", month, "月份有", day, "天")
    elif month == 6:
        day = 30
        print(year, "年", month, "月份有", day, "天")
    elif month == 7:
        day = 31
        print(year, "年", month, "月份有", day, "天")
    elif month == 8:
        day = 31
        print(year, "年", month, "月份有", day, "天")
    elif month == 9:
        day = 30
        print(year, "年", month, "月份有", day, "天")
    elif month == 10:
        day = 31
        print(year, "年", month, "月份有", day, "天")
    elif month == 11:
        day = 30
        print(year, "年", month, "月份有", day, "天")
    elif month == 12:
        day = 31
    else:
        print("输入有问题....")
