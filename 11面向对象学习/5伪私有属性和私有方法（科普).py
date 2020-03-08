# -*- coding: utf-8 -*-
# @Time    : 2020/02/07 14:29
# @Author  : xianming yu
# @File    : 5伪私有属性和私有方法（科普).py

"""
伪私有属性和私有方法（科普)
"""
"""
i1 提示
    在日常开发中,不要使用这种方式访问对象的私有属性 或 私有方法
i2 在python中没有真正意义的私有
    1.在给属性和方法命名时,实际是对名称做了一些特殊处理,使得外界无法访问
    2.处理方式:在名称前面加上 _类名__名称
i3 代码示例
    class Women:
        def __init__(self, name):
            self.name = name
            # 不要问女生的年龄
            self.__age = 18
        def __secret(self):
            print("我的年龄是 %d" % self.__age)
    调用:创建对象
        xiaofang = Women("小芳")
        # 私有属性，在外部访问的方式
        print(xiaofang._Women__age)
        # 私有方法，在外部调用方式
        xiaofang._Women__secret()
    输出结果:
        18
        我的年龄是 18
        
"""
