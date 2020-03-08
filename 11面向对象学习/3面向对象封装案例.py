# -*- coding: utf-8 -*-
# @Time    : 2020/02/02 14:05
# @Author  : xianming yu
# @File    : 3面向对象封装案例.py
"""
面向对象封装案例
目标
    封装
    小明爱跑步
    存放家具
    士兵射击
"""
"""
i1 封装
    i1.1 "封装"是面向对象编程的一大特点
    i1.2 面向对象编程的第一步--将属性和方法封装到一个抽象的类中
    i1.3 外界使用"类"创建"对象",然后让"对象"调用"方法"
    i1.4 对象方法的细节都被封装在类的内部
i2 面向对象封装实例1
    i2.1 案例1:小明爱跑步
        需求:
            1.小明体重75.0公斤
            2.小明每次跑步会减肥0.5公斤
            3.小明每次吃东西体重增加1公斤
        设计:
            1.小明是一个人类,所以需要定义一个Person类(名词提炼法)
            2.需要定义两个属性分别是:name(小明),weight(体重)
            3.需要定义两个方法跑步(run())和吃东西(cat())(动词提炼法)
        提示:
            在"对象的方法内部",是可以"直接访问对象的属性的" 
        代码实现:
            class Person:
                def __init__(self,name,weight):
                    self.name=name
                    self.weight=weight
                def __str__(self):
                    return "我的名字叫[%s],体重是[%.1f]kg"%(self.name,self.weight)
                def run(self):
                    self.weight-=0.5
                    print("%s跑步后体重是%.1fkg"%(self.name,self.weight))
                def eat(self):
                    self.weight+=1
                    print("%s吃东西后体重是%.0fkg"%(self.name,self.weight))   
        调用:
            person=Person("小明",75.0)
            print(person)
            person.run()
            person.eat()
        输出结果:
            小明的体重是75.0kg
            小明跑步后体重是74.5kg
            小明吃东西后体重是76kg
    i2.2 案例2:小明爱跑步扩展--增加小美也爱跑步
        需求:
            1.小明和小美都爱跑步
            2.小明体重75.0公斤
            3.小美体重45.0公斤
            4.每次跑步都会减少0.5公斤
            5.每次吃东西都会增加1公斤
        设计:
            1.小明和小美都是人类,所以需要定义一个Person类(名词提炼法)
            2.需要定义两个属性分别是:name(小明,小美),weight(体重)
            3.需要定义两个方法跑步(run())和吃东西(cat())(动词提炼法)
        提示:
            1.在对象方法的内部,是"直接可以访问对象属性的"
            2.同一个类创建的多个对象之间,"属性"互不干扰
        代码实现:
            class Person:
                def __init__(self,name,weight):
                    self.name=name
                    self.weight=weight
                def __str__(self):
                    return "我的名字叫[%s]的体重是[%.1f]kg"%(self.name,self.weight)
                def run(self):
                    self.weight-=0.5
                    print("%s跑步后体重是%.1fkg"%(self.name,self.weight))
                def eat(self):
                    self.weight+=1
                    print("%s吃东西后体重是%.0fkg"%(self.name,self.weight))
            调用小明:
                person1=Person("小明",75.0)
                print(person1)
                person1.run()
                person1.eat()
            输出结果:
                我的名字叫[小明]的体重是[75.0]kg
                小明跑步后体重是74.5kg
                小明吃东西后体重是76kg             
                
            调用小美:
                person2=Person("小美",45.0)
                print(person2)
                person2.run()
                person2.eat()
            输出结果:
                我的名字叫[小美]的体重是[45.0]kg
                小美跑步后体重是44.5kg
                小美吃东西后体重是46kg
i3 面向对象封装实例2
    摆放家具
        i3.1 需求 
            1.房子(House)有户型,总面积和家具名称列表
                注意:新房子没有任何家具
            2.家具(Houseltem)"有名字"和"占地面积",其中
                席梦思(bed)占地4平米
                衣柜(chest)占地2平米
                餐桌(table)占地1.5平米
            3.将以上三件家具添加到房子中
            4.打印房子时,要求输出:户型,总面积,剩余面积,家具列表
        i3.2 设计
            房子类设计:
                属性
                    house_type #户型
                    area #总面积
                    free_area #剩余面积
                    item_list #家具名称列表
                方法实现
                    __init__(self,house_type,area):
                    __str__(self):
                    add_item(self,item): #添加家具方法
            家具类设计:
                属性
                    name #家具名字
                    area #家具占地面积
                方法实现
                    __init__(self,name,area):
                    __str__(self):
        i3.3 注意点
            剩余面积
                1.在创建房子对象时,定义一个剩余面积的属性,初始值和总面积相等
                2.在调用add_item方法,向房子添加家具时,让剩余面积=剩余面积-家具面积
            思考题
                我们开发时是先开发房子类还是家具类?
                答案是:家具类
                原因:
                    1.家具类简单
                    2.房子类中要使用到家具,所以家具类是要被使用的类,通常应该先开发
        i3.4 代码初步实现
            #家具类
            class Houseltem:
                def __init__(self,name,area):
                    self.name = name
                    self.area = area
                def __str__(self):
                    return "[%s]占地[%.2f]平米"%(self.name,self.area)
            bed=Houseltem("席梦思",4)
            chest=Houseltem("衣柜",2)
            table=Houseltem("餐桌",1.5)
            
            #房子类
            class House:
                def __init__(self,house_type,area):
                    self.house_type = house_type
                    self.area = area
                    self.free_area = area
                    self.item_list=[]
                def __str__(self):
                    return ("户型:%s\n总面积:%.2f平方,剩余[%.2f]平方\n家具:%s"
                            %(self.house_type,self.area,self.free_area,self.item_list))
                def add_item(self,item):
                    print("要添加的%s"%item)
            my_house=House("两室一厅",80)
            my_house.add_item(bed)
            my_house.add_item(chest)
            my_house.add_item(table)
            print(my_house)
            输出结果:
                要添加的[席梦思]占地[4.00]平米
                要添加的[衣柜]占地[2.00]平米
                要添加的[餐桌]占地[1.50]平米
                户型:两室一厅
                总面积:80.00平方,剩余[80.00]平方
                家具:[]
            小结:
                1.创建一个房子类,使用到__init__和__str__两个内置方法
                2.准备一个add_item方法,用于添加家具
                3.使用房子类创建了一个房子对象my_house
                4.让房子对象my_house调用了三次add_item方法,将三件家具以实参传递到add_item方法内部
        i3.5 上面的i3.4代码中并没有实现真正的添加家具,所以在这一步我们需要实现"添加家具"的功能
            需求
                1.判断家具的面积是否超过剩余面积,如果超过,提示不能添加这件家具
                2.将家具的名称追加到"家具名称列表当中"
                3.用房子的剩余面积-家具面积    
            代码实现
                家具类
                    class Houseltem:
                        def __init__(self,name,area):
                            self.name = name
                            self.area = area
                        def __str__(self):
                            return "[%s]占地[%.2f]平米"%(self.name,self.area)
                    调用:创建对象
                        bed=Houseltem("席梦思",4)
                        chest=Houseltem("衣柜",2)
                        table=Houseltem("餐桌",1.5)
                房子类
                    class House:
                        def __init__(self,house_type,area):
                            self.house_type = house_type
                            self.area = area
                            self.free_area = area
                            self.item_list=[]
                        def __str__(self):
                            return ("户型:%s\n总面积:%.2f平方,剩余[%.2f]平方\n家具:%s"
                                    %(self.house_type,self.area,self.free_area,self.item_list))
                        def add_item(self,item):
                            if item.area>self.area:
                                print("[%s]面积太大,无法添加"%item.name)
                                return "xxx"
                            self.item_list.append(item.name)
                            self.free_area=self.free_area-item.area #计算剩余面积
                    调用:创建对象
                        my_house=House("两室一厅",80)
                        my_house.add_item(bed) 
                        my_house.add_item(chest)
                        my_house.add_item(table)
                        print(my_house)
                    输出结果:
                        户型:两室一厅
                        总面积:80.00平方,剩余[72.50]平方
                        家具:['席梦思', '衣柜', '餐桌']
i4 面向对象封装实例3
    士兵射击
        i4.1 需求
            1.士兵许三多有一把AK47
            2.士兵可以开火
            3.枪能够发射子弹
            4.枪装填子弹 —— 增加子弹数量
        i4.2 设计
            枪类设计:
                属性
                    model #枪的型号
                    bullet_count #枪初始化子弹的数量,默认为0
                    
                方法需求
                    1.判断是否有子弹，没有子弹无法射击
                    2.使用print提示射击，并且输出子弹数量
                                    
                方法实现
                    __init__(self,model) 
                    add_bullet(self,count) #装填子弹方法
                    shoot(self) #射击方法
                    
                代码实现
                    class Gun:
                        def __init__(self, model):                    
                            # 枪的型号
                            self.model = model
                            # 子弹数量
                            self.bullet_count = 0                    
                        def add_bullet(self, count):                    
                            self.bullet_count += count                    
                        def shoot(self):                    
                            # 判断是否还有子弹
                            if self.bullet_count <= 0:
                                print("没有子弹了...")                    
                                return                    
                            # 发射一颗子弹
                            self.bullet_count -= 1                            
                            print("%s 发射子弹[%d]..." % (self.model, self.bullet_count))

                    调用:创建枪对象
                        ak47 = Gun("ak47")
                        ak47.add_bullet(50)
                        ak47.shoot()
                    输出结果:
                        ak47 发射子弹[49]...
            士兵类设计
                属性
                    name #士兵的名字
                    gun #士兵的枪
                    
                属性注意点
                    1.在定义属性时，如果不知道设置什么初始值,可以设置为'None'
                    2.None关键字表示什么都没有
                    3.None表示一个空对象,没有方法和属性，是一个特殊的常量
                    4.可以将None赋值给任何一个变量
                    
                方法需求
                    1.判断是否有枪，没有枪没法冲锋
                    2.喊一声口号
                    3.装填子弹
                    4.射击
                
                方法实现
                    __init__(self, name) # 士兵的名字
                    fire(self) #判断士兵是否有枪,高喊口号,让枪装填子弹, 让枪发射子弹
                
                代码实现
                    class Soldier:
                        def __init__(self, name):                    
                            # 姓名
                            self.name = name
                            # 枪，士兵初始没有枪 None 关键字表示什么都没有
                            self.gun = None                    
                        def fire(self):                    
                            # 1. 判断士兵是否有枪
                            if self.gun is None:
                                print("[%s] 还没有枪..." % self.name)                    
                                return                    
                            # 2. 高喊口号
                            print("冲啊...[%s]" % self.name)                    
                            # 3. 让枪装填子弹
                            self.gun.add_bullet(50)                    
                            # 4. 让枪发射子弹
                            self.gun.shoot()
                调用:创建枪对象
                    ak47 = Gun("ak47")
                    xusanduo=Soldier("许三多")
                    xusanduo.gun=ak47
                    xusanduo.fire()
                输出结果:
                    冲啊...[许三多]
                    ak47 发射子弹[49]...  
        小结
            1. 创建了一个 士兵类，使用到 __init__ 内置方法
            2. 在定义属性时，如果 不知道设置什么初始值，可以设置为 None
            3. 在 封装的 方法内部，还可以让 自己 使用其他类创建的对象属性 调用已经 封装好的方法

i5 身份运算符
    1.身份运算符用于 比较 两个对象的 内存地址 是否一致 —— 是否是对同一个对象的引用
        在 Python 中针对 None 比较时，建议使用 is 判断
        运算符         描述                                              实例
        is           is是判断两个标识符是不是引用同一个对象                x is y,类似id(x)==id(y)
        is not       is not是判断两个标识符是不是引用不同对象              x is not y,类似id(a) != id(b)
    2.is 与==区别
        is 用于判断两个变量 引用对象是否为同一个 
        == 用于判断引用变量的值是否相等
        实例
            >>> a = [1, 2, 3]
            >>> b = [1, 2, 3]
            >>> b is a 
            False
            >>> b == a
            True                                                         
"""

class Women:
    def __init__(self,name):
        self.name=name
        self.__age=18
    def sele(self):
        print("%s的年龄是%d"%(self.name,self.__age))
xiaofang=Women("小芳")
print(xiaofang.__age)


