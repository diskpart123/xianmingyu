# -*- coding: utf-8 -*-
# @Time    : 2020/01/24 10:43
# @Author  : xianming yu
# @File    : 2面相对象基础语法.py

"""
面向对象基础语法
目标
    dir 内置函数
    定义简单的类(只包含方法)
    方法中的self参数
    初始化方法
    内置方法和属性
"""
"""
i1.dir内置函数(知道)
    在Python中对象几乎是无所不在的,我们之前学习的变量,数据,函数都是对象
    在python中可以使用以下两个方法验证:
        1.在标识符/数据后输入一个.然后按下TAB键,ipython会提示该对象能够调用的方法列表
        2.使用内置函数dir传入标识符/数据,可以查看对象内的所有属性及方法
        提示:__方法名__,格式的方法是python提供的内置方法/属性,稍后会给大家介绍一些常用的内置方法/属性
        序号              方法名             类型              作用
        01              __new__             方法              创建对象时会被自动调用
        02              __init__            方法              对象初始化时,会被自动调用
        03              __del__             方法              对象被从内存中销毁前,会被自动调用
        04              __str__             方法              返回对象的描述信息,print函数输出使用 
        def test():
            (前面三个引号)你好这是一个测试案例(后面三个引号)
            print("你好,python")
        print(dir(test)) # 可以查看对象内的所有属性及方法
        print(test.__doc__) #查看test函数下的文档备注    
    提示:利用好dir()函数,在学习时很多内容就不需要死记硬背
i2.定义简单的类(只包含方法)
    注释:面向对象是更大的封装,在一个类中封装多个方法,这样通过这个类创建出来的对象,就可以直接调用这些方法了!
    i2.1 定义只包含方法的类
        i2.1.1 在python中要定义一个只包含方法的类,语法格式如下:
            class 类名():
                def 方法1(self,参数列表):
                    pass
                def 方法2(self,参数列表):
                    pass
        i2.1.2 方法的定义格式和之前学习的函数几乎一样,区别在于第一个参数必须是self,大家暂时记住,稍后记住self
                注意点:类名的命名规则,要符合大驼峰命名法
    i2.2 创建对象
        i2.2.1 当一个类定义完成之后,要使用这个类来创建对象,语法格式如下:
            对象变量=类名()
    i2.3 第一个面向对象程序
        需求如下:
            小猫爱吃鱼,小猫爱喝水
        分析
            1.定义一个猫类Cat
            2.定义两个方法eat和drink
            3.按需求---不需要定义属性
        代码如下:
            class Cat:
                def eat(self):
                    print("小猫爱吃鱼")
                def drink(self):
                    print("小猫爱喝水")
            #创建猫对象
            tom=Cat()
            #对象调用类中两个的方法
            tom.eat()
            tom.drink()
    i2.4 "引用"概念的强调
        注释:在面向对象开发当中,"引用"的概念是同样适用的!
        i2.4.1 在python中使用类创建对象后,tom变量中仍然记录的是对象在内存中的地址,也就是tom变量引用了"新建的猫对象"
        i2.4.2 使用print输出对象变量,默认情况下,是能够输出这个变量引用的对象是由哪一个类创建的对象,以及在内存中的地址(输入的地址为十六进制表示)
               tom=Cat()  #注释:等号(=)右侧的Cat()负责创建对象,等号(=)左侧tom变量负责对创建的对象进行引用
               print(tom)
               输入结果:
                    <__main__.Cat object at 0x0000020A620CDEB8>
               提示:在计算机中,通常使用十六进制表示内存地址
                十进制和十六进制都是用来表达数字的,只是表示的方式不一样
                十进制和十六进制的数字之间可以来回转换 
        i2.4.3 %d可以以10进制输出数字,%x可以以16进制输出数字
            tom=Cat()   
            addr=id(tom)
            print("%d"%addr)
            输出结果:
                2243617939128
            print("%x"%addr)
            输出结果:
                20a620cdeb8
    i2.5 案例进阶--使用Cat类在创建一个对象
        lazy_cat=Cat()
        lazy_cat.eat()
            输出结果:
                小猫爱吃鱼
        lazy_cat.drink()
            输出结果:
                小猫爱喝水
        **提问:tom和lazy_cat是同一个对象吗?我们可以用print函数直接打印一下tom和lazy_cat这两个对象,看一下内存地址
        是否一样,如下:
            print(tom)
                输出结果:
                    <__main__.Cat object at 0x0000023844C39390>
            print(lazy_cat)
                输出结果:
                    <__main__.Cat object at 0x0000023844C39470>
                得到结果:很明显tom和lazy_cat不是同一个对象
i3 方法中的self参数
    i3.1 案例改造--在类外部给对象增加属性
        i3.1.1 在python中要给对象设置属性,非常容易,但是不推荐使用
            因为对象属性的封装应该封装在类的内部
        i3.1.2 "只需要在类的外部代码中"直接通过,设置一个属性即可
            注意:这种方式虽然简单,但是不推荐使用
                tom=Cat()
                tom.name="Tom"
                print(tom.name)
                输出结果:
                    Tom
    i3.2 使用self在方法的内部输出每一只猫的名字
        解释:由哪一个对象调用的方法,方法内的self就是由哪一个对象引用
        i3.2.1 在类封装方法的内部,self就表示"当前调用方法的对象自己"
        i3.2.2 调用方法时,程序员不需要传递self参数
        i3.2.3 在方法内部
            可以通过self.访问对象的属性
            也可以通过self.调用其他对象的方法
        i3.2.4 改造代码如下:
            class Cat:
                def eat(self):
                    #哪一个对象调用的方法,self就是哪一个对象的引用
                    print("%s爱吃鱼"%self.name)
                def drink(self):
                    print("%s爱喝水"%self.name)           
            tom=Cat()
            print(tom)
            tom.name="Tom"
            tom.eat()
            tom.drink()
            输出结果:
                <__main__.Cat object at 0x0000024270329390>
                Tom爱吃鱼
                Tom爱喝水
                        
            lazy_cat=Cat()
            print(lazy_cat)
            lazy_cat.name="大懒猫"
            lazy_cat.eat()
            lazy_cat.drink()
            输出结果:
                <__main__.Cat object at 0x00000242703DDF28>
                大懒猫爱吃鱼
                大懒猫爱喝水
        i3.2.5 在类的外部,通过变量名.访问对象的属性和方法
        i3.2.6 在类封装的方法中,通过self.访问对象的属性和方法
i4 初始化方法
    i4.1 之前的代码存在的问题--在类的外部给对象增加属性
        i4.1.1 将案例代码进行调整,先调用方法,再设置属性,观察一下执行效果
            tom=Cat()
            tom.eat() #先调用方法
            tom.drink() #先调用方法
            tom.name="Tom" #再设置属性
            print(tom)
            **程序执行报错如下:
            AttributeError: 'Cat' object has no attribute 'name'
        提示:
            提示1:在日常开发中,不推荐在类的外部给对象增加属性,如果程序在运行时没有找到属性,程序则会报错
            提示2:对象应该包含有那些属性,应该封装在类的内部
    i4.2 初始化方法
        i4.2.1 当使用"类名()"创建对象时,会自动执行以下操作
            i4.2.1.1 为对象在内存中"分配空间"--创建对象
            i4.2.1.2 为对象的属性"设置初始值"--初始化方法(init)
        i4.2.2 这个初始化方法就是__init__方法,__init__是对象的内置方法
            i4.2.2.1 __init__方法是专门用来定义一个类"具有哪些属性的方法"!
            i4.2.2.2 在Cat类中增加__init__方法,验证该方法在创建对象时会被自动调用
                class Cat:
                    def __init__(self):
                        print("初始化方法")
                #创建tom对象
                tom=Cat()
                输出结果:
                    初始化方法  
    i4.3 在初始化方法内部定义属性
        i4.3.1 在__init__方法内部使用 self.属性名=属性的初始值 就可以定义属性
        i4.3.2 定义属性之后,再使用Cat类创建对象,都会拥有该属性
        代码示例如下:
            class Cat():
                def __init__(self):
                    print("这是一个初始化方法")
                    #定义使用Cat类创建的猫对象都有一个name的属性
                    self.name = "Tom"
                def eat(self):
                    print("%s猫爱吃鱼"%self.name)
            #使用类名()创建对象的时候,会自动调用初始化方法__init__
            tom=Cat()
            tom.eat()
            输出结果:
                这是一个初始化方法
                Tom猫爱吃鱼
    i4.4 改造初始化方法--初始化的同时设置初始值
        i4.4.1 在开发中,如果希望在创建对象的同时,就设置对象的属性,可以对__init__方法进行改造
            i4.4.1.1 把希望设置的属性值,定义成__init__方法的参数
            i4.4.1.2 在方法内部使用self.属性=形参接受外部传递的参数
            i4.4.1.3 在创建对象时,使用 类名(属性1,属性2....)进行调用
            代码示例:
                  class Cat():
                        def __init__(self,name):
                            print("这是一个初始化方法")
                            #定义使用Cat类创建的猫对象都有一个name的属性
                            self.name = name
                        def eat(self):
                            print("%s猫爱吃鱼"%self.name)
                  #使用类名()创建对象的时候,会自动调用初始化方法__init__
                  tom=Cat("懒猫")
                  tom.eat()
                  输出结果:
                    这是一个初始化方法
                    懒猫爱吃鱼
i5 内置方法和属性
    序号      方法名         类型          作用
     1      __del__        方法          对象被从内存中销毁前,会被自动调用
     2      __str__        方法          返回对象的描述信息,print输出使用
     i5.1 __del__方法(知道)
        i5.1.1 在Python中
            当使用"类名()"创建对象时,为对象分配完空间后,自动调用__init__方法
            当一个对象被从内存中销毁前,会自动调用__del__方法
        i5.1.2 应用场景
            __init__改造初始化方法,可以让创建对象更加灵活
            __del__如果希望在对象被销毁前,再做一些事情,可以考虑一下__del__方法
        i5.1.3 生命周期
            一个对象从调用"类名()"创建的生命周期开始
            一个对象的__del__方法一旦被调用,生命周期结束
            在对象的生命周期内,可以访问对象属性,或者让对象调用方法
            代码示例:
                class Cat:
                    def __init__(self,newname):
                        self.name=newname
                        print("%s来了"%self.name)
                    def __del__(self):
                        print("%s去了"%self.name)
                tom=Cat("Tom")
                print(tom.name)
                print("*"*20)
                输出结果:
                    Tom来了
                    Tom
                    ********************
                    Tom去了
                输出结果解释:为什么"Tom去了"会打印在*号后面,那是因为Tom这个变量,在当前模块中是一个
                           全局变量,当代码执行完成之后,系统才会把Tom这个变量进行回收,所以最后才会
                           执行方法__del__然后输出"Tom去了",如果你想让"Tom去了"在*号上面打印输
                           出,可以用del 删除 tom这个全局变量,如下所示
                            tom=Cat("Tom")
                            print(tom.name)
                            del tom #用del 删除 tom这个全局变量
                            print("*"*20)
     i5.2 __str__方法
        i5.2.1 在python中使用print输出对象变量,默认情况下,会输出这个变量引用的对象,是由
               哪一个类创建的对象,以及在内存中地址(十六进制表示)
        i5.2.2 如果在开发中,希望使用print输出对象变量时,能够打印自定义的内容,就可以利用
               __str__这个内置方法了
               注意:__str__方法必须返回(return)一个字符串(string) 
               代码示例:
                class Cat:
                    def __init__(self,newname):
                        self.name=newname
                        print("%s来了"%self.name)
                    def __del__(self):
                        print("%s去了"%self.name)
                    def __str__(self): #定义__str__方法
                        return "我是小猫[%s]"%self.name #必须返回一个字符串
                tom=Cat("Tom")
                print(tom)
                输出结果:
                    Tom来了
                    我是小猫Tom
                    Tom去了  #最后调用__del__方法删除tom变量,然后输出__del__方法下的内容              
                                     
                           
                           
"""
class Cat:
    def __init__(self,newname):
        self.name=newname
        print("%s来了"%self.name)
    def __del__(self):
        print("%s去了"%self.name)
    def __str__(self):
        return "我是小猫[%s]"%self.name
tom=Cat("Tom")
print(tom)


