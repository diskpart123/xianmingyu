# -*- coding: utf-8 -*-
# @Time    : 2020/02/09 12:02
# @Author  : xianming yu
# @File    : 7单继承_方法的重写.py

"""
方法的重写
"""
"""
i1 应用场景
    当 父类的方法实现不能满足子类需求时，可以对方法进行重写(override)
i2 重写父类方法的两种情况
    1.覆盖父类的方法
    2.对父类进行扩展
i3 覆盖父类的方法
    1.如果在开发中,父类的方法实现 和 子类的方法实现,完全不同就可以
      使用"覆盖" 的方式,"在子类中" 重新编写 父类的方法实现
    2.具体实现的方法
      就相当于在子类中定义了一个和父类同名的方法并且实现
    3.重写之后,在运行时,只会调用子类中重写的方法,而不再会调用父类封装的方法
    4.代码示例
        class Animate:
            def eat(self):
                print("吃...")
            def run(self):
                print("跑")
        class Dog(Animate):
            def bark(self):
                print("二郎神,叫...")
        class XiaoTianQuan(Dog):
            def fly(self):
                print("飞跃...")
            def bark(self): #重写父类的方法,在 **子类中** 定义了一个 **和父类同名的方法并且实现**
                print("普通狗叫....")
        调用:创建对象
            ceshi=XiaoTianQuan()
            ceshi.bark() #调用子类中重写父类的方法
        输出结果:
            普通狗叫....       
i4 对父类方法进行扩展
    1.如果在开发中,子类的方法实现中包含父类的方法实现
        父类原本封装的方法实现是子类方法的一部分
    2.使用扩展的方式
        2.1 在子类中重写父类的方法
        2.2 在需要的位置使用super().父类方法,来调用父类的方法执行
        2.3 代码其他的位置针对子类的需求,编写子类特有的代码实现
    3.关于super
        3.1 在python中super是一个特殊的类
        3.2 super() 就是使用 super类创建出来的对象
        3.3 最常使用的场景就是在,重写父类方法时,调用在父类中封装的方法实现
    4.代码示例
        class Animate:
            def eat(self):
                print("吃...")
            def run(self):
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
            ceshi=XiaoTianQuan()
            ceshi.bark()
        输出结果:
            普通狗叫....
            二郎神,叫... 
    5.提示
        1.在开发时，`父类名` 和 `super()` 两种方式不要混用
        2.如果使用 **当前子类名** 调用方法，会形成递归调用，**出现死循环**
        
              
"""
class Animate:
    def eat(self):
        print("吃...")
    def run(self):
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

ceshi=XiaoTianQuan()
ceshi.bark()