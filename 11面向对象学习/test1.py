# -*- coding: utf-8 -*-
# @Time    : 2020/01/23 17:36
# @Author  : xianming yu
# @File    : test1.py

"""
设计一个人开枪的游戏

#定义枪类
class Gun(object):
    def __init__(self,model):
        self.model = model
        self.count = 0
    def filling(self,qty):
        self.qty = qty
        self.qty+=self.count
    def shott(self):
        if self.qty<=0:
            print("%s的子弹数量为%d"%(self.model, self.qty))
        self.qty-=1
        print("%s发射子弹,剩余子弹数量为%d"%(self.model,self.qty))
class Person(object):
    def __init__(self,name):
        self.name = name
        self.gun=None
    def if_gun(self):
        if self.gun is None:
            print("士兵%s没有一把枪...不能射击..."%self.name)
        self.gun.filling(10)
        self.gun.shott()


ak47=Gun("AK47")
xusanduo=Person("许三多")
xusanduo.gun=ak47
xusanduo.if_gun()
"""
"""
1 在Dog类封装方法 game
普通狗只是简单的玩耍
2 定义XiaoTianDog子类继承自Dog类,并且重写game方法
哮天犬需要在天上玩耍
3 定义Person类,并且封装一个和狗玩的方法
在方法内部，直接让 **狗对象** 调用game方法
"""
"""
1.人狗大战，生成多条狗，多个人
2.狗能咬人，人能打狗
3.咬了或被打了都掉血

class Dog(object):
    def __init__(self,name):
        #狗的名字
        self.name = name
        #狗的经验值
        self.empirical=10
    def d_bite(self,person):
        self.empirical-=1
        print("[%s]打了[%s],[%s]剩余经验值:[%d]"%(person.name,self.name,self.name,self.empirical))
class PerSon(object):
    def __init__(self,name):
        self.name = name
        self.empirical =10
    def p_bite(self,dog):
        self.empirical-=1
        print("[%s]咬了[%s],[%s]剩余经验值:[%d]"%(dog.name,self.name,self.name,self.empirical))
jingba=Dog("京巴")
xiaoming=PerSon("小明")
jingba.d_bite(xiaoming)
xiaoming.p_bite(jingba)
"""
"""
1.创建一个家具类
2.创建一个房子类
3.向房子中添加家具

#定义家具类
class Furniture:
    def __init__(self,name,area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area
bed=Furniture("席梦思",25)
desk=Furniture("电脑桌",10)
cabinet=Furniture("橱柜",15)
xxx=Furniture("TEST",20)

class House:
    def __init__(self,model):
        #房子类型
        self.model = model
        self.area = 60
        self.residue_area = self.area
        self.furniture_list=[]
    def __str__(self):
        return ("户型:[%s]\n总面积:[%d],剩余面积[%d]\n家具列表:%s"%
                (self.model, self.area,self.residue_area,self.furniture_list))
    def add(self,furniture):
        if furniture.area>self.residue_area:
            print("[%s]的占地面积大于房子的面积...不能添加!"%furniture.name)
            return
        self.residue_area-=furniture.area
        self.furniture_list.append(furniture.name)
        self.furniture_list.append(furniture.area)

luxury=House("两室一厅")
luxury.add(bed)
luxury.add(desk)
luxury.add(cabinet)
luxury.add(xxx)
print(luxury)
"""

"""
class Animate:
    def __init__(self):
        self.name="diskpart" # 父类的公有属性
    def run(self):
        print("跑") #父类的公有方法
class Dog(Animate):
    def bark(self):
        print("二郎神,叫...")
        #self.run() #在子类中调用父类的公有方法
        print(self.name) #在子类中访问父类的公有属性
# 调用:创建对象
test=Dog() #子类创建test对象
test.bark()
"""

