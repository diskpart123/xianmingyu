# -*- coding: utf-8 -*-
# @Time    : 2020/02/08 12:07
# @Author  : xianming yu
# @File    : 6单继承.py
"""
单继承学习
"""
"""
i1 目标
    i1.1 单继承
i2 面向对象三大特性
    i2.1 "封装"根据"职责"将"属性"和"方法"封装到一个抽象类中
    i2.2 "继承"实现代码的重用,相同的代码不需要重复的编写
    i2.3 "多态"不同的对象调用相同的方法,产生不同的执行结果,增加代码的灵活度
i3 单继承
    i3.1 继承的概念,语法和特点
        1.继承的概念:"子类"拥有"父类"的所有方法和属性
        2.继承的语法
            class 类名(父类名):
                pass
            2.1 "子类"继承自"父类",可以直接享受"父类"中已经封装好的方法，不需要再次开发
            2.2 "子类"中应该根据"职责",封装"子类"特有的属性和方法
        3.代码示例
            class Animate:
                def eat(self):
                    print("吃")
                def drink(self):
                    print("喝")
            class Dog(Animate): #Dog类继承Animate类
                def bark(self):
                    print("叫")
            调用:创建对象
                xiaotianquan=Dog()
                xiaotianquan.eat() #用Dog生成的对象调用Animate类的方法
            输出结果:
                吃
i4 专业术语
    i4.1 Dog类是Animal类的子类,Animal类是Dog类的父类,Dog类从Animal类继承
    i4.2 Dog类是Animal类的派生类,Animal类是Dog类的基类,Dog类从Animal类派生
i5 继承的传递性
    i5.1 C类从B类继承,B类又从A类继承
    i5.2 那么C类就具有B类和A类的所有属性和方法
    诠释:子类拥有父类以及父类的父类中封装的所有属性和方法
i6 问答题
    有4个类分别是A类,B类,C类,D类,其中B类继承A类,C类继承B类,D类继承A类,请问C类能
    够调用D类的方法吗?
    答案:不能,因为C类和D类之间没有继承关系       
"""
class Animate:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
class Dog1(Animate):
    def bark1(self):
        print("叫")
class Dog2(Animate):
    def bark2(self):
        print("叫")

xiaotianquan1=Dog1()
xiaotianquan2=Dog2()
xiaotianquan1.bark1()
xiaotianquan2.bark2()