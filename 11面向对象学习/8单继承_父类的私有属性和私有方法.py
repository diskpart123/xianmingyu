# -*- coding: utf-8 -*-
# @Time    : 2020/02/09 12:43
# @Author  : xianming yu
# @File    : 8单继承_父类的私有属性和私有方法.py
"""
父类的私有属性和私有方法
"""
"""
i1. 子类对象不能在自己的方法内部,直接访问父类的"私有属性" 或 "私有方法"
i2. 子类对象可以通过父类的公有方法间接访问到父类的私有属性或私有方法,如下代码所示
    代码示例:
        class Animate:
            def __init__(self):
                self.__name="diskpart"
            def eat(self):
                print("吃...")
            def __run(self):
                print("跑")
        class Dog(Animate):
            def bark(self):
                print("二郎神,叫...")
        class XiaoTianQuan(Dog):
            def fly(self):
                print("飞跃...")
            def bark(self): #重写父类的方法,在 **子类中** 定义了一个 **和父类同名的方法并且实现**
                print("普通狗叫....")
                super().bark() # 利用super()来调用父类的方法
        调用:创建对象
            ceshi=XiaoTianQuan() #子类生成ceshi对象
            ceshi._Animate__run() #子类对象可以通过父类的公有方法间接访问到父类的"私有方法"
            print(ceshi._Animate__name) #子类对象可以通过父类的公有方法间接访问到父类的"私有属性"
        输出结果:
            跑
            diskpart            
    i2.1 私有属性和私有方法是对象的隐私,不对外公开,外界以及子类都不能直接访问
    i2.2 私有属性和私有方法通常用于做一些内部的事情
i3 子类方法中调用父类的公有方法和公有属性
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


