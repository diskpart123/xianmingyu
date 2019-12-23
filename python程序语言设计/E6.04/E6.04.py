def reverse(n):
    m = 0
    while n >= 10:
        m = n % 10 + m * 10
        n = n // 10
    m = m * 10 + n
    return m

number = eval(input("请输入一个整数："))

print(reverse(number))
