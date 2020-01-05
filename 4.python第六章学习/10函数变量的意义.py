# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 21:10
@file: 10函数变量的意义.py
"""
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2

go=add #把add函数赋值给到go变量,go的本质是一个地址,修改地址实现不同的行为
print(go(5,3)) #调用go函数,然后传入两个参数
print(id(go),id(add)) #查看go函数与add函数的地址,得到两个相同的地址
print(type(go),type(add)) #查看go函数与add函数的数据类型,等到两个一样的function类型
print("------------------------")
#第一种函数赋值给到go变量
go=sub #把sub函数赋值给到go变量
print(go(5,3)) #调用go函数,然后传入两个参数
print(id(go),id(sub)) #查看go函数与sub函数的地址,得到两个相同的地址
print(type(go),type(sub)) #查看go函数与sub函数的数据类型,等到两个一样的function类型
print("------------------------")

#区别:
go1=add(1,2) #add(1,2) 为返回值
go2=add #函数类型的地址
print(type(go1),type(go2)) #所以得到结果:go1是int类型,go2是function


