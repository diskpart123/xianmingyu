# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/2 13:47
@file: 6函数复合调用执行过程.py
"""

def go1():
    print("go1 start")
    go2()
    print("go1 end")


def go2():
    print("go2 start")
    go3()
    print("go2 end")


def go3():
    print("go3 start")
    print("go3 end")

go1()
"""
当用户执行go1()函数,程序会跳转到go1()函数体,执行第一条语句print(“go start”),
然后在执行第二行的go2()函数,此时程序会跳转到go2()函数体,然后在
执行go2()函数下的第一条语句print(“go2 start”),然后在执行第二行的go3()函数,
此时程序会跳转到go3()函数体,然后在执行go3()函数下的第一条语句print(“go3 start”)
和第二条语句print(“go3 end”),执行完go3()函数后,程序会跳转到go2()函数下执行print(“go2 end”),
执行完go2()函数后,程序会跳转到go1()函数下执行print(“go1 end”),
此时go1()函数执行完成
"""

