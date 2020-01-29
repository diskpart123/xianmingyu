
# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/5 16:29
@file: test7.py
"""
# dog_attack_level = {
#     "京巴":20,
#     "藏獒":80,
#     "平头哥":60
# }
#
# def dog(name,d_type):
#     if d_type in dog_attack_level:
#         d = {
#             "name":name,
#             "type":d_type,
#             "life_val" :100
#         }
#     else:
#         print("未知物种，不易接近")
#         return None
#     return d
# def person(name,age,sex):
#     d = {
#         "name": name,
#         "age": age,
#         "sex":sex,
#         "life_val": 100
#     }
#     if age > 18:
#         d["attack_level"] = 50
#     else:
#         d["attack_level"] = 30
#     return d
#
#
# def bite(dog_obj,person_obj):
#     person_obj["life_val"] -= dog_attack_level[dog_obj["type"]]
#     print("疯狗[%s]咬了[%s],掉血[%s]..." %(dog_obj["name"], person_obj['name'], dog_attack_level[dog_obj["type"]]) )
#
# def beat(person_obj,dog_obj):
#     dog_obj["life_val"] -= person_obj['attack_level']
#     print("[%s] 打了 疯狗[%s],狗掉血[%s]..." %(person_obj["name"], dog_obj["name"], person_obj["attack_level"]))
#
#
# dog1 = dog("majj","平头哥")
# dog2 = dog("二哈","京巴")
# p1 = person("alex",22,"male")
# bite(dog1,p1) #调用
# beat(p1,dog2)
# print(dog1,dog2)


dog_level={
    "京巴":20,
    "哈奇士":40,
    "藏獒":60,
    "平头哥":80
}
# print(dog_level)
# print(dog_level["京巴"])
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
    print("疯狗[%s]咬了[%s],人掉血[%s]"%(dog1["name"],p1["name"],dog_level[dog1["type"]]))

def person_gongji(p1,dog1):
    print("[%s]打了疯狗[%s],狗掉血[%s]"%(p1["name"],dog1["name"],p1["access_level"]))

dog1=dog_obj("majj","平头哥")
print(dog1)

p1=person("Alex", 22,"男")
print(p1)

person_gongji(p1,dog1)
