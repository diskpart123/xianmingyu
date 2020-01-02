# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/2 13:02
@file: 4函数执行过程.py
"""


def go1():
    print("go1 start")
    print("go1 end")


def go2():
    print("go2 start")
    print("go2 end")


def go3():
    print("go3 start")
    print("go3 end")


"""
调用上面的3个函数,go1(),go2(),go3(),它们执行的顺序从上到下执行,也就是瀑布模型(自上而下)
解释:在go1没有执行完之前go2是不会执行的,同样的原理go2执行完成后go3在执行,所以顺序是:go1,go2,go3
"""
go1()
go2()
go3()
