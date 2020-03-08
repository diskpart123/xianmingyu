# -*- coding: utf-8 -*-
# @Time    : 2020/02/12 8:15
# @Author  : xianming yu
# @File    : 14类方法.py

"""
类方法
"""
"""
i1 类方法
    1."类属性"就是针对"类对象"定义的属性
        1.1 使用赋值语句(=)在class关键字下方定义类属性
        1.2 类属性用于记录与这个类相关的特征
    2."类方法"就是针对"类对象"定义的方法
        2.1 在类方法内部可以直接访问类属性,或者调用其它的类方法
    3.语法如下
        @classmethod
        def 类方法名(cls):
            pass
    4.类方法需要用修饰器@classmethod来标识,告诉解释器这是一个类方法
    5.类方法第一个参数是cls
        5.1 由哪一个类调用的方法,方法内的cls就是哪一个类的引用
        5.2 这个cls参数和"实例方法"的第一个参数self是类似的
        提示:使用其它名称也可以,不过习惯使用cls
    6.通过 "类名."调用类方法,调用方法时,不需要传递cls参数
    7.在方法的内部
        7.1 可以通用cls.访问类属性
        7.2 也可以使用cls.调用其他的类方法
    8.示例需求
        8.1 定义一个工具类
        8.2 每件工具都有自己的name
        需求
            在类中封装一个show_tool_count的类方法,输出当前使用的这个类,创建对象的个数
        代码实现
            class Tools(object):
                count=0
                def __init__(self,name):
                    self.name = name
                    Tools.count+=1
                @classmethod
                def show_tool_count(cls): #定义类方法
                    print("工具对象的数量是:%d"%cls.count) #在类方法中访问类属性
            调用:创建对象                
                tools1=Tools("斧头")
                tools2=Tools("榔头")
                Tools.show_tool_count() #通过"类名.类方法"的方式来调用
            输出结果:
                工具对象的数量是:2
    提示:在类方法内部,可以直接使用cls访问类属性,或者调用类方法            
            
"""

class Tools(object):
    count=0
    def __init__(self,name):
        self.name = name
        Tools.count+=1
    @classmethod
    def show_tool_count(cls): #定义类方法
        print("工具对象的数量是:%d"%cls.count) #在类方法中访问类属性
    @classmethod
    def test(cls):
        cls.show_tool_count() #通过cls.show_tool_count()访问类方法
tools1=Tools("斧头")
tools2=Tools("榔头")
Tools.show_tool_count()
Tools.test()