# -*- coding: utf-8 -*-
# @Time    : 2020/02/07 14:08
# @Author  : xianming yu
# @File    : 4私有属性和私有方法.py

"""
私有属性和私有方法
"""
"""
i1 应用场景及定义方式
    i1.1 应用场景
        1.在实际开发中,对象的某些属性或方法可能只希望在对象的内部被使用,而不希望在外部被访问到
        2.私有属性就是对象不希望公开的属性
        3.私有方法就是对象不希望公开的方法
    i1.2 定义方式
        在定义属性或方法时,在属性名或者方法名前增加两个下划线,定义的就是私有属性或方法
        类  
            Women
        属性
            name
            __age 私有属性
        方法
            __init__(self,name)
            __secret(self) #私有方法
    i1.3 代码示例
        class Women:
            def __init__(self, name):
        
                self.name = name
                # 不要问女生的年龄
                self.__age = 18
        
            def __secret(self):
                print("我的年龄是 %d" % self.__age)
        调用:创建对象
            xiaofang = Women("小芳")
            # 私有属性，外部不能直接访问
            print(xiaofang.__age)
            # 私有方法，外部不能直接调用
            xiaofang.__secret() 

   
            
"""
class Women:
    def __init__(self, name):
        self.name = name
        # 不要问女生的年龄
        self.__age = 18
    def __secret(self):
        print("我的年龄是 %d" % self.__age)
xiaofang = Women("小芳")
# 私有属性，外部不能直接访问
print(xiaofang._Women__age)
# 私有方法，外部不能直接调用
xiaofang._Women__secret()