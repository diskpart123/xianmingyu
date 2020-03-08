# -*- coding: utf-8 -*-
# @Time    : 2020/02/09 20:34
# @Author  : xianming yu
# @File    : 10多继承.py

"""
多继承
"""
"""
i1 概念
    1.子类可以拥有多个父类,并且具有所有父类的属性和方法
        例如:孩子会继承父亲和母亲的特性
i2 语法
    class 子类名(父类名1,父类名2...):
        pass
i3 多继承的使用注意事项
    1.问题提出
        如果"不同的父类" 中存在 "同名的方法"，"子类对象" 在调用方法时，会调用哪一个父类中的方法呢？
    2.提示
        开发时,应该尽量避免上面问题提出产生混淆的情况！—— 如果"父类之间" 存在"同名的属性或者方法,应该"尽量避免"使用多继承
    3.多继承代码示例
        class A:
            def test(self):
                print("A_test")
            def demo(self):
                print("A_demo")
        class B:
            def demo(self):
                print("B_demo")
            def test(self):
                print("B_test")
        class C(A,B): #C类同时继承A类和B类
            pass
        上面的代码"不同的父类" 中存在 "同名的方法",子类对象在调用方法时，会调用哪一个父类中的方法呢？我们可以用python的内置
        方法__mro__来看一下可以查看"方法" 搜索顺序,代码如下:
        print(C.__mro__)
        输出结果:
          (<class '__main__.C'>, <class '__main__.F'>, <class '__main__.B'>, <class 'object'>)
i4 Python中的 MRO —— 方法搜索顺序
    1.Python中针对"类"提供了一个"内置属性"__mro__可以查看"方法"搜索顺序
    2.mro 是 method resolution order,主要用于"在多继承时判断 方法,属性的调用路径
    3.语法如下
        print(C.__mro__)
        输出结果:
            (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>) 
    4.注意点
        1.在搜索方法时，是按照 __mro__ 的输出结果 "从左至右" 的顺序查找的
        2.如果在当前类中 "找到方法,就直接执行,不再搜索
        3.如果 "没有找到,就查找下一个类中是否有对应的方法,如果找到，就直接执行，不再搜索
        4.如果找到最后一个类，还没有找到方法，程序报错
        
    
            
"""
class F:
    def test(self):
        print("A_test")
    def demo(self):
        print("A_demo")
class B:
    def demo(self):
        print("B_demo")
    def test(self):
        print("B_test")
class C(F,B):
    pass
print(C.__mro__)