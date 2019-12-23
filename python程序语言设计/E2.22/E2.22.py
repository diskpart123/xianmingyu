years = eval(input("Enter the number of years: "))
sec = years * 365 * 24 * 60 * 60
born = sec // 7
death = sec // 13
move = sec // 45
newpeople = 3120324986 + sec // 7 + sec // 45 - sec // 13
print("The population in",years,"years is",newpeople)
