# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 22:05
@file: 12装饰器设计模式.py
"""
import time


def getcosttime(test):
    start_time = time.time()
    test()
    end_time = time.time()
    time_t = end_time - start_time
    print(time_t)


def go1():
    count = 0
    for i in range(100000000):
        count += i
    print(count)


def come():
    count = 0.0
    for i in range(10):
        count += i
    print(count)


"""
解释:我们可以在调用getcosttime函数的时候把come这个函数当作参数的方式传递进去
在getcosttime函数第23行的test()就代表come这个函数,同理我们也可以把go1这个
函数当作参数的方式传递给到getcosttime函数
"""
#
getcosttime(come)  # 测试come这个函数执行用了多长时间
print("-------------------------")
getcosttime(go1)  # 测试go1这个函数执行用了多长时间
