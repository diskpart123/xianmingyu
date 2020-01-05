# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 21:40
@file: 11函数变量用途.py
"""
#业务层代码
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def getmax(num1,num2):
    return num1 if num1 > num2 else num2

#核心层代码,也称之为接口
def Test( go,num1,num2):
    return go(num1,num2)

#通过核心层代码调用业务层代码,注意:一般情况下核心层代码是不变的,变化的是业务层代码
print(Test(add,1,2))
print(Test(sub,4,3))
print(Test(getmax,5,3))


