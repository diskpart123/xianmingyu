minutes = eval(input("Enter the number of minutes: "))
years = minutes//(60*24*365)
days = int((minutes%(60*24*365))/(60*24))
print(minutes,"minutes is approximately",years,"and",days)
