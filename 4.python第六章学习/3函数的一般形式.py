# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/2 10:35
@file: 3函数的一般形式.py
"""


# 1.定义一个函数,比较两个数的大小,然后返回最大值
# def 定义函数,getmax函数名称,num1,num2形参
def getmax(num1, num2):
    # 11-15line(行)是函数体
    if num1 > num2:
        return num1
    else:
        return num2


num = getmax(100, 199)
print(num)
