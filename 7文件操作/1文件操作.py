# -*- coding: utf-8 -*-
# @Time    : 2020/02/22 9:04
# @Author  : xianming yu
# @File    : 1文件操作.py

"""
学习文件操作
"""
"""
读取模式:
    'r' 读取（默认）
    'w' 写入，并先截断文件(会将原来的文件内容覆盖掉)
    'x' 排它性创建，如果文件已存在则失败
    'a' 写入，如果文件存在则在末尾追加
    'b' 二进制模式
    't' 文本模式（默认）
    '+' 更新磁盘文件（读取并写入）
        r+， 读写【可读，可写】
        w+，写读【可读，可写】
        x+ ，写读【可读，可写】
        a+， 写读【可读，可写】
"""

"""
案例:
    将1.txt文件中的第7行到第10行中的内容保存在2.txt中
    7,8,9,10
    As rain upon my tongue
    就如舌尖上的雨露
    I teased at life as if it were a foolish game
    我戏弄生命 视其为愚蠢的游戏
"""

files="E:\\xianmingyu\\7文件操作\\1.txt"
with open(files,"r",encoding="utf-8") as f1:
    result=f1.readlines()
    count=0
    for i in result:
        count+=1
        if count>=7 and count<=10:
            with open("2.txt","a",encoding="utf-8") as f2:
                f2.write(i)
with open("2.txt","r",encoding="utf-8") as f:
    rest=f.read()
    print(rest)











    





