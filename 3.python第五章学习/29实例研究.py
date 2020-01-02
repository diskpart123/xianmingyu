"""
第五章:实例研究
"""
"""
5-1 程序清单
回顾程序清单4-4,它给出一个提示用户输入一个数学题答案的程序.现在通过循环,你可以重写这个程序,让用户一直输入答案
直到输入正确的答案为止;

import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
if number1 < number2:
    number1, number2 = number2, number1
print(str(number1) + "-" + str(number2) + "=?")
sign_out = 1
while sign_out:
    answer = eval(input("请输入答案:"))
    if answer == number1 - number2:
        print("答案正确.." + str(number1) + "-" + str(number2) + "=" + str(number1 - number2))
        sign_out = 0
    else:
        print("答案不正确,请重新输入....")
"""
"""
5-2 程序清单
这里的问题是猜出电脑里存储的数字是什么.你将要编写一个能够随机生成一个0到100之间且包括0和100的数字的程序.这个程序提示用户连续的输入数字
直到它与那个随机生成的数字相同.对于每个用户输入的数字,程序提示它是否过高还是过低,所以用户可以更明智的选择下一个输入的数字.下面是一个简单
的运行

import random
number=random.randint(0,100)
input_up=int(input("请输入数字:"))
if input_up>number:
    print("你输入的数字过大...")
elif input_up<number:
    print("你输入的数字太小...")
else:
    print("你猜对了...")

#进阶:修改上面的代码,利用while循环直到用户把数字猜对后退出循环
import random
number=random.randint(0,100)
print(number)
input_up=-1
while  number != input_up:
    input_up=int(input("请输入数字:"))
    if input_up>number:
        print("你输入的数字过大...")
    elif input_up<number:
        print("你输入的数字太小...")
else:
    print("你猜对了...")
"""

"""
5-4 程序清单
在程序清单4-4的减法测试程序中,它只会在每次运行时生成一个问题.你可以使用一个循环来连续生成问题.那么该怎样
编写一个能生成5个问题的程序呢?按照循环设计策略:
第一步:确定需要被循环的语句,这些语句包括获取两个随机数,提示用户做减法,然后给这个题打分.
第二部:将这些语句放到一个循环里
第三步:添加循环控制变量和循环继续条件来执行5次循环

import random
count = 0
num = 5
while count < 5:
    count += 1
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    if number1 < number2:
        number1, number2 = number2, number1
    print(str(number1) + "-" + str(number2) + "=?")
    answer = input("请输入答案:")
    if answer.isdigit():
        answer = int(answer)
        if answer == number1 - number2:
            pritn("恭喜你答对了....")
        else:
            print("答错了,请重新输入答案,你还有%d次机会" % (num - count))
    else:
        print("你输入的不是数字,请重新输入...")
"""

"""
5-5 程序清单(使用哨兵值控制循环)
让程序读取并计算一组不确定个数的整数的和.输入0表明输入结束,你不必为每一个输入的值设置一个新的变量.
而是只需要使用一个名为data的变量来存储输入值,使用名为sum的变量来存储这些值的和,只要读入一个值并且
它不为0,那就把它赋给data,并把data添加到sum中

import time
data = eval(input("请输入数字:"))
sum = 0
while data != 0:
    data = eval(input("请输入数字:"))  # data在程序中起到的作用就是"哨兵"的作用,如果输入的data的值为0循环结束
    sum += data
    print(sum)
print(sum)
"""
"""
5-6 程序清单
使用嵌套for循环来显示乘法口诀表
#示例1
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"x"+str(i)+"="+str(j*i),end="  ")
    print()

示例2:
print("              MuliplicationTable")
print("    ", end="")
for i in range(1, 10):
    print(format(i, "3d"), end=" ")
print()
print("----------------------------------------")
for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1, 10):
        print(" ", format(i * j, "2d"), end="")
    print()
"""

"""
5-9 程序清单
问题:预测学费
假设今年你所在的大学学费为10000美元并且它以每年7%的速度增长.那么多少年之后学费会翻倍?
思考:在你尝试编写程序之前,首先考虑如何手动解决这个问题.第二年的学费是第一年的学费*1.07,因此,以后每一年的学费都是其前一年学费的*1.07

tuition = 10000  # 学费的初始值
year = 0  # 年数
while tuition < 20000:  # 学费递增小于20000
    tuition *= 1.07  # 学费按照每一年百分之七的速度增长
    year += 1  # 每循环一次年数加1
print("%d年之后学费会翻倍" % (year))
print("翻倍后的学费为:$" + format(tuition, ".2f"))
"""
"""
绘制18*18的网格

import turtle
for y in range(0, 360, 20):
    for x in range(0, 380, 20):
        turtle.goto(x, y)
        turtle.pendown()
    turtle.penup()
for x in range(0, 380, 20):
    for y in range(0, 360, 20):
        turtle.goto(x, y)
        turtle.pendown()
    turtle.penup()
turtle.penup()
turtle.done()
"""

