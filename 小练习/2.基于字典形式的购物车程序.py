# -*- coding: utf-8 -*-
# @Time    : 2020/01/14 9:50
# @Author  : xianming yu
# @File    : 2.基于字典形式的购物车程序.py

# 编写一个购物车程序
#会员信息
import sys
from collections import Counter #用于合并两个字典中同一个key的value
database_crm={1234:100,234234:90} #会员卡列表
def Commodity(**sku): #定义商品列表
    return sku
crm_input=eval(input("请输入会员卡号:"))

for key in database_crm.keys(): #遍历会员卡号
    if key==crm_input: #匹配会员卡号
        print("会员卡号:"+str(key),"余额:"+str(database_crm[crm_input])) #打印会员卡号与余额
        break
    else:
        pass
else:
    print("你输的会员卡号:{}不存在".format(crm_input))
    sys.exit() # 如果会员卡号不存在,则停止程序往下运行
a=Commodity(可乐=5,雪碧=3) #商品列表
center="打印商品列表"
print(center.center(20,"*"))
print(a)
add_shoping={} # 空购物车
add_shoping1={} #空购物车,用于合并add_shoping购物车一样的key的value
cd=True
while cd:
    shoping_sku=input("请输入购买的商品名称:") #选择商品
    if shoping_sku not in a.keys():
        if shoping_sku=="exit":
            cd=False
        else:
            print("输入的{}不存在,请重新输入!".format(shoping_sku))
            continue
    elif shoping_sku in a.keys():
        if int(a[shoping_sku])<int(database_crm[crm_input]):
            if shoping_sku in add_shoping.keys(): #如果商品已经在购物车中存在那么就把value值相加
                add_shoping1[shoping_sku]=a[shoping_sku]
                add_shoping,add_shoping1=Counter(add_shoping),Counter(add_shoping1)
                add_shoping=dict(add_shoping+add_shoping1)
                add_shoping1.clear()
                database_crm[crm_input]=database_crm[crm_input]-a[shoping_sku]
            elif shoping_sku not in add_shoping.keys():
                add_shoping[shoping_sku]=a[shoping_sku] #加入购物车
                database_crm[crm_input]=database_crm[crm_input]-a[shoping_sku]
                for key,values in add_shoping.items():
                    print("商品:{},已添加购物车".format(key))
        else:
            print("会员卡余额不足....")
            break

end="购买商品清单"
print(end.center(20,"*"))
for key,value in add_shoping.items():
    print(key, value)
print("会员卡号:"+str(crm_input),"余额:"+ \
      str(database_crm[crm_input])) #打印会员卡号与余额
#购物车基本程序已经完成,下一步完成已购买的商品删除后,余额返回