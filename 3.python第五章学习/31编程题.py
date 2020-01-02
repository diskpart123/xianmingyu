# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2019/12/30 10:53
@file: 31编程题.py
"""
"""
5.10(找出最高分):编写程序提示用户输入学生个数以及每个学生的分数,然后显示最高分,假设输入是存储在一个名为score.txt文件
,程序从这个文件获取输入;
解题思路:首先需要准备一个score.txt文本文件,然后在里面填写学生的个数,学生的分数,学生的个数填写在第一行,分数从第二行
开始,填写完毕后保存文本文件,然后用python输入输出重定向在CMD控制台输入,求出最大分数

num=eval(input(""))
print("学生个数:",num)
max_data=eval(input("输入数据:"))
print(max_data)
for i in range(num-1):
    data = eval(input("请输入数字:"))
    if data>max_data:
        max_data=data
    print(data)
print("max_data:",max_data)
"""
"""
5.11 (找出两个最高分) 编写程序提示用户输入学生个数以及每个学生的分数,然后显示最高分和次高分的分数,此题是5.10的升级版

num = eval(input(""))
print("学生个数:", num)
max_data = eval(input("max_data:"))
nex_max_data = eval(input("nex_max_data:"))
if max_data < nex_max_data:
    max_data, nex_max_data = nex_max_data, max_data
else:
    pass
for i in range(num - 1):
    data = eval(input("请输入数字:"))
    if data > max_data:
        nex_max_data = max_data
        max_data = data
    elif data < max_data: 
        if data < nex_max_data:
            pass
        elif data > nex_max_data:
            nex_max_data = data
    else:
        pass
    print(data)
print("max_data:", max_data)
print("nex_max_data:", nex_max_data)
"""

"""
count = 1
for i in range(100, 1000 + 1):
    if i % 5 == 0 and i % 6 == 0:
        print(i, end="  ")
        if count % 10 == 0: #按照10个数字每行显示
            print("")
        count += 1
"""

"""
5.50(Turtle:显示三角形图案的数字)编写程序显示三角形图案数字
for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
"""

"""
5.51(Turtle:显示一个格子) 编写程序显示18x18的格子

import turtle

step = 540
turtle.showturtle()
count = 0
for y in range(19):
    turtle.forward(step)
    turtle.penup()
    count += 20
    turtle.goto(0, count)
    turtle.pendown()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.left(90)
count = 0
step = 360
for x in range(19):
    turtle.forward(step)
    turtle.penup()
    count += 30
    turtle.goto(count, 0)
    turtle.pendown()
turtle.done()
"""
"""
绘制国际象棋棋盘

import turtle

step = 20
for x in range(8):
    for y in range(8):
        turtle.penup()
        turtle.goto(x * step, y * step)
        turtle.pendown()
        if (x + y) % 2 == 0:
            turtle.begin_fill()
            for j in range(4):
                turtle.forward(20)
                turtle.right(90)
            turtle.color("black")
            turtle.end_fill()
        else:
            for k in range(4):
                turtle.forward(20)
                turtle.right(90)
turtle.done()
"""