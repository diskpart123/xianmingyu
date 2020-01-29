# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 11:33
@file: test6.py
"""
# a=[]
# for i in range(1,10):
#     if i==1:
#         pass
#     elif i==2:
#         a.append(i)
#     else:
#         for j in range(1,10):
#             if i%j==0 and  i%i==0 and i%2==0
#
#         if i%1==0 and i%i==0 and i%2==0:
#             pass
#         else:
#             a.append(i)
# print(a)
# from pygorithm.sorting import quick_sort
# a=[100,23,98,200,31,45,135]
# result=quick_sort.sort(a)
# for i in range(len(result)):
#     print(i,result[i])

"""
dog_level={
    "京巴":20,
    "哈奇士":40,
    "藏獒":60,
    "平头哥":80
}

def dog_obj(name,type):
    d={
        "name":name,
        "type":type,
        "life_val":100
    }
    return d
def person(name,age,sex):
    d={
        "name":name,
        "age":age,
        "sex":sex
    }
    if age>18:
        d["access_level"]=50
    else:
        d["access_level"]=30
    return d
def dog_gongji(dog1,p1):
    print("疯狗[%s]咬了[%s],掉了[%s]"%(dog1["name"],p1["name"],dog_level[dog1["type"]]))
    #print("疯狗[%s]咬了[%s],掉血[%s]..." %(dog_obj["name"], person_obj['name'], dog_attack_level[dog_obj["type"]]) )
def person_gongji(p1,dog1):
    print("[%s]打了疯狗[%s],掉了[%s]"%(p1["name"],dog1["name"],p1["access_level"]))
"""
class Dog:
    d_type="jingba"
    def say_hi(self):
        print("This is",self.d_type)
d1=Dog()
d2=Dog()
print(id(d1.d_type))
print(id(d2.d_type))








