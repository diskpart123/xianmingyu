""""
输入3个整数,然后按照从大到小的顺序排列显示,并且求出最大整数
"""
a, b, c = eval(input("a,b,c:"))
if a > b > c:
    print(a, b, c)
    print(max(a, b, c))
elif a > c > b:
    print(a, c, b)
    print(max(a, b, c))
elif b > a > c:
    print(b, a, c)
    print(max(a, b, c))
elif b > c > a:
    print(b, c, a)
    print(max(a, b, c))
elif c > a > b:
    print(c, a, b)
    print(max(a, b, c))
elif c > b > a:
    print(c, b, a)
    print(max(a, b, c))
