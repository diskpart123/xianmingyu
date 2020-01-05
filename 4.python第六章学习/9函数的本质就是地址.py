# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 21:03
@file: 9函数的本质就是地址.py
"""


# 函数的本质其实就是一个地址
def add(num1, num2):
    return num1 + num2


print(id(add))  # 查看函数的内存地址
print(type(add))  # 查看函数类型
