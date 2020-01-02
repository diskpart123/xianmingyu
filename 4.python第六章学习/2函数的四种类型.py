# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/2 10:06
@file: 2函数的四种类型.py
"""
"""
1.没有参数,没有返回值
def go():
    print("Hello world!")
go() #调用函数
"""

"""
2.调用go()函数10次
def go():
    print("Hello world!")
for i in range(10):
    go()
"""

"""
3.有参数,没有返回值
def goprint(num):
    print("Hello",num)
goprint("Python") #调用函数,并输入参数
"""

"""
4.调用goprint(num)函数10次
def goprint(num):
    print("Hello",num)
for i in range(10):
    goprint(i)
"""

"""
5.无输入,无参数,有返回值,记住:return代表是返回值,函数中程序只要执行到return,那么整个函数体就结束了
import random
def getdata():
    return random.randint(0,100)
for i in range(10):
    a=getdata()
    print(a)
"""
"""
6.有输入(输入实参),有参数(形参),有返回值
def add(num1,num2): #两个形参
    return num1+num2
num=add(1,2) #输入实参
print(num)
"""