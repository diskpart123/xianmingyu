
"""
is 成员运算符:判断内存地址是否一样
num1 = 3
num2 = 3
print(id(num1), id(num2))
if num1 is num2:
    print("num1和num2是同一个内存地址")
num2=4 #变更了num2这个对象的值为4
if num1 is num2:
    print("num1和num2是同一个内存地址")
else:
    print("两个地址不一样了")
"""

"""
is not 成员运算符:判断不是同一个地址

num3=5
num4=6
if num3 is not num4:
    print("两个变量对象的地址确实不一样....")
else:
    print("两个变量对象的地址一样")
"""

"""
总结:
    is和is not,结合上面的案例说明:编译器中有一个常量表,如num1=3,num2=4
    其中值3和4就存在常量表当中,且它们的内存地址不一样,如:3这个值的内存地址
    是:140712702931264,4这个值的内存地址是:140712702931296,这里的is和
    is not 判断的就是内存地址是否一样
"""
