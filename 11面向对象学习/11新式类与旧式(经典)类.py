# -*- coding: utf-8 -*-
# @Time    : 2020/02/09 21:18
# @Author  : xianming yu
# @File    : 11新式类与旧式(经典)类.py

"""
新式类与旧式(经典)类
"""
"""
i1 说明
    object是Python为所有对象提供的"基类"，提供有一些内置的属性和方法，可以使用dir函数查看
i2 新式类
    以object为基类的类,推荐使用
i3 经典类
    不以object为基类的类,不推荐使用
i4 注意
    1.在Python3.x中定义类时,如果没有指定父类,会默认使用object作为该类的"基类"——Python3.x中定义的类都是"新式类"
    2.在Python2.x中定义类时,如果没有指定父类,则不会以object作为"基类"
    3.新式类和经典类在多继承时——会影响到方法的搜索顺序
i5 推荐
    1.为了保证编写的代码能够同时在Python2.x和Python3.x运行!今后在定义类时,如果没有父类,建议统一继承自object
    2.代码示例
        class 类名(object):
            pass
"""
class A:
    def test(self):
        print("xxxx")
print(dir(A))