def futureinvestmentvalue(investmentamount,monthlyterestrate,years):
    acc = investmentamount * (1 + monthlyterestrate / 100) ** (years * 12)
    return round(acc,2)

amount = eval(input("The amount invested:"))
rate = eval(input("Annual interest rate:"))

print("Years","    ","Future Value")

for i in range(1,31):
    num = futureinvestmentvalue(amount,rate / 12,i)
    print(i,"          ",num)
