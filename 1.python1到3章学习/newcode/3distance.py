import turtle

# 第一章练习题

"""
1.1 (显示三个不同的消息)编写程序显示"Welcome to Python"、"Welcome to Computer Science"和"Programming is fun"
print("Welcome to Python")
print("Welcome to Computer Science")
print("Programming is fun")
"""

"""
1.2 (显示同样的消息五次) 编写程序显示"Welcome to Python"
print("Welcome to Python |" * 5)
"""

# 1.3 (显示一种模式) 编写程序显示下面的模式
# print("""
# FFFFFF  U    U  NN    NN
# FF      U    U  NNN   NN
# FFFFFF  U    U  NN N  NN
# FF       U  U   NN  N NN
# FF        UUU   NN   NNN
# """)


"""
1.4 (打印表格)编写程序显示下面的模式
"""
# print("""
# a     a^2    a^3
# 1     1      1
# 2     4      8
# 3     9      27
# 4     16     64
# """)

"""
1.5 (计算表达式) 编写程序显示下面表达式的结果

print(((9.5*4.5)-(2.5*3))/(45.5-3.5))
"""

"""
1.6 (级数求和)编写程序显示1+2+3+4+5+6+7+8+9
print(1+2+3+4+5+6+7+8+9)
"""

"""
1.7 (近似 Π)可以使用下面的公式计算 Π=4*(1-(1/3)+(1/5)-(1/7)+(1/9)-(1/11)

print(4*(1-(1/3)+(1/5)+(1/7)+(1/9)-(1/11)))
print(4*(1-(1/3)+(1/5)-(1/7)+(1/9)-(1/11)+(1/13)-(1/15)))
"""

"""
1.8 (圆的面积和周长) 使用下面的公式编写程序,显示半径是5.5的圆的面积和周长
面积:area=radius*radius*Π
周长:perimeter=2*radius*Π

import math

area = 5.5 * 5.5 * (math.pi)
perimeter = 2 * 5.5 * (math.pi)
print("面积:", area, "周长:", perimeter)
"""

"""
1.9 (矩形的面积和周长) 使用下面的公式编写程序,显示宽度为4.5而高为7.9的矩形的面积和周长

面积: area=width*height
周长: L=2*(width+height)

area = 4.5 * 7.9
L = 2 * (4.5 + 7.9)
print("面积:", area, "周长:", L)
"""

"""
1.10 (平均速度)假设一个人在45分30秒内跑了14公里,编写程序显示每小时的平均速度是多少英里(注意:1英里是1.6公里)

hour = ((45 * 60) + 30) / 60  # 把秒转换成小时
lenghts = 14 / 1.6  # 把公里转换成英里
avg = lenghts / hour
print("每小时平均时速为" + str(format(avg, "3.2f")) + "英里")

"""

"""
1.11 (人口预测)美国人口普查局基于下面假设来预测人口:
    每7秒1人出生
    每13秒1人死亡
    每45秒一个新移民
    编写程序显示接下来5年每一年的人口,假设当前人口数是3120324986,每年有365天。提示:python中,可以使用
    整数除法运算符//来完成整数除法运算,它的结果是一个整数例如:5//4是1(而不是1.25),10//4是2(而不是2.5)

years = int(input("输入年数:"))
second = (24 * 60 * 60) * (365 * years)
born = second // 7
die = second // 13
immigrant = second // 45
New_population = 3120324986 + born + immigrant - die
print("5年后的人口数为:", New_population)
"""

""""
1.12 (Turtle:绘制正方形) 编写程序在屏幕中心绘制正方形

import turtle

turtle.showturtle()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(100)
turtle.goto(50, 50)
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(100)
turtle.hideturtle()

turtle.done()
"""

"""
1.13 (Turtle:绘制十字)

import turtle

turtle.showturtle()
turtle.forward(100)
turtle.left(180)
turtle.goto(50, 0)
turtle.right(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(100)
turtle.hideturtle()
turtle.done()
"""

"""
1.14 (Turtle:绘制三角形)

import turtle

turtle.showturtle()
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.done()
"""

"""
1.15 (Turtle:绘制两个三角形)

import turtle

turtle.showturtle()
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(300)
turtle.right(120)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.hideturtle()

turtle.done()
"""

"""
1.16 (Turtle:绘制四个圆)

import turtle

turtle.showturtle()
turtle.circle(50)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.circle(50)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.circle(50)
turtle.done()
"""

"""
1.17 (Turtle:绘制直线)编写程序绘制一条连接两个点(-39,48)和(50,-50)的红线,然后显示这两个点的坐标

import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(-39, 48)
turtle.pendown()
turtle.write("坐标:x=-30 y=48", font=("华文琥珀", 10, "normal"))
turtle.color("red")
turtle.goto(50, -50)
turtle.color("black")
turtle.write("坐标:x=50 y=-50", font=("华文琥珀", 10, "normal"))
turtle.done()
"""

"""
1.18 (Turtle:绘制五角星)编写程序绘制一个五角星(提示:五角星每个点的内角度是36度)

import turtle

turtle.showturtle()
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.left(144)
turtle.forward(100)
turtle.done()
"""

"""
1.19 (Turtle:绘制多边形)编写程序绘制一个依次连接点(40，-69.28)、(-40,-69.28)、(-80,-9.8)、(-40,69)、(40,69)和(80,0)的多边形

import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(40, -69.28)
turtle.pendown()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80, 0)
turtle.goto(40, -69.28)
turtle.hideturtle()
turtle.done()
"""

"""
1.20 (Turtle:显示立方体)编写程序显示一个立方体

import turtle

turtle.showturtle()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.left(135)
turtle.forward(72)
turtle.pendown()
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.forward(72)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.forward(72)
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.forward(72)
turtle.hideturtle()
turtle.done()
"""

"""
1.21 (Turtle:显示时钟)编写程序显示一个时钟表示时间9:15:00

import turtle

turtle.showturtle()
turtle.circle(100)
turtle.penup()
turtle.goto(-10, -15)
turtle.pendown()
turtle.write("9:15:00", font=("华文琥珀", 10, "normal"))
turtle.penup()
turtle.goto(0, 1)
turtle.pendown()
turtle.write("6", font=("华文琥珀", 10, "normal"))
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.forward(90)
turtle.write("3", font=("华文琥珀", 10, "normal"))
turtle.left(180)
turtle.forward(180)
turtle.write("9", font=("华文琥珀", 10, "normal"))
turtle.left(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(85)
turtle.write("12", font=("华文琥珀", 10, "normal"))
turtle.hideturtle()

turtle.done()
"""

# 第二章练习题
"""
#通过两个坐标位置，求两个坐标之间的距离

x1, y1 = eval(input("请输入x1,y1>:"))
x2, y2 = eval(input("请输入x2,y2>:"))

turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write(str(x1) + str(",") + str(y1))
turtle.goto(x2, y2)
turtle.write(str(x2) + str(",") + str(y2))
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.pendown()
lenght = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
turtle.write("长度=" + str(lenght))

turtle.done()
"""

"""
# 2.1 将摄氏温度转换成华氏温度
celsius = eval(input("摄氏温度>:"))
fahrenheit = (9 / 5) * celsius + 32
print("华氏温度:", fahrenheit)
"""

"""
# 2.2 计算圆柱体的体积：编写一个读取圆柱的半径和高，并利用下面的公式计算圆柱体底面积和体积的程序：

# 圆柱面积=半径*半径*Π
# 圆柱体积=圆柱面积*高

import math

radius = eval(input("请输入圆柱半径:"))
lenght = eval(input("请输入圆柱高:"))
area = radius * radius * math.pi
print("圆柱面积:", area)
volume = area * lenght
print("圆柱体积:", volume)
"""

"""
# 2.3 (将英尺数转换成米数):编写一个程序，它读取英尺数，然后将它转换成米数，并显示结果(一英尺等于0.305米)
feet = eval(input("请输入英尺:"))
meters = round(feet * 0.305, 2)
print("{}英尺等于米{}".format(feet, meters))
"""

"""
# 2.4 (将磅转换成千克)：编写一个将镑转换成千克的程序，这个程序提示用户输入磅数，转换为千克数，并显示结果
,一磅等于0.4535924千克

pounds = eval(input("请输入英镑:"))
kilograms = pounds * 0.4535924
print("{}英镑等于{}千克".format(pounds, kilograms))
"""

"""
2.5 (财务应用程序:计算消费):编写一个读取小计和酬金率然后计算小费以及合计金额的程序，
例如：如果用户输入的小计是10，酬金率是15%，程序就会显示小费是1.5，合计金额是
11.5；


subtotal = eval(input("输入小计:"))
rates = eval(input("输入酬金率:"))
rate = ("%.f%%" % (rates * 100))
tip = subtotal * rates
total = subtotal + tip
print("小计:{},酬金率:{}".format(subtotal, rate))
print("小费:{},小计:{},合计金额:{}".format(tip, subtotal, total))
"""

"""
2.6 (对一个整数中的各位数字求和)：编写一个程序，读取0到1000之间的整数，并计算它各位数字之和。例如：如果一个整数是932，那么它各位数字之和就是
14,(提示：使用%来提取数字，使用//运算符来去除掉被提取的数字。例如：932%10=2，而932//10=93)


for i in range(0, 1000):
    bai = (i // 100)
    shi = (i // 10 % 10)
    ge = i % 10
    sums = bai + shi + ge
    # print("百{},十{},个{},合计:{}".format(bai,shi,ge,sums))
    print("数字:" + str(bai) + str(shi) + str(ge) + " 合计=" + str(sums))
"""

"""
2.7 (计算年数和天数):编写一个程序，提示用户输入分钟数(例如：1000000000),然后将分钟转换为
年数和天数，并显示出来

#第一种写法:
minutes = eval(input("请输入分钟数:"))
residue = minutes % 525600
days = residue / 1440
years = (minutes - residue) / 525600
print("%d年零%d天" % (years, days))



#第二种写法:
min=eval(input("请输入分钟数:"))
days=min//(60*24)
years=days//365
days=days%365
min=min%(60*24)
print(years,"年",days,"天",min,"分钟")

"""

"""
2.8 (科学：计算能量):编写一个程序，计算将水从初始温度加热到最终温度所需要的能量，你的程序应该提示用户输入以千克计算的水量，以及水的初始温度和最终温度。
计算公式是:Q=M*(final_temperature- initial_temperature)* 4184
这里的M是按千克计的水量，温度为摄氏温度，热量Q以焦耳计


water_kilograms = eval(input("输入水量(公斤):"))
initial_temperature = eval(input("输入初始温度:"))
final_temperature = eval(input("输入最终温度:"))
Q = water_kilograms * (final_temperature - initial_temperature) * 4184
print("需要的能量是:", Q)

"""

"""
2.9 (科学：风寒温度)室外有多冷？只有温度值是不足以提供答案的。其他因素，例如：风速、相对湿度和光照都对室外寒冷程度有很大影响。在2001年，国家气
象局(NWS)实行以新的利用温度和风速来衡量风寒温度，公式如下：

风寒温度=35.74+(0.6215*华氏温度)-(35.75*(风速**0.16))+(0.4275*华氏温度*(风速** 0.16)


degree_Fahrenheit = eval(input("输入华氏温度:"))
wind_speed = eval(input("输入风速(每小时):"))
Wind_chill = 35.74 + (0.6215 * degree_Fahrenheit) - (35.75 * (wind_speed ** 0.16)) + (
        0.4275 * degree_Fahrenheit * (wind_speed ** 0.16))
print("风寒温度是:", Wind_chill)

"""

"""
2.10 (物理方面:计算跑道长度)假定给出飞机的加速度a和起飞速度v，可以根据以下公式计算出飞机起飞所需要的最短跑道长度

长度=(v**2)/(2*a)
编写一个程序，提示用户输入以米/秒(m/s)为单位的v,和以米/秒的平方(m/(s**2))位单位的a,然后显示最短跑道长度。


v = eval(input("请输入飞行速度:"))
a = eval(input("请输入加速度:"))
lenght = (v ** 2) / (2 * a)
print("最短的跑道长度是:", lenght)

"""

"""
2.11 (金融应用程序:投资额):假如你想将一笔钱以固定年利率存入账户。如果你希望三年之后账户中有5000美元,你现在需要存多少钱？使用下面的公式
可以算出初始存款：

最初存款额=最终金额/((1+月利率<年利率/100/12>)**月数)

final_account = eval(input("请输入最终金额:"))
annual_interest_rate = eval(input("请输入年利率:"))
years = eval(input("请输入年数:"))
deposit_value = (final_account) / ((1 + (annual_interest_rate / 100 / 12)) ** (years * 12))
print(deposit_value)
"""

"""
2.12 (打印表格)：编写一个打印表格程序
"""

a = """
a   b  a**b
1   2  1
2   3  8
3   4  81
4   5  1024
5   6  15625
"""

"""
2.13 (分割数字)：编写一个程序，提示用户输入四位整数并以反方向顺序显示
integer = (input("请输入数字:"))
integer = (integer[::-1])
print("倒序的数字:", integer)

"""

"""
这道题答案不知是否正确

2.14 (几何方面:三角形的面积)：编写一个程序，提示用户输入三角形的三个顶点(x1,y1)、(x2,y2)、(x3,y3)然后显示
它的面积.

x1 = 1.5
y1 = -3.4
x2 = 4.6
y2 = 5
x3 = 9.5
y3 = -3.4
S = (1 / 2) * (x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)
print(S)
"""

"""
2.15 (几何方面:正六边形的面积)：编写一个程序，提示用户输入正六边形的边长并显示它的面积
计算正六边形面积的公式是:((3*(3**0.5))/2)*(s**2),其中s是边长

s = eval(input("请输入正六边形边长:"))
area = ((3 * (3 ** 0.5)) / 2) * (s ** 2)
print("正六边形面积:", area)
"""

"""
2.16 (物理方面:加速度):平均加速度的定义：是速度变化量除以变化所占用的时间，如下公式所示：
a=(v1-v0)/t
编写一个程序：提示用户输入以米每秒为单位的初始化速度v0和末速度v1，以秒位单位速度变化所占用的时间
t,然后显示平均加速度


v1 = eval(input("请输入(末速度):"))
v0 = eval(input("请输入(初始化速度):"))
t = eval(input("请输入(所占用时间):"))
a = (v1 - v0) / t
print("平均加速度为:", a)

"""

"""
2.17 (健康应用程序:计算BMI):身体质量指数(BMI)是以体重衡量健康程度的一种指数,
BMI=以千克的体重为单位/以米为单位的身高的平方

--此题:书里给的公式1英尺=0.0254米是错误的，正确应该是1英尺=0.3048米


pounds = eval(input("请输入磅数:"))
kilograms = pounds * 0.4535924
print(kilograms)

feet = eval(input("请输入英尺:"))
meters = feet * 0.305
print(meters)

BMI = kilograms / meters ** 2
print("BMI的值为:", BMI)
"""

"""
2.18 (当前时间)程序清单2-7给出的程序显示当前GMT时间。修改程序使之提示用户输入时区,这个时区用距离GMT的小时数表示
,然后显示指定时区的时间

import time

zongmiaoshu = time.time()
print((zongmiaoshu)) - -从1970年至当前时间的秒数包括微秒

totalseconds = int(time.time())
print(totalseconds)  # 总秒数取整

dangqianmiaoshu = totalseconds % 60  # 当前秒数
print(dangqianmiaoshu)

zongfenzhongshu = totalseconds // 60  # 总分钟数
print(zongfenzhongshu)  # 26181546

dangqianfenzhongshu = zongfenzhongshu % 60  # 当前分钟数
print(dangqianfenzhongshu)

zongxiaoshishu = zongfenzhongshu // 60  # 总小时数
print(zongxiaoshishu)

input_shiqu = eval(input("请输入时区:"))

xianzaixiaoshishu = (zongxiaoshishu % 24) - input_shiqu  # 当前小时数  GMT时格林威治时间在加8个小时就时中国时区
print(xianzaixiaoshishu)

print("{}:{}:{}".format(xianzaixiaoshishu, dangqianfenzhongshu, dangqianmiaoshu))
"""

"""
2.19 (金融应用程序:计算未来投资额) 使用下面的公式编写一个投资额、年利率和年数然后显示未来投资额的程序:
未来投资额=投资额*(1+月投资率)**月数

invested = eval(input("输入投资额:"))
Apr = eval(input("输入年利率:"))
number_years = eval(input("输入年数:"))
Future_investment = invested * ((1 + (Apr / 100 / 12)) ** (number_years * 12))
print("未来投资额为:" + str(format(Future_investment, "6.2f")))
"""

"""
2.20 (金融应用程序:计算利息)如果你知道差额和百分比的年利率，你可以使用下面的公式计算下个月月供的利息
利息=差额*(年利率/1200)

balance = int(input("输入差额:"))
Apr = eval(input("输入年利率:"))
interest = balance * (Apr / 1200)
print("利息:" + str(format(interest, "3.2f")) + str("%"))
"""

"""
2.21 (金融应用程序：复利值)假设你每月存100美元到一个年利率为5%的储蓄账户,因此
月利率时0.05/12=0.00417。

第一个月后,账户里的数目变为：
100*(1+0.0.00417)=100.417

第二个月后,账户里的数目变为:
(100+100.417)*(1+0.00417)=201.252

第三个月后,账户里的数目变为:
(100+201.252)*(1+0.00417)=302.507

以此类推:
        编写一个程序,提示用户键入每月存款数然后显示六个月后的账户总额

monthly_interest_rate = 0.05 / 12
month1 = 100 * (1 + monthly_interest_rate)
month2 = (month1 + 100) * (1 + monthly_interest_rate)
month3 = (month2 + 100) * (1 + monthly_interest_rate)
month4 = (month3 + 100) * (1 + monthly_interest_rate)
month5 = (month4 + 100) * (1 + monthly_interest_rate)
month6 = (month5 + 100) * (1 + monthly_interest_rate)
print("6个月后账户总额为:" + str(format(month6, "5.2f")))
"""

"""
练习题1.11:(人口预测)美国人口普查局基于下面假设来预测人口:
    每7秒1人出生
    每13秒1人死亡
    每45秒一个新移民
    编写程序显示接下来5年每一年的人口,假设当前人口数是3120324986,每年有365天。提示:python中,可以使用
    整数除法运算符//来完成整数除法运算,它的结果是一个整数例如:5//4是1(而不是1.25),10//4是2(而不是2.5)

2.22 (人口预测):改写练习题1.11来提示用户键入年数,然后显示那么多年后人口数:

years = int(input("输入年数:"))
second = (24 * 60 * 60) * (365 * years)
born = second // 7
die = second // 13
immigrant = second // 45
New_population = 3120324986 + born + immigrant - die
print("5年后的人口数为:", New_population)
"""

"""
2.23 (Turtle:绘制四个圆)编写一个程序，提示用户输入半径并在屏幕中央画四个圆

radius = eval(input("输入半径:"))
import turtle

turtle.showturtle()
turtle.circle(radius)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.circle(radius)
turtle.hideturtle()
turtle.done()
"""

"""
2.24 (Turtle:绘制四个正六边形,在屏幕中央画四个正六边形)

import turtle

radius = eval(input("输入半径:"))
turtle.showturtle()
turtle.circle(radius, steps=6)
turtle.penup()
turtle.goto(105, 0)
turtle.pendown()
turtle.circle(radius, steps=6)
turtle.penup()
turtle.goto(105, 100)
turtle.pendown()
turtle.circle(radius, steps=6)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.circle(radius, steps=6)
turtle.hideturtle()
turtle.done()
"""

"""
2.25 (Turtle:绘制一个矩形)提示用户输入矩形中心、长和宽,然而显示这个矩形

import turtle

Centres1 = int(input("x:"))
Centres2 = int(input("y:"))
Chang = eval(input("输入长:"))
Kuan = eval(input("输入宽:"))

turtle.showturtle()
turtle.penup()
turtle.goto(Centres1, Centres2)
turtle.pendown()
turtle.forward(Kuan)
turtle.left(90)
turtle.forward(Chang)
turtle.left(90)
turtle.forward(Kuan)
turtle.left(90)
turtle.forward(Chang)
turtle.hideturtle()
turtle.done()

"""

"""
2.26 (Turtle:绘制一个圆)提示用户输入圆心和半径并在屏幕中央显示圆和它的面积

import turtle
import math

yuanxin1 = eval(input("x:"))  # x=0
yuanxin2 = eval(input("y:"))  # y=100
radius = eval(input("输入半径:"))  # radius=100
area = math.pi * (radius ** 2)
turtle.showturtle()
turtle.circle(radius)
turtle.penup()
turtle.goto(yuanxin1, yuanxin2)
turtle.pendown()
turtle.write("面积:" + str(format(area, "7.2f")))

turtle.done()
"""

# 第三章练习题

"""
3.1 (几何学:一个五边形的面积)编写一个程序,提示用户输入提示用户输入五边形顶点到中心的距离r,然后
计算出五边形的面积

计算五边形面积的公式是:Area=5*s*s/(4*tan(math.pi/5))，这里的s是边长,边长的计算公式是：s=2*r*sin(math.pi/5)


import math

Distance = eval(input("输入距离:"))
Side_length = 2 * Distance * math.sin(math.pi / 5)
Area = 5 * Side_length * Side_length / (4 * math.tan(math.pi / 5))

import turtle

turtle.showturtle()
turtle.circle(100, steps=5)
turtle.left(90)
turtle.goto(0, 100)
turtle.right(180)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.write("R", font=("华文琥珀", 15, "normal"))
turtle.penup()
turtle.left(180)
turtle.goto(0, 100)
turtle.pendown()
turtle.write("面积:"+str(format(Area,"4.2f")))
turtle.hideturtle()

turtle.done()
"""

"""
3.2 (几何学:大圆距离)大圆距离是球面上两点之间的距离.假设(x1,y1)和(x2,y2)是两点的经度和纬度,两点之间的大圆距离可以用下面的公式计算：
d=radius*arccos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))

编写一个程序,提示用户输入地球表面两点经度和纬度的度数然后显示它们的大圆距离。地球的平均半径为6371.01km。注意:你需要使用math.radians函数
将度数转换成弧度数,因为Python三角函数使用的都是弧度。公式中的经纬度时西经和北纬。用负数表示东经和南纬.

import math

x1, y1 = eval(input("请输入x1,y1>:"))
x2, y2 = eval(input("请输入x2,y2>:"))
radius = 6371.01
d = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(
    math.radians(x2)) * math.cos(
    math.radians(y1) - math.radians(y2)))

print("两点之间大圆的距离:" + str(format(d, "7.3f")) + "km")
"""

"""
3.3 (几何学:估算面积)从网站www.gps-data-team.com/map/上找到佐治亚洲亚特兰大、佛罗里达州奥兰多、大草原佐治亚、北卡罗来纳州夏洛特的
GPS位置,然后计算出这四个城市所围成的区域的大概面积。(提示:可以使用上题3.2中的公式计算两个城市之间的距离。将多边形划分成两个三角形，然后
用编程题2.14中的公式计算三角形的面积)

--不会做
"""

"""
3.4 (几何学:五角形的面积)五角形的面积可以使用下面的公式计算(s是边长):
Area=(5*(s**2))/(4*(tan(math.pi/5)))
编写一个程序,提示用户输入五角形的边长,然后显示面积

import math

s = eval(input("输入五角形的边长:"))
area = (5 * (s ** 2)) / (4 * (math.tan(math.pi / 5)))
print("五角形的面积是:" + str(format(area, "5.3f")))
"""

"""
3.5 (几何学:一个正多边形的面积)正多边形是边长相等的多边形,而且所有的角相等。计算正多边形的面积的公式是:
Area=(n*(s**2))/(4*math.tan(math.pi/n))

import math

num = eval(input("输入数目:"))
side = eval(input("输入边长:"))
Area = (5 * (side ** 2)) / (4 * math.tan(math.pi / num))
print("正多边形的面积是:" + str(format(Area, "5.3f")))
"""

"""
3.6 (找出ASCLL码的字符)编写一个程序,接受一个ASCLL码值(一个0-127之间的整数)。然后显示它对应的字符。例如:如果用户输入
97,程序将显示字符a。

String = int(input("请输入字符编码:"))
print("输入字符编码是:" + str(String) + ",对应的字符是:" + chr(String))
"""

"""
3.7 (随机字符)编写一个程序,使用time.time()函数显示一个大写的随机字符

import time

a = int(time.time())
a = a % 26
print(chr(ord("A") + a))  # 得到的结果是：A-Z的大写字母
print(chr(ord("a") + a))  # 得到的结果是：a-z的小写字母
"""

"""
3.8 (金融应用程序:货币单元)改写程序清单3-4,修正将浮点数转换成整数的过程中带来的精度损失。输入一个整数,它的后两位
数字代表美分。例如:输入1156,它代表11美元56美分

money = eval(input("input money:"))
meiyuan = int(money // 100)
meifen = money % 100
print(meiyuan, "美元", meifen, "美分")



#扩展案例: 元、角、分 展示,例如输入:10.03
money = eval(input("输入money:"))
yuan = int(money)
jiao = int((money * 10) % 10)
fen = int(round((money * 100)) % 10)  # 这里需要注意的是:money*100得到的结果是1002.9999999999999,这里需要用round函数四舍五入到1003
print(yuan, "元", jiao, "角", fen, "分")
"""

"""
3.9 (金融应用程序:工资表) 编写一个程序,读取下面的信息,然后打印一个工资表
雇员姓名:例如(史密斯)
一周工作时间:例如(10)
每小时报酬:例如(9.75)
联邦预扣税率:例如(20%)
州预扣税率:例如(9%)

name = input("输入姓名:")
Weekly_working_hours = eval(input("输入周工作时间:"))
Hourly_rate = eval(input("每小时报酬:"))
Federal_rate = eval(input("联邦预扣税率:"))
State_rate = eval(input("州预扣税率:"))
Gross_pay = Weekly_working_hours * Hourly_rate  # 工资总额
Federal_with = Gross_pay * Federal_rate  # 联邦扣缴
State_with = Gross_pay * State_rate  # 州扣缴
State_with1 = Gross_pay * State_rate
State_with1 = str(State_with1)
n5, n6 = State_with1.split(".")
State_with1 = n5 + "." + n6[0:2]
Total_deduction = Federal_with + State_with  # 总扣缴
Total_deduction1 = Federal_with + State_with
Total_deduction1 = str(Total_deduction1)
n1, n2 = Total_deduction1.split(".")
Total_deduction1 = n1 + "." + n2[0:2]
Net_pay = Gross_pay - Total_deduction  # 最终支付
Net_pay = str(Net_pay)
n3, n4 = Net_pay.split(".")
Net_pay = n3 + "." + n4[0:2]

print("姓名:",name,"\n"
      "工作时间:",float(Weekly_working_hours),"\n"
      "每小时报酬:","$"+str(Hourly_rate),"\n"
      "工资总额:","$"+str(Gross_pay),"\n"
      "Deductions:","\n"
      "\t","联邦扣缴(20%):","$"+str(Federal_with),"\n"
      "\t","州扣缴(9.0%):","$"+str(State_with1),"\n"
      "\t","总扣缴:","$"+str(Total_deduction1),"\n"
      "最终支付:","$"+str(Net_pay)
      )
"""



# 3.10 (Turtle:显示统一码)编写一个程序:显示希腊字母   

# import turtle
# turtle.showturtle()
# turtle.write("\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8")
# turtle.done()


# **这里有个小技巧:如果我们不知道怎么"特殊字符"怎么写出来,可以通过word粘贴和复制到
#     pycharm中,然后用ord()函数求出字符编码,然后再把字符编码通过hex()转换成十六进制编码
#     再把十六进制编码前面加"\u",就可以打印出特殊字符
# a="【"
# print(ord(a))
# b=12304
# print(hex(b))
# print("\u3010")


"""
3.11 (反向数字)编写一个程序,提示用户输入一个四位整数,然后显示颠倒各位数字后的数

a = int(input("输入四位整数:"))
b = a % 10
c = a // 10
d = c % 10
e = c % 10
f = c // 10
g = f % 10
h = f // 10
print("数字倒序结果:", b, e, g, h)
"""

"""
3.12 (Turtle:绘制一个五角星)编写一个程序,提示用户输入五角星的边长,
然后绘制一个五角星(提示:五角星每个点的内角是36度),用180-36=144

import turtle
Length=eval(input("输入五角星边长:"))
turtle.showturtle()
turtle.forward(Length)
turtle.right(144)
turtle.forward(Length)
turtle.right(144)
turtle.forward(Length)
turtle.right(144)
turtle.forward(Length)
turtle.right(144)
turtle.forward(Length)
turtle.hideturtle()
turtle.done()
"""
"""
3.13 (Turtle:显示一个STOP牌)编写一个程序,显示一个STOP牌,六边形是红颜色的而文字是白色的(六边形的
内角度数是120)用180-120=60

Length = eval(input("输入六边形边长:")) #输入150
import turtle

turtle.showturtle()
turtle.begin_fill()
turtle.forward(Length)
turtle.right(60)
turtle.forward(Length)
turtle.right(60)
turtle.forward(Length)
turtle.right(60)
turtle.forward(Length)
turtle.right(60)
turtle.forward(Length)
turtle.right(60)
turtle.forward(Length)
turtle.penup()
turtle.goto(55, -134)
turtle.pendown()
turtle.pencolor("white")
turtle.write("STOP", font=("Britannic Bold", 20))
turtle.color("red")
turtle.end_fill()
turtle.done()
"""

"""
3.14 (Turtle:绘制一个奥运五环标志) 编写一个程序,提示用户输入环的半径,
然后画出大小相等的五环,颜色依次为:蓝、黑、红、黄、绿    

import turtle

radius = eval(input("输入半径:"))  # 输入100
turtle.showturtle()

turtle.penup()
turtle.goto(-180, 0)
turtle.pensize(10)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(radius)
turtle.penup()
turtle.goto(40, 0)
turtle.pensize(10)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(radius)
turtle.penup()
turtle.goto(260, 0)
turtle.pensize(10)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(radius)

turtle.penup()
turtle.goto(-70, -100)
turtle.pensize(10)
turtle.pendown()
turtle.pencolor("yellow")
turtle.circle(radius)

turtle.penup()
turtle.goto(150, -100)
turtle.pensize(10)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(radius)

turtle.done()
"""

"""
3.15 (Turtle:绘制一个笑脸)编写一个程序,绘制一个笑脸

import turtle

turtle.showturtle()
turtle.circle(100)
turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.left(145)
turtle.forward(50)
turtle.left(180)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.left(70)
turtle.forward(50)
turtle.penup()
turtle.goto(0, 105)
turtle.pendown()
turtle.left(145)
turtle.forward(25)
turtle.left(180)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.left(120)
turtle.forward(50)
turtle.penup()
turtle.goto(-40, 165)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.color("black")
turtle.end_fill()
turtle.penup()
turtle.goto(20, 165)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(10)
turtle.end_fill()
turtle.hideturtle()

turtle.done()
"""

"""
3.16 (Turtle:绘制图形)编写一个程序,绘制一个三角形、一个正方形、一个五边形、一个六边形和一个八边形,注意这些图形底边是
平行于x轴的(提示:将turtle的朝向调整60度就可以使三角形的底边平行与x轴)


import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(-400, 0)
turtle.color("black")
turtle.pendown()
turtle.begin_fill()
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.left(120)
turtle.forward(150)
turtle.end_fill()

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-20, 0)
turtle.pendown()

turtle.begin_fill()
turtle.color("black")
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.end_fill()

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.forward(80)
turtle.left(60)
turtle.forward(80)
turtle.left(60)
turtle.forward(80)
turtle.left(60)
turtle.forward(80)
turtle.left(60)
turtle.forward(80)
turtle.left(60)
turtle.forward(80)
turtle.left(60)
turtle.end_fill()

turtle.penup()
turtle.goto(440, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.forward(60)
turtle.left(45)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
"""


"""
3.17 (Turtle:三角形面积)编写一个程序,提示用户输入一个三角形的三点P1,P2,P3,然后在三角形的下面显示三角形的面积

x1, y1 = eval(input("请输入x1,y1>:"))
x2, y2 = eval(input("请输入x2,y2>:"))
x3, y3 = eval(input("请输入x3,y3>:"))
S = (1 / 2) * (x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)
import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(x1, y2)
turtle.write("p2:" + "(" + str(x1) + "," + str(y1) + ")")
turtle.pendown()
turtle.goto(x2, y2)
turtle.write("p3:" + "(" + str(x2) + "," + str(y2) + ")")
turtle.goto(x3, y3)
turtle.write("p1:" + "(" + str(x3) + "," + str(y3) + ")")
turtle.goto(x1, y2)
turtle.penup()
turtle.goto(-50, -70)
turtle.pendown()
turtle.write("三角形面积:" + str(S))

turtle.done()
"""

"""
3.18 (Turtle:三角形的角)修改程序清单3-2 ,编写一个程序,提示用户输入三角形的三点:p1,p2和p3,然后显示它的角度

import math

x1, y1, x2, y2, x3, y3 = eval(input("输入三个顶点坐标:"))  # 输入:-50,-50,-10,50,50,-30
a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))
A = round(A * 100) / 100.0
B = round(B * 100) / 100.0
C = round(C * 100) / 100.0
print("The three angles are", A, B, C)

import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.write("p2:(" + str(A) + ")")
turtle.pendown()
turtle.goto(x2, y2)
turtle.write("p1:(" + str(B) + ")")
turtle.goto(x3, y3)
turtle.write("p3:(" + str(C) + ")")
turtle.goto(x1, y1)

turtle.done()
"""

"""
3.19 (Turtle:绘制一条直线)编写一个程序,提示用户输入两点,然后绘制一条连接两点的线并且显示这些点的坐标

x1, y1 = eval(input("输入x1,y1:"))  # 输入:50,-50
x2, y2 = eval(input("输入x2,y2:"))  # 输入:-39,49
import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.write("(" + str(x1) + "," + str(y1) + ")")
turtle.pendown()
turtle.goto(x2, y2)
turtle.write("(" + str(x2) + "," + str(y2) + ")")
turtle.done()
"""