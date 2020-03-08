# -*- coding: utf-8 -*-
# @Time    : 2020/02/12 9:07
# @Author  : xianming yu
# @File    : 15静态方法.py

"""
静态方法
"""
"""
i1 静态方法
    1.在开发时,如果需要在"类"封装一个方法,这个方法:
        1.1 既不需要访问"实例属性",或者调用"实例方法"
        1.2 也不需要访问"类属性",或者调用"类方法"
        那么这个时候,可以把这个方法封装成一个"静态方法"
    2.语法如下
        @staticmethod
        def 静态方法名():
            pass
    3."静态方法"需要使用"修饰器"@staticmethod来标识,告诉解释器这是一个静态方法
    4.通过"类名.静态方法()"来调用静态方法
    5.代码示例
        class Dog(object):
            @staticmethod #加上@staticmethod来标识,告诉解释器这是一个静态方法
            def run(): #定义静态方法
                print("小狗快乐的跑....")
        调用静态方法
            Dog.run()
        输出结果:
            小狗快乐的跑....      
        
"""
class Dog(object):
    @staticmethod #加上@staticmethod来标识,告诉解释器这是一个静态方法
    def run(): #定义静态方法
        print("小狗快乐的跑....")
Dog.run()