# 判断输入金额的尾数是不是大于0.03

money = eval(input("请输入金额>:"))

money_test = (money * 10 - (int(money * 10))) / 10

print(money_test)
