amount = eval(input("Enter the monthly saving amount: "))
rate = (1 + 0.00417)
am1 = amount * rate
am2 = (amount + am1) * rate
am3 = (amount + am2) * rate
am4 = (amount + am3) * rate
am5 = (amount + am4) * rate
am6 = (amount + am5) * rate
print("After the sixth month, the account value is",round(am6,2))
