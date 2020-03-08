# -*- coding: utf-8 -*-
# @Time    : 2020/02/14 11:34
# @Author  : xianming yu
# @File    : 18案例代码演练_测试掌握情况.py

"""
人狗大战，用面向对象如何实现？
需求:
    1.人狗大战，生成多条狗，多个人
    2.狗能咬人，人能打狗
    3.咬了或被打了都掉血



class Dog(object):

    def __init__(self, variety, name, dog_atk):
        # 狗的品种
        self.variety = variety
        # 狗的名字
        self.name = name
        # 狗的攻击力
        self.dog_atk = dog_atk
        # 狗的生命值
        self.dog_health = 100

    # 定义狗咬人的方法
    def bite(self, person):
        person.person_health -= self.dog_atk
        print("狗[%s]咬了[%s],人掉血[%d],人还剩血量[%d]" %
              (self.name, person.name, self.dog_atk, person.person_health))

class Person(object):

    def __init__(self,name,person_atk):
        # 人的名字
        self.name = name
        # 人的攻击力
        self.person_atk = person_atk
        #人的生命值
        self.person_health = 100
    #定义人攻击狗的方法
    def attack(self,dog):
        dog.dog_health-=self.person_atk
        print("[%s]打了[%s],狗掉血[%d],狗还剩余血量[%d]"
              %(self.name,dog.name,self.person_atk,dog.dog_health))
#1.实例化狗
jingba=Dog("狼犬","犬诚卫士",30)
#2.实例化人
xiaoming=Person("小明",40)
#3.狗咬人
jingba.bite(xiaoming)
#4.人攻击狗
xiaoming.attack(jingba)

"""

"""
需求
    1.创建房子类
    2.创建家具类
    3.向房子中添加家具


class Furniture(object):
    def __init__(self,name,area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area

bed=Furniture("席梦思",20)
cabinet=Furniture("橱柜",15)
tea=Furniture("茶几",10)



class House(object):
    def __init__(self, house_type):
        # 房子的户型
        self.house_type = house_type
        # 房子面积
        self.area = 100
        # 房子剩余面积
        self.residual_area = self.area
        self.furniture_list = []

    # 定义一个往房子中添加家具的方法
    def add(self, furniture):
        if furniture.area > self.residual_area:
            print("[%s]占地面积超过了房子的面积,不能添加..."%furniture.name)
        self.furniture_list.append(furniture.name)
        self.furniture_list.append(furniture.area)
        self.residual_area-=furniture.area
    def __str__(self):
        return ("户型:[%s]\n房子面积:[%d],房子剩余面积:[%d]\n家具:%s"
              %(self.house_type,self.area,self.residual_area,self.furniture_list))

house=House("两室一厅")

house.add(bed)
house.add(cabinet)
house.add(tea)
print(house)
"""

"""
# 定义会员类
class MemBer:
    def __init__(self, card_type, card_number, card_balance):
        # 卡类型
        self.card_type = card_type
        # 卡号
        self.card_number = card_number
        # 卡余额
        self.card_balance = card_balance

    def __str__(self):
        return ("卡类型:%s\n卡号:%d\n卡余额:%d"
                % (self.card_type, self.card_number, self.card_balance))

huiyuan = MemBer("普通会员卡", 123456, 100)



# 商品类
class Commodity:
    def __init__(self, name, spec, price):
        # 商品名称
        self.name = name
        # 商品规格
        self.spec = spec
        # 商品单价
        self.price = price


commodity=Commodity("可乐",1,4)
commodity1=Commodity("牛奶",1,8)
commodity2=Commodity("整箱牛奶",1,90)
# print(commodity.name,commodity.spec,commodity.price)



# 定义购物车类
class Shopping_cart:
    def __init__(self):
        self.shopping_cart=[]

    #商品添加购物车方法
    def add(self,commodity,member):
        if commodity.price>member.card_balance:
            print("卡余额为[%d],不能添加商品[%s]单价为[%d]..."%(member.card_balance,commodity.name,commodity.price))
            return
        self.shopping_cart.append(commodity.name)
        self.shopping_cart.append(commodity.price)
        member.card_balance-=commodity.price

    def __str__(self):
        return ("购物车:%s"%(self.shopping_cart))

#调用:创建对象
gouwuche1=Shopping_cart()
gouwuche1.add(commodity,huiyuan)
gouwuche1.add(commodity1,huiyuan)
gouwuche1.add(commodity2,huiyuan)
print(gouwuche1)
print("-------------------------")
print(huiyuan)
"""
"""
#学生信息表,还没有完成

class Student_Information(object):
    # 定义静态方法用来显示学生信息表
    @staticmethod
    def help_information():
        a="学生信息表"
        print(a.center(20,"*"))
    def __init__(self,name,language,mathematics,english):
        # 学生姓名
        self.name = name
        # 语文成绩
        self.language = language
        # 数学成绩
        self.mathematics =mathematics
        # 英语成绩
        self.english = english
        # 总分成绩 语文+数学+英语
        self.total_points=int(self.language)+int(self.mathematics)+int(self.english)
        # 存放学生信息
        self.student_list={}
    # 新建学生信息
    def new_add(self):
        self.student_list["name"]=self.name
        self.student_list["language"]=self.language
        self.student_list["mathematics"]=self.mathematics
        self.student_list["english"]=self.english
        self.student_list["total_points"]=self.total_points

    def __str__(self):
        return ("%s"%self.student_list)

test1=Student_Information("喻先明","90","50","70")
test2=Student_Information("喻先明","90","50","70")
test1.new_add()
test2.new_add()

print(test1)
print(test2)
"""

"""
校园管理系统
"""
