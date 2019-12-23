# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 15:21
# @Author  : xianming yu
# @File    : 28等价循环.py

# 循环等价处理1
num = 0
while num < 10:
    print(num)
    num += 1

# 循环等价处理2
for i in range(10):
    print(i)

# 循环等价处理3
num = 0
while True:
    num += 1
    print(num)
    if num == 9:
        break
