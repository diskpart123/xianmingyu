amount = 10000
n = 1
sum = 0

while n < 11:
    amount = amount * 1.05
    n +=1
    sum = sum + amount

print("十年之后的学费是：", round(amount,2),"从现在到十年之后的学费总和是：",round(sum,2))