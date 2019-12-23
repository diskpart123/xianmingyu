rate = eval(input("Enter the exchange rate from dollars to RMB: "))
convert = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if convert == 0:
    dollars = eval(input("Enter the dollars amount: "))
    amount = dollars * rate
    print("$",dollars,"is",amount,"yuan.")
elif convert == 1:
    rmb =eval(input("Enter the RMB amount: "))
    amount = rmb / rate
    print(rmb,"yuan is $",round(amount,2))
else:
    print("Incorrect input")