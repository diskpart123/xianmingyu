amount = eval(input("Enter an amount, for example, 11.56: "))

amount = int(amount * 100)
numberofonedollars = amount // 100
amount = amount % 100

numberofquarters = amount // 25
amount = amount % 25

numberofdimes = amount // 10
amount = amount % 10

numberofnickels = amount // 5
amount = amount % 5

numberofpennies = amount

print("Your amount", amount, "consists of\n")

if numberofonedollars ==0:
    None
elif numberofonedollars == 1:
    print("\t", numberofonedollars, "dollar\n")
else:
    print("\t", numberofonedollars, "dollars\n")
if numberofquarters == 0:
    None
elif numberofquarters == 1:
    print("\t", numberofquarters, "quarter\n")
else:
    print("\t", numberofquarters, "quarters\n")
if numberofdimes == 0:
    None
elif numberofdimes == 1:
    print("\t", numberofdimes, "dime\n")
else:
    print("\t", numberofdimes, "dimes\n")
if numberofnickels == 0:
    None
elif numberofnickels == 1:
    print("\t", numberofnickels, "nickel\n")
else:
    print("\t", numberofnickels, "nickels\n")
if numberofpennies == 0:
    None
elif numberofpennies == 1:
    print("\t", numberofpennies, "penny\n")
else:
    print("\t", numberofpennies, "pennies\n")

#print("Your amount", amount, "consists of\n",
#      "\t", numberofonedollars, "dollars\n",
#      "\t", numberofquarters, "quarters\n",
#      "\t", numberofdimes, "dimes\n",
#      "\t", numberofnickels, "nickels\n",
#      "\t", numberofpennies, "pennies\n")
