# if 嵌套
"""
例如:一个男孩找女朋友,name(姓名)age(年龄)tall(身高)star(星座)pos(坐标)
name:无需求
age:40以上
tall:170以上
star:天蝎座
pos:坐标(北京)
"""

name = input("输入姓名:")
age = eval(input("输入年龄:"))
tall = eval(input("输入身高:"))
start = input("输入星座:")
pos = input("输入坐标:")
if pos != "北京":
    print("地址不符合")
else:
    if age <= 40:
        print("年龄不符合")
    else:
        if tall < 170:
            print("身高不符合")
        else:
            if start != "天蝎座":
                print("星座不符合")
            else:
                print("符合要求!", name)
