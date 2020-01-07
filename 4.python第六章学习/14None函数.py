# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/6 15:33
@file: 14None函数.py
"""
"""
定义一个没有返回值的函数,函数中没有return那么函数在调用时默认返回的是:None,
也可以在return后面不加任何值,那么返回的也是:None
"""
def go():
    print("go")
a=go()
print(a)
#输出结果:go,None

