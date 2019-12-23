M = eval(input("Enter the amount of water in kilograms: "))
intemp = eval(input("Enter the initial temperature:"))
fintemp = eval(input("Enter the final temperature:"))
print("The energry needed is",M * (fintemp - intemp) * 4184)
