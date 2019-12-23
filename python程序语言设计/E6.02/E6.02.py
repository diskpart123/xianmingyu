def sumdigits(n):
    sum = 0
    while n >= 10:
        sum = n % 10 + sum
        n = n // 10
    sum = sum + n
    return sum

num = eval(input("请输入一个整数："))

print(sumdigits(num))
