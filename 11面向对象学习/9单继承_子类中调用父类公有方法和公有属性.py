# -*- coding: utf-8 -*-
# @Time    : 2020/02/09 20:07
# @Author  : xianming yu
# @File    : 9单继承_子类中调用父类公有方法和公有属性.py

"""
单继承_子类中调用父类公有方法和公有属性
"""
"""
i1 子类方法中调用父类的公有方法和公有属性
    class Animate:
        def __init__(self):
            self.name="diskpart" # 父类的公有属性
        def run(self):
            print("跑") #父类的公有方法
    class Dog(Animate):
        def bark(self):
            print("二郎神,叫...")
            self.run() #在子类中调用父类的公有方法
            print(self.name) #在子类中访问父类的公有属性
    调用:创建对象
        test=Dog() #子类创建test对象
        test.bark()
    输出结果:
        二郎神,叫...
        跑
        diskpart
"""

class Animate:
    count=0
    def __init__(self):
        self.name="diskpart" # 父类的实例属性
    def run(self):
        print("跑") #父类的公有方法
class Dog(Animate):
    def bark(self):
        print("二郎神,叫...")
        self.run() #在子类中调用父类的公有方法
        Animate.count+=1 #在子类中访问父类的类属性
        print(self.name) #在子类中访问父类的实例属性
