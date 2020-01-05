# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 11:05
@file: 8函数场合.py
"""
# 我们一般在处理问题的时候,会把一个问题拆解成不同的情况,分别处理,这样很快就能实现程序
# 需要找出2-100之间的质数(素数),函数实现的方式
def num(number):
    list1 = []
    for i in range(2, number):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            list1.append(i)
    return list1

a = num(200)  # 调用函数,并传入参数
print(a)
