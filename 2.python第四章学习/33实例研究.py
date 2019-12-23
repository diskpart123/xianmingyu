"""
实例研究
"""

"""
4-1 程序清单
设想你要开发一个帮助一年级学生练习加法的程序.这个程序会随机产生两个一位整数:number1和number2
然后显示给学生一个问题:what is 1+7(1+7=?),在学生输入答案后,程序会显示一条消息表明答案是对还是错.
提示:
    你可以使用函数random模块中的randint(a,b)函数产生一个随机数字.这个函数返回一个在a和b之间包括a和b的随机
    整数i
random.randint(0,9) #返回的数字包含0和9
random.randrange(0,9)#返回的数字包含0但不包括9

#第一种:正常写法
import random

count = 0
temp = True
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
print("what is " + str(number1) + "+" + str(number2) + \
      "(" + str(number1) + "+" + str(number2) + "=?" + ")")
answer = input(str(number1) + "+" + str(number2) + "=请输入答案:")
answer = eval(answer)
print(answer)
if answer == (number1 + number2):
    print("您输入的答案是正确的")
else:
    print("答案错误")
    

#第二种:加入限制次数的写法,如果答案输入三次都不正确,由用户自己输入是否继续,继续填写Y,结束填写N
import random

count = 0
temp = True
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
print("what is " + str(number1) + "+" + str(number2) + \
      "(" + str(number1) + "+" + str(number2) + "=?" + ")")
while temp:
    if count == 3:
        print("你已经输入了三次答案都是错误的,是否还继续输入..是(Y),否(N)")
        input_test = input("请输入(Y/N):")
        if input_test == "Y" or input_test == "y":
            print("计算答案游戏重新开始....")
            count = 0
        elif input_test == "N" or input_test == "n":
            print("计算答案游戏,退出!")
            break
        else:
            print("只能输入大写或者小写的Y和N,请重新输入!")
            continue
    answer = input(str(number1) + "+" + str(number2) + "=请输入答案:")
    if answer.isdigit():
        answer = eval(answer)
        print(answer)
        if answer == (number1 + number2):
            print("您输入的答案是正确的")
            break
        else:
            print("答案错误")
            count += 1
            continue
    else:
        print("只能输入数字!")
"""

"""
4-2 程序清单
      提示用户输入一个整数的程序.如果那个数字是5的倍数,程序显示结果HiFive,如果这个数能被2整除,程序显示HiEven

number = eval(input("输入一个整数:"))
if number % 5 == 0:
    print("HiFive")
if number % 2 == 0:
    print("HiEven")

"""

"""
4-3 程序清单
关键点:猜生日是一个很有趣的用简单程序解决的问题
      你可以通过询问5个问题来找出你朋友的生日在一个月中的哪一天.每个问题都在询问这一天是否在5个数字集中,
      生日就是出现在这个数字的集合的第一个数字的和.例如:如果生日是19,那它就会在set1\set2\set5中出现.这
      三个数字集合的第一个数字分别是1\2\16,它们加起来的和就是19
逻辑理解:
       这个游戏非常容易编写,你可能想知道这个游戏是如何产生的.这个游戏背后的数学思想其实是非常简单的.这些数字
       不是随意地放在一起,它们分别对应二进制数1\10\100\1000\10000.1到31之间的十进制数字要用二进制数表示
       则最多需要5个数字,如下:
           十进制数字        二进制表示
              1                00001
              2                00010
              3                00011
              ...              .....
              19               10011
              ...              .....
              31               11111
       所以数字19的二进制数为10011,得到数字19是因为数字集合set1\set2\set5第一个数字相加的结果即:1+2+16=19
       它们所对应的二进制数为:1+10+10000=10011,而二进制数字10011对应的十进制的数字是19.
       如果是数字31又该如何推理呢?
       十进制数字31,二进制表示为11111,所以它出现在set1\set2\set3\set4\set5中的第一个数字相加的结果即:
       1+2+4+8+16,它们所对应的二进制数为1+10+100+1000+10000=11111.
       注意点:1-31之间的十进制数字要用二进制数表示则最多需要5个数字
day = 0
question1 = "数字集合\n" + \
            "1 3 5 7\n" + \
            "9 11 13 15\n" + \
            "17 19 21 23\n" + \
            "25 27 29 31\n" + \
            "请输入question1集合的数字:"
answer = eval(input(question1))
if answer == 1:
    day += 1

question2 = "数字集合\n" + \
            "2 3 6 7\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31\n" + \
            "请输入question2集合的数字:"
answer = eval(input(question2))
if answer == 1:
    day += 2

question3 = "4 5 6 7\n" + \
            "12 13 14 15\n" + \
            "20 21 22 23\n" + \
            "28 29 30 31\n" + \
            "请输入question3集合的数字:"
answer = eval(input(question3))
if answer == 1:
    day += 4

question4 = "8 9 10 11\n" + \
            "12 13 14 15\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31\n" + \
            "请输入question4集合的数字:"

answer = eval(input(question4))
if answer == 1:
    day += 8

question5 = "16 17 18 19\n" + \
            "20 21 22 23\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31\n" + \
            "请输入question5集合的数字:"
answer = eval(input(question5))
if answer == 1:
    day += 16

print("您的生日是:" + str(day) + "!")

"""

"""
4-4 程序清单
假设你要编写一个训练一年级学生的加法的程序.程序随机产生两个一位的整数:number1和number2,而number1>=number2,然后
向学生提问类似"9-2=?"这样的问题.在回答完问题之后,程序会显示一条信息表明答案是否正确

import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
if number1 < number2:
    number1, number2 = number2, number1
print("数字:" + str(number1) + "+" + str(number2) + "=?")
answer = eval(input("输入答案:"))
if answer == number1 + number2:
    print("答案正确!")
else:
    print("答案错误....请继续努力")
"""




"""
4-5 程序清单
编写一个程序来判断一个给定的年份属于哪一个生肖,中国十二生肖以12为循环,这个循环的每一年都分别
由一个动物表示:猴\鸡\狗\猪\鼠\牛\虎\兔\龙\蛇\马\羊:
year % 12(0:猴,1:鸡,2:狗,3:猪,4:鼠,5:牛,6:虎,7:兔,8:龙,9:蛇,10:马,11:羊) 

year = eval(input("请输入年份:"))
if year % 12 == 0:
    print("猴")
elif year % 12 == 1:
    print("鸡")
elif year % 12 == 2:
    print("狗")
elif year % 12 == 3:
    print("猪")
elif year % 12 == 4:
    print("鼠")
elif year % 12 == 5:
    print("牛")
elif year % 12 == 6:
    print("虎")
elif year % 12 == 7:
    print("兔")
elif year % 12 == 8:
    print("龙")
elif year % 12 == 9:
    print("蛇")
elif year % 12 == 10:
    print("马")
elif year % 12 == 11:
    print("羊")
"""

"""
4-6 程序清单

编写一个程序,提示用户输入以磅为单位的体重和以英寸为单位的身高
1磅=0.453千克
1英寸=0.0254米
公式:以千克为单位体重除以以米为单位的身高的平方

weight = eval(input("输入以英镑为单位的体重:"))
weight = weight * 0.45359237
print("weight:", format(weight, "4.2f"))
height = eval(input("输入以英寸为单位的身高:"))
height = height * 0.0254
print("height:", format(height, "4.2f"))
BMI = weight / (height**2)
print("BMI:", format(BMI, "4.2f"))
if BMI < 18.5:
    print("超轻")
elif BMI >= 18.5 and BMI < 25.0:
    print("标准")
elif BMI >= 25.5 and BMI < 30.0:
    print("超重")
else:
    print("痴肥")

# 输入以英镑为单位的体重:146
# 74.902066425
# 输入以英寸为单位的身高:70
# 1.76000000044
"""

"""
4-7 程序清单
计算税额
关键点:使用嵌套的if语句来编写一个计算税款的程序

    美国联邦个人收入所得税是根据报税身份和可纳税收入来计算的.
    报税身份有四种:单身报税人\已婚合并申报人\已婚分开申报人\户主.
    税率每年都会改变.

staus=eval(input("输入身份序号(0->代表单身报税人,1->代表已婚合并申报人,\
2->代表已婚分开申报人,3->代表户主):"))
income = eval(input("输入收入:"))
tax = 0
if staus == 0:
    if income <= 8350:
        tax = 8350 * 0.1
    elif income <= 33950:
        tax = 8350 * 0.1 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (
                income - 171550) * 0.33
    else:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (
                372950 - 171550) * 0.33 + (income - 372950) * 0.35

elif staus == 1:
    if income <= 16700:
        tax = 16700 * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (income - 67900) * 0.25
    elif income <= 208850:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (income - 137050) * 0.28
    elif income <= 372950:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
              (income - 208850) * 0.33
    else:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
              (372950 - 208850) * 0.33 + (income - 372950) * 0.35
elif staus == 2:
    if income <= 8350:
        tax = 8350 * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15
    elif income <= 68525:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income <= 104425:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (income - 68525) * 0.28
    elif income <= 186475:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
              (income - 104425) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
              (186475 - 104425) * 0.33 + (income - 186475) * 0.35
elif staus == 3:
    if income <= 11950:
        tax = 11950 * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15
    elif income <= 117450:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (income - 45500) * 0.25
    elif income <= 190200:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (income - 117450) * 0.28
    elif income <= 372950:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
              (income - 190200) * 0.33
    else:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + \
              (372950 - 190200) * 0.33 + (income - 372950) * 0.35
print(tax)

"""

"""
4-11 程序清单 

关键点:在一个游戏编程中,检测一个对象是否在另一个对象中是一个常见的任务
    在游戏编程中,你经常要决定一个对象是否在另一个对象中.这个实例给出测
    试某个点是否在一个圆的程序中.这个程序提示用户输入一个圆心,半径,和一
    个点.然后程序显示这个圆和点一级一条表明这个点实在圆内还是圆外的消息

import math
import turtle

x1, y1 = eval(input("输入x1和y1的坐标:"))
radius = eval(input("输入半径:"))

turtle.showturtle()
# turtle.begin_fill()
# turtle.color("black")
# turtle.circle(5)
# turtle.end_fill()
turtle.dot(10, "black")  # 这个方法画了一个直径为10的黑点,简化了上面注释的画圆的代码,一行就可以处理画圆的操作
turtle.penup()
turtle.goto(x1, y1 - radius)
turtle.pendown()
turtle.circle(radius)
x2, y2 = eval(input("输入x2和y2的坐标:"))
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
# turtle.begin_fill()
# turtle.color("black")
# turtle.circle(5)
# turtle.end_fill()
turtle.dot(10, "black")
turtle.goto(x1, y1)
turtle.hideturtle()
turtle.done()
d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
if d == radius:
    print("圆上")
elif d < radius:
    print("圆内")
else:
    print("圆外")
"""
