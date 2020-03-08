# -*- coding: utf-8 -*-
# @Time    : 2020/02/14 10:55
# @Author  : xianming yu
# @File    : 19单例设计.py

"""
单例
"""

"""
单例
    目标
        1.单例设计模式
        2.__new__方法
        3.Python举例
        
    i1 单例设计模式
        1.设计模式
            1.1 设计模式是"前人工作总结和提炼",通常被人们广泛流传的设计模式都是针对"某一特定问题"的成熟的解决方案
            1.2 使用设计模式是为了可重用代码,让代码更容易被他人理解,保证代码可靠性
        2.单例设计模式
            2.1 目的--让类创建的对象,在系统中只有"唯一的一个实例"
            2.2 每一次执行 "类名()"返回的对象,内存地址是相同的
    
    i2 单例设计模式的引用场景
        1.音乐播放对象
        2.回收站对象
        3.打印机对象
        4.等等....
    
    i3 __new__方法
        1.使用"类名()"创建对象时,python解释器首先会调用__new__方法为对象分配空间
        2.__new__是一个由object基类提供的内置静态方法,主要作用有两个:
            2.1 在内存中为对象分配空间
            2.2 返回对象的引用
        3.python解释器获得对象的引用后,将引用作为第一个参数,传递给__init__方法     
        4.重写 __new__方法一定要 return super().__new__(cls),否则Python解释器得不到
          分配空间的对象引用,就不会调用对象初始化方法
        5.注意:__new__是一个静态方法,在调用时需要主动传递cls参数
        6.代码示例:
            class MusicPlayer(object):
                def __new__(cls, *args, **kwargs):
                    # 如果不返回任何结果
                    return super().__new__(cls)
                def __init__(self):
                    print("初始化音乐播放对象")
            调用:创建对象
                player1=MusicPlayer()
                player2=MusicPlayer()
                print(player1)
                print(player2)
            输出结果:
                初始化音乐播放对象
                初始化音乐播放对象
                <__main__.MusicPlayer object at 0x000002095E999710>
                <__main__.MusicPlayer object at 0x000002095E999358>
    i4 python中的单例
        单例-让类创建的对象,在系统中只有唯一的一个实例
            1.定义一个类属性,初始值是None,用于记录单例对象的引用
            2.重写__new__方法
            3.如果类属性 is None,调用父类方法分配空间,并在类属性中记录结果
            4.返回类属性中记录的对象引用
        代码实现
            class MusicPlayer(object):
                # 记录第一个被创建对象的引用
                instance = None
                def __new__(cls, *args, **kwargs):
                    # 判断类属性是否是空对象
                    if cls.instance is None:
                        #调用父类的方法,为第一个对象分配空间
                        cls.instance =super().__new__(cls)
                    #返回的类属性保存的对象引用
                    return cls.instance
                    
                def __init__(self):
                    print("初始化音乐播放对象")
            
            #创建多个对象
                player1=MusicPlayer()
                player2=MusicPlayer()
                print(player1)
                print(player2)
            输出结果: (这样两个对象的返回的内存地址就是一样的)
                初始化音乐播放对象
                初始化音乐播放对象
                <__main__.MusicPlayer object at 0x0000018526659710>
                <__main__.MusicPlayer object at 0x0000018526659710>
    
    i5 只执行一次初始化工作
        1.在每一次使用"类名()"创建对象时,python的解释器都会自动的调用两个方法:
            __new__ 分配空间
            __init__ 对象初始化
        2.在上一小节对__new__方法改造之后,每次都会得到第一次被创建对象的引用
        3.但是初始化方法还会被再次调用
        4.需求
            让初始化对象只被执行一次
        5.解决办法
            1.定义一个类属性init_flag标记是否执行过初始化动作,初始值为:False
            2.在__init__方法中判断init_flag如果为False就执行初始化动作
            3.然后将init_flag设置为True
            4.这样再次自动调用__init__方法时,初始化动作就不会在执行了        
        6.代码实现
            class MusicPlayer(object):
                # 记录第一个被创建对象的引用
                instance = None
                #记录是否执行过初始化动作
                init_flag = False
                init_flag=False
                def __new__(cls, *args, **kwargs):
                    # 判断类属性是否是空对象
                    if cls.instance is None:
                        #调用父类的方法,为第一个对象分配空间
                        cls.instance =super().__new__(cls)
                    #返回的类属性保存的对象引用
                    return cls.instance
            
                def __init__(self):
                    # 判断类属性init_flag是否为False
                    if  MusicPlayer.init_flag==False:
                        print("初始化音乐播放对象")
                        #把类属性init_flag设置为True
                        MusicPlayer.init_flag=True

            #创建多个对象
                player1=MusicPlayer()
                player2=MusicPlayer()
                print(player1)
                print(player2) 
            输出结果:(创建了两个对象但是初始化方法只执行了一次,这样就达到了我们的需求目的)
                初始化音乐播放对象
                <__main__.MusicPlayer object at 0x000001C5B4DD9710>
                <__main__.MusicPlayer object at 0x000001C5B4DD9710>
                      
                
                 
"""
class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    #记录是否执行过初始化动作
    init_flag = False
    init_flag=False
    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
            #调用父类的方法,为第一个对象分配空间
            cls.instance =super().__new__(cls)
        #返回的类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 判断类属性init_flag是否为False
        if  MusicPlayer.init_flag==False:
            print("初始化音乐播放对象")
            #把类属性init_flag设置为True
            MusicPlayer.init_flag=True

#创建多个对象
player1=MusicPlayer()
player2=MusicPlayer()
print(player1)
print(player2)