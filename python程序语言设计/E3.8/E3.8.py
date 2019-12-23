amount = eval(input("Enter an amount, for example, 1156: "))

numberofonedollars = amount // 100
amount = amount % 100

numberofquarters = amount // 25
amount = amount % 25

numberofdimes = amount // 10
amount = amount % 10

numberofnickels = amount // 5
amount = amount % 5

numberofpennies = amount

print("Your amount", amount, "consists of\n",
      "\t", numberofonedollars, "dollars\n",
      "\t", numberofquarters, "quarters\n",
      "\t", numberofdimes, "dimes\n",
      "\t", numberofnickels, "nickels\n",
      "\t", numberofpennies, "pennies\n")
