# -*- coding: utf-8 -*-
# @Time    : 2020/02/10 11:58
# @Author  : xianming yu
# @File    : 12多态.py

"""
多态
"""
"""
i1 多态
    1.不同的"子类对象"调用相同的"父类方法",产生不同的执行结果
    2.多态可以增加代码的灵活度
    3.以继承和重写父类方法为前提
    4.是调用方法的技巧,不会影响到类的内部设计
i2 多态案例演练
    需求如下:
        1 在Dog类封装方法 game
            普通狗只是简单的玩耍
        2 定义XiaoTianDog子类继承自Dog类,并且重写game方法
            哮天犬需要在天上玩耍
        3 定义Person类,并且封装一个和狗玩的方法
            在方法内部，直接让 **狗对象** 调用game方法
    设计
        Dog类设计
            属性
                name #狗的名字
            方法实现
                game() #普通狗只是简单的玩耍
        XiaoTianDog类设计
            属性
                继承父类(Dog)的属性,在XiaoTianDog创建对象的时候可以指定与父类不同的name属性
            方法实现
                game() #定义XiaoTianDog子类继承自Dog类,并且重写game方法
        Person类设计
            属性
                name #人的名字
            方法实现
                game_with_dog(self,dog) # 在方法内部，直接让"狗对象"调用'game'方法
    代码实现
        class Dog(object):
            def __init__(self,name):
                self.name = name
            def game(self):
                print("%s是一只普通狗..."%self.name)
        class XiaoTianDog(Dog):
            def game(self):
                print("%s是一只神狗..."%self.name)
        
        class Person(object):
            def __init__(self,name):
                self.name = name
            def game_with_dog(self,dog):
                print("%s和%s玩耍的很愉快!"%(self.name,dog.name))
        调用:创建对象        
            wangcai1=XiaoTianDog("飞天旺财")
            xiaoming1=Person("小明")
            xiaoming1.game_with_dog(wangcai1)
            wangcai2=XiaoTianDog("哈雷")
            xiaogang=Person("小刚")
            xiaogang.game_with_dog(wangcai2)
        输出结果:
            小明和飞天旺财玩耍的很愉快!
            小刚和哈雷玩耍的很愉快!
i3 案例小结
    i3.1 Person 类中只需要让狗对象调用game方法,而不关心具体是"什么狗"
    i3.2 game方法是在Dog父类中定义的
    i3.3 在程序执行时,传入不同的"狗对象"实参,就会产生不同的执行效果
    i3.4 "多态"更容易编写出出通用的代码,做出通用的编程,以适应需求的不断变化！
            
"""
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s是一只普通狗..."%self.name)
class XiaoTianDog(Dog):
    def game(self):
        print("%s是一只神狗..."%self.name)

class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s和%s玩耍的很愉快!"%(self.name,dog.name))
#调用:创建对象
wangcai1=XiaoTianDog("飞天旺财")
xiaoming1=Person("小明")
xiaoming1.game_with_dog(wangcai1)
wangcai2=XiaoTianDog("哈雷")
xiaogang=Person("小刚")
xiaogang.game_with_dog(wangcai2)