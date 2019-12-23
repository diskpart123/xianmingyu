def getpentagonalnumber(n):
    return n * ( 3 * n - 1 ) / 2

n = eval(input("请输入n:"))

print(int(getpentagonalnumber(n)))