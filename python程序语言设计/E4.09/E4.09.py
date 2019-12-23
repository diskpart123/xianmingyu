weight1, price1 = eval(input("Enter weight and price for package 1:"))
weight2, price2 = eval(input("Enter weight and price for package 2:"))

perprice1 = price1 / weight1
perprice2 = price2 / weight2

if perprice1 < perprice2:
    print("Package 1 has the better price.")
else:
    print("Package 2 has the better price.")
