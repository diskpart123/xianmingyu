"""
4.1 (代数方面:解一元二次方程)例如:(a*(x**2))+(b*x)+c=0的平方根可以使用下面的公式获取
r1 = (-b + (math.sqrt(b ** 2 - (4 * a * c)))) / 2 * a
r2 = (-b - (math.sqrt(b ** 2 - (4 * a * c)))) / 2 * a

b ** 2 - (4 * a * c) 被称为二次方程的判别式.如果它为正,那么方程有两个实数根.如果它为零
,那么方程有一个根.如果判别式为零,则显示一个根.否则,显示"The equation has no real roots."
import math

a, b, c = eval(input("请输入a,b,c:"))
if b ** 2 - (4 * a * c) > 0:
    r1 = (-b + (math.sqrt(b ** 2 - (4 * a * c)))) / 2 * a
    r2 = (-b - (math.sqrt(b ** 2 - (4 * a * c)))) / 2 * a
    print("The roots are:", format(r1, "8.6f"), "and", format(r2, "6.5f"))
elif b ** 2 - (4 * a * c) == 0:
    r1 = (-b + (math.sqrt(b ** 2 - (4 * a * c)))) / 2 * a
    print("The root is", r1)
else:
    print("The equation has no real roots")

"""

"""
4.2 (游戏:三个数相加) 程序清单4-1中的程序产生两个整数,然后提示用户输入这两个整数的和
修改这个程序产生三个一位整数,提示用户输入这三个整数的和

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
print("%d+%d+%d=?,请输入答案:" % (num1, num2, num3))
answer = eval(input(":"))
if answer == num1 + num2 + num3:
    print("你输入的答案是%d,答案是正确!" % (answer))
else:
    print("对不起,输入答案是%d不正确,正确的答案是:%d,继续努力..." % (answer, num1 + num2 + num3))
"""

"""
4.3 (代数:解2*2线性方程)你可以使用克莱姆法则解下面的线性方程2*2系统:

(a*x)+(b*y)=e
               x=((e*d)-(b*f))/((a*d)-(b*c))     y=((a*f)-(e*c))/((a*d)-(b*c))
(c*x)+(d*y)=f

编写程序,提示用户输入a,b,c,d,e和f,然后显示结果.如果a*d-b*c为零,呈现"The equation has no solution"

a, b, c, d, e, f = eval(input("输入数字:"))
if a * d - b * c == 0:
    print("The equation has no solution")
else:
    x = ((e * d) - (b * f)) / ((a * d) - (b * c))
    y = ((a * f) - (e * c)) / ((a * d) - (b * c))
    print("x is", x, "y is", y)
"""

"""
4.4 (游戏:学习加法) 编写一个程序产生两个100以下的整数,然后提示用户输入这两个整数的和,
如果答案是正确的,程序报告结果为真,否则为假.这个程序类似与程序清单4-1

import random

num1 = random.randrange(0, 99)
num2 = random.randrange(0, 99)
answer = eval(input("输入答案:"))
if answer == num1 + num2:
    print(True)
else:
    print(False)
"""

"""
4.5 (找未来数据) 编写程序提示用户输入表示今天是一周内哪一天的数字(星期天是0,星期一是1,以此类推,星期六是6)
还要提示用户输入今天之后到未来某天的天数,然后显示未来这天是星期几.
提示:再过Y天是星期几，答：星期（X+Y-1）/7的余数

day = eval(input("输入数字:"))
shuoming1 = ""
if day == 1:
    shuoming1 = "星期一"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
elif day == 2:
    shuoming1 = "星期二"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
elif day == 3:
    shuoming1 = "星期三"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
elif day == 4:
    shuoming1 = "星期四"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
elif day == 5:
    shuoming1 = "星期五"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
elif day == 6:
    shuoming1 = "星期六"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
elif day == 0:
    shuoming1 = "星期天"
    print("您输入的数字是:%d,代表:%s" % (day, shuoming1))
else:
    print("输入不正确")

day_1 = eval(input("输入开始日期<day_1>:"))  # 输入今天星期几代表的数字,如5,代表是星期五
shuoming2 = ""
if day_1 == 1:
    shuoming2 = "星期一"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
elif day_1 == 2:
    shuoming2 = "星期二"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
elif day_1 == 3:
    shuoming2 = "星期三"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
elif day_1 == 4:
    shuoming2 = "星期四"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
elif day_1 == 5:
    shuoming2 = "星期五"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
elif day_1 == 6:
    shuoming2 = "星期六"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
elif day_1 == 0:
    shuoming2 = "星期天"
    print("您输入的数字是:%d,代表:%s" % (day_1, shuoming2))
else:
    print("输入不正确")

interval = eval(input("interval:"))  # 再输入这个数字代表再过几天
what_day = (day_1 + interval - 1) % 7  # 算出最终是星期几
shuoming3 = ""
if what_day == 1:
    shuoming3 = "星期一"
    print("数字为:%d,%s" % (what_day, shuoming3))
elif what_day == 2:
    shuoming3 = "星期二"
    print("数字为:%d,%s" % (what_day, shuoming3))
elif what_day == 3:
    shuoming3 = "星期三"
    print("数字为:%d,%s" % (what_day, shuoming3))
elif what_day == 4:
    shuoming3 = "星期四"
    print("数字为:%d,%s" % (what_day, shuoming3))
elif what_day == 5:
    shuoming3 = "星期五"
    print("数字为:%d,%s" % (what_day, shuoming3))
elif what_day == 6:
    print("星期六")
elif what_day == 0:
    shuoming3 = "星期日"
    print("数字为:%d,%s" % (what_day, shuoming3))
else:
    print("输入不正确")
"""

"""
4.6 (健康应用程序:BMI) 修改程序清单4-6让用户输入磅表示的用户体重以及英尺英寸表示用户的身高,
例如:如果一个人有5英尺10英寸,你就可以输入英尺5和英寸
BMI=体重/身高的平方
1磅=0.453千克
1英尺=12英寸
1英寸=0.0254米

# 解题思路
# 第一步:统一把身高单位转换为英寸
# 第二步:把转换好的英寸相加
# 第三步:把磅转换为千克

weight = eval(input("请输入weight:"))
feet = eval(input("请输入feet:"))  # feet代表英尺
inche = eval(input("请输入inche:"))  # inche代表英寸
kg_weight = weight * 0.453
feets = feet * 12  # 英尺转换成英寸
inches = inche + feets
meter = inches * 0.0254  # 英寸转换成米
BMI = kg_weight / (meter ** 2)
if BMI < 18.5:
    print("超轻")
elif BMI >= 18.5 and BMI < 25.0:
    print("标准")
elif BMI >= 25.5 and BMI < 30.0:
    print("超重")
else:
    print("痴肥")
"""

"""
4.7 (财务应用程序:货币单位)修改程序清单3-4为只显示非零值的程序,单一的值用单数表示,
例如:ldollar(美元)和lpenny(美分),而大于1的值用双数表示,例如:2dollars(美元)和3pennies(美分)


amount=eval(input("请输入金额:"))
remainingamount=int(amount*100) #将钱数转换成分数  1156

numberofonedollars=remainingamount//100 #得到美元的个数  11
remainingamount=remainingamount%100 #得到剩余的分数  56

numberofquarters=remainingamount//25 #得到两角五分硬币的个数   2
remainingamount=remainingamount%25 #得到剩余的分数  6

numberofdimes=remainingamount//10 #得到一角硬币的个数  0
remainingamount=remainingamount%10 #得到剩余的分数  0

numberofnickels=remainingamount //5 #得到五分硬币的个数
remainingamount=remainingamount%5 #得到剩余的分数

numberofpennies=remainingamount
print("Your amount",amount,"consists of","\n"
"\t",numberofonedollars,"dollars","\n"
      "\t",numberofquarters,"quarters","\n"
      "\t",numberofdimes,"dimes","\n"
      "\t",numberofnickels,"nickels","\n"
      "\t",numberofpennies,"pennies","\n")

#修改后程序
amount = eval(input("请输入金额:"))
remainingamount = int(amount * 100)  # 将钱数转换成分数

if remainingamount // 100:
    numberofonedollars = remainingamount // 100  # 得到美元的个数
    remainingamount = remainingamount % 100  # 得到剩余的分数

if remainingamount // 25:
    numberofquarters = remainingamount // 25  # 得到两角五分硬币的个数
    remainingamount = remainingamount % 25  # 得到剩余的分数

if remainingamount // 10:
    numberofdimes = remainingamount // 10  # 得到一角硬币的个数
    remainingamount = remainingamount % 10  # 得到剩余的分数

if remainingamount // 5:
    numberofnickels = remainingamount // 5  # 得到五分硬币的个数
    remainingamount = remainingamount % 5  # 得到剩余的分数

numberofpennies=remainingamount
print("Your amount",amount,"consists of","\n"
"\t",numberofonedollars,"dollars","\n"
      "\t",numberofquarters,"quarters","\n"      
      "\t",numberofnickels,"nickels","\n"
      "\t",numberofpennies,"pennies","\n")
"""

"""
4.8 (对三个整数排序) 编写一个程序提示用户输入三个整数,然后以升序显示它们

a, b, c = eval(input("请输入数字:"))
if a > b > c:
    print(a, b, c)
elif a > c > b:
    print(a, c, b)
elif b > a > c:
    print(b, a, c)
elif b > c > a:
    print(b, c, a)
elif c > a > b:
    print(c, a, b)
elif c > b > a:
    print(c, b, a)
"""

"""
4.9 (金融方面:比较价钱) 假设你购买大米的时候发现它有两种包装.你会想编写一个程序比较这两种
包装价钱.程序提示用户输入每种包装的重量和价钱,然后显示价格更好的那种包装

pack1_price = eval(input("输入单价:"))
pack1_weight = eval(input("输入重量:"))
pack1 = pack1_price * pack1_weight
pack2_price = eval(input("输入单价:"))
pack2_weight = eval(input("输入重量:"))
pack2 = pack2_weight * pack2_price
if pack1 > pack2:
    print("pack1,has the better price")
else:
    print("pack2,has the better price")
"""

"""
4.10 (游戏:乘法测验) 程序清单4-4随机产生一个减法问题.修改程序随机产生两个小于100的整数
乘法

import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)
print(str(num1) + "*" + str(num2) + "=?")
answer = eval(input("请输入答案:"))
if answer == num1 * num2:
    print("答案正确..." + str(num1) + "*" + str(num2) + "=" + str(answer))
else:
    print("数字:" + str(answer) + "答案错误...正确答案是:" + str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
"""

"""
4.11 (找出一个月中的天数) 编写程序提示用户提示年和月,然后显示这个月的天数,例如:如果用户如输入年份为2000,月份2
这里程序应该显示2000年二月份有29天,如果用户输入年份为2005,月份输入3这个程序应该显示2005年三月份有31天
"""
year=eval(input("输入年份:"))
month=eval(input("输入月份:"))
day=""
if (year%4==0 and year%100!=0) or (year%400==0):
    if month==2:
        day=29
        print(year,"年",month,"月份有",day,"天")
else:
    if month==1:
        day=31
        print(year, "年", month, "月份有", day, "天")
    elif month==2:
        day=28
        print(year, "年", month, "月份有", day, "天")
    elif month==3:
        day=31
        print(year, "年", month, "月份有", day, "天")
    elif month==4:
        day=30
        print(year, "年", month, "月份有", day, "天")
    elif month==5:
        day=31
        print(year, "年", month, "月份有", day, "天")
    elif month==6:
        day=30
        print(year, "年", month, "月份有", day, "天")
    elif month==7:
        day=31
        print(year, "年", month, "月份有", day, "天")
    elif month==8:
        day=31
        print(year, "年", month, "月份有", day, "天")
    elif month==9:
        day=30
        print(year, "年", month, "月份有", day, "天")
    elif month==10:
        day=31
        print(year, "年", month, "月份有", day, "天")
    elif month==11:
        day=30
        print(year, "年", month, "月份有", day, "天")
    elif month==12:
        day=31
    else:
        print("输入有问题....")               


"""
4.12 (检测一个数字) 编写一个程序提示用户输入一个整数,然后检测该数字是否能被5和6都整除\能被5或6整除还是只被它们中的一个整除(但又不能被它们同时整除)

num1 = eval(input("输入数字:"))
if num1 % 5 == 0 and num1 % 6 == 0:
    print("Is %d divisible by 5 and 6", True)
else:
    print("Is %d divisible by 5 and 6?", False)
    if num1 % 5 == 0 or num1 % 6 == 0:
        print("Is %d divisible by 5 or 6", True)
        print("Is %d divisible by 5 or 6", "but not both?", True)
"""

"""
4.13 (财务应用程序:计算税款) 程序清单4-7给出的源代码计算单身报税人的税款


status = eval(input("请输入报税人身份:(0.单身报税人1.已婚合并申报人2.已婚分开申报人3.户主)"))
income = eval(input("请输入纳税收入:"))
tax = ""
if status == 0:
    if income > 0 and income < 8350:
        tax = income * 0.1
    elif income > 8351 and income < 33950:
        tax = 8350 * 0.1 + (income - 8350) * 0.15
    elif income > 33951 and income < 82250:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (income - 82250) * 0.25
    elif income > 82251 and income < 171550:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income > 171551 and income < 372950:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (
                    income - 171550) * 0.33
    else:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (
                    372950 - 171550) * 0.33 + (income - 372950) * 0.35
elif status == 1:
    if income > 0 and income < 16700:
        tax = income * 0.1
    elif income > 16701 and income < 67900:
        tax = 16700 * 0.1 + (income - 16700) * 0.15
    elif income > 67901 and income < 137050:
        tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (income - 67900) * 0.25
    elif income > 137051 and income < 208850:
        tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (income - 137050) * 0.28
    elif income > 208851 and income < 372950:
        tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + (
                    income - 208850) * 0.33
    else:
        tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + (
                372950 - 208850) * 0.33 + (income - 372950) * 0.35
elif status == 2:
    if income > 0 and income < 8350:
        tax = income * 0.1
    elif income > 8351 and income < 33950:
        tax = 8350 * 0.1 + (income - 8350) * 0.15
    elif income > 33951 and income < 68525:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income > 68526 and income < 104425:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (income - 68525) * 0.28
    elif income > 104426 and income < 186475:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + (
                income - 104425) * 0.33
    else:
        tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + (
                186475 - 104425) * 0.33 + (income - 186475) * 0.35

elif status == 3:
    if income > 0 and income < 11950:
        tax = income * 0.1
    elif income > 11951 and income < 45500:
        tax = 11950 * 0.1 + (income - 11950) * 0.15
    elif income > 45501 and income < 117450:
        tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (income - 45500) * 0.25
    elif income > 117451 and income < 190200:
        tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (income - 117450) * 0.28
    elif income > 190201 and income < 372950:
        tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + (
                    income - 190200) * 0.33
    else:
        tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + (
                    372950 - 190200) * 0.33 + (income - 372950) * 0.35
else:
    print("输入错误....")
print(tax)
"""

"""
4.14 (游戏:头或尾) 编写程序让客户猜测一个弹起的硬币显示的正面还是反面,程序提示的用户输入一个猜测值,然后显示这个猜测值是正确的还是错误的

import random

is_romdom = random.randint(0, 1)
input_test = input("请猜测硬币的正方面:")
if input_test == is_romdom:
    print("猜对了")
elif is_romdom == 0:
    print("正面")
else:
    print("反面")
"""

"""
4.15 (游戏:彩票)改写程序清单4-10产生一个三位彩票数,程序提示用户输入一个三位整数,然后根据下面的规则判断用户是否赢得奖金:
    1)如果用户输入的数和彩票数字完全匹配,包括数字顺序,那么奖金就是10000美元
    2)如果用户输入的数匹配彩票中的所有数字,不包括顺序,那么奖金是3000美元
    3)如果用户输入的数中的一个数匹配彩票数字中的任意一个数,那么奖金是1000美元

import random

A = random.randint(100, 999)  # 彩票数
print(A)
B = eval(input("输入数:"))  # 用户输入数
A1 = A // 10
A11 = A1 // 10
A12 = A1 % 10
A2 = A % 10

B1 = B // 10
B11 = B1 // 10
B12 = B1 % 10
B2 = B % 10

if A == B:
    print(10000)
elif (A11 == B11 or A11 == B12 or A11 == B2) and (A12 == B11 or A12 == B12 or A12 == B2) and (
        A2 == B11 or A2 == B12 or A2 == B2):
    print(3000)
elif (A11 == B11 or A11 == B12 or A11 == B2) or (A12 == B11 or A12 == B12 or A12 == B2) or (
        A2 == B11 or A2 == B12 or A2 == B2):
    print(1000)
"""

"""
4.16 (随机字符) 编写程序显示一个随机大写字母

import random

uppercase = random.randint(65, 90)
print(chr(uppercase))
"""

"""
4.17 (游戏:剪刀\石头\布)编写程序来玩流行的剪刀-石头-布的游戏.(剪刀可以剪纸,石头可以磕碰剪刀,而布可以包裹石头),程序随机产生一个数字0,1或2来
表示剪刀\石头\布.程序提示用户输入数字0,1或2然后显示一条消息表示用户或计算机是赢,输,或者平局

# 0 代表剪刀 1 代表石头 2 代表布
import random
entity1 = ""
number = random.randint(0, 2)
print(number)
if number == 0:
    entity1 = "剪刀"
elif number == 1:
    entity1 = "石头"
else:
    entity1 = "布"
input_number = eval(input("输入数字:"))
entity2 = ""
if input_number == 0:
    entity2 = "剪刀"
elif input_number == 1:
    entity2 = "石头"
elif input_number == 2:
    entity2 = "布"

if number == input_number == 0:
    print("电脑出的是剪刀,你也是剪刀,所以平局")
if number == input_number == 1:
    print("电脑出的是石头,你也是石头,所以平局")
if number == input_number == 2:
    print("电脑出的是布,你也是布,所以平局")

if number == 0 and input_number == 1:
    print("电脑出的是%s,你出的是%s" % (entity1, entity2), "所以您赢了!")
if number == 1 and input_number == 2:
    print("电脑出的是%s,你出的是%s" % (entity1, entity2), "所以您赢了!")
if number == 2 and input_number == 0:
    print("电脑出的是%s,你出的是%s" % (entity1, entity2), "所以您赢了!")

if number == 1 and input_number == 0:
    print("电脑出的是%s,你出的是%s" % (entity1, entity2), "所以电脑赢了!")
if number == 2 and input_number == 1:
    print("电脑出的是%s,你出的是%s" % (entity1, entity2), "所以电脑赢了!")
if number == 0 and input_number == 2:
    print("电脑出的是%s,你出的是%s" % (entity1, entity2), "所以电脑赢了!")
"""

"""
4.18(金融问题:货币兑换)编写一个程序提示用户输入美元和人民币之间的货币汇率.提示用户输入0表示将美元转换为人民币而1表示将人民币转换为美元.
提示用户输入美元或人民币数将它分别转换为人民币或美元.

rate = eval(input("输入汇率(0.1421 人民币转换为美元的汇率,7.0389 #美元转换为人民币的汇率):"))
input_status = eval(input("输入类型(0:美元转换为人民币,1:人民币转换为美元):"))
# 0.1421 #人民币转换为美元的汇率
# 7.0389 #美元转换为人民币的汇率
if input_status == 0:
    amount = eval(input("请输入美元金额:"))
    result = amount * rate
    print(result)
elif input_status == 1:
    mount = eval(input("请输入人民币金额:"))
    result = 1000 * rate
    print(result)
else:
    print("输入错误!")
"""

"""
4.19(计算三角形周长)编写程序读取三角形的三个边,如果输入都是合法的则计算它的周长,否则,显示这个输入是非法的.如果两边之和大于第三边则输入
都是合法的.

a, b, c = eval(input("请输入三角形的三条边(a,b,c):"))
if a + b > c and a + c > b and c + b > a:
    perimeter = a + b + c
    print("三角形周长:", perimeter)
else:
    print("输入不合法!")
"""

"""
4.20(科学方面:风寒温度) 编程题2.9给出计算风寒温度的公式.这个公式适用于温度在-58摄氏度(华氏温度)和41摄氏度(华氏温度)之间且风速大于或
等于2编写程序提示用户输入一个温度值和风速.如果输入是合法的,程序就显示风寒的温度;否则,它显示一条消息表明这个温度或风速是非法的

temperature = eval(input("输入温度值:"))
wind_speed = eval(input("输入风速:"))
if temperature >= -58 and temperature <= 41:
    cold_temperature = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (
            0.4275 * temperature * (wind_speed ** 0.16))
    print("风寒的温度是:", format(cold_temperature, "4.2f"))

else:
    print("输入不合法....")
"""

"""
4.21 (科学问题:一周的星期几) 泽勒的一致性是一个有泽勒开发的算法,用于计算一周的星期几,这个公式如下:
h = (q + 26*(m+1)/10 + k +k/4 + j/4 +5j) % 7   #注意:公式中除法采用整除
1.这里的h是指一周的星期几(0:星期六,1:星期天,2:星期一,3:星期二,4:星期三,5:星期四,6:星期五)
2.q是一个月的哪一天
3.m是月份(3:三月,4:四月;.....12:十二月.一月和二月都是按照前一年的13月和14月来计数的
4.j是世纪数(即:year/100)
5.k是一个世纪的某一年(year%100)

编写一个程序提示用户输入一个年份\月份以及这个月的某天,然后它会显示它是一周的星期几.


# (0:星期六,1:星期天,2:星期一,3:星期二,4:星期三,5:星期四,6:星期五)
year = eval(input("year:"))
j = year / 100
k = year % 100
m = eval(input("month:"))
q = eval(input("day:"))
h = int((q + 26 * (m + 1) // 10 + k + k // 4 + j // 4 + 5 * j) % 7)
print(h)
xq = ""
if h == 0:
    xq = "星期六"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
if h == 1:
    xq = "星期天"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
if h == 2:
    xq = "星期一"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
if h == 3:
    xq = "星期二"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
if h == 4:
    xq = "星期三"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
if h == 5:
    xq = "星期四"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
if h == 6:
    xq = "星期五"
    print("你输入的是:%d年%d月%d日,%s" % (year, m, q, xq))
"""

"""
4.22 (几何问题:点在圆内吗?) 编写一个程序提示用户输入一个点(x,y),然后检测这个点是否在圆心为(0,0),半径为10的圆内
x1, y1 = eval(input("输入x1和y1的坐标:"))
radius = eval(input("输入半径:"))
import turtle

turtle.showturtle()
turtle.dot(10, "black")
turtle.penup()
turtle.goto(x1, y1 - radius)
turtle.pendown()
turtle.circle(radius)
x2, y2 = eval(input("输入x2和y2的坐标:"))
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(10, "black")
import math

d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
if d == radius:
    print("圆上")
elif d < radius:
    print("圆内")
else:
    print("圆外")
turtle.done()
"""

"""
4.23 (几何问题:点在矩形内吗?) 编写程序提示用户输入点(x,y),然后检测这个点是否在以(0,0)为中心,而宽为10高为
5的矩形内
import turtle

turtle.showturtle()
turtle.goto(200, 100)
turtle.goto(-200, 100)
turtle.goto(-200, -100)
turtle.goto(200, -100)
turtle.goto(200, 100)
x, y = eval(input("输入x和y的坐标:"))
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(10, "black")
x=abs(x) #利用abs函数把x转换为绝对值
y=abs(y) #利用abs函数把y转换为绝对值
if x<200 and y<100:
    print("矩形内")
elif x==200 and y<100:
     print("矩形宽高边上")
elif x<200 and y==100:
    print("矩形长边上")
else:
    print("矩形外!")
turtle.done()
"""

"""
4.24(游戏:选出一张牌)编写程序模拟从52张牌中选出一张.你的程序应该显示这张牌的大小(Ace,2,3,4,5,6,7,8,9,10,jack,
,Queen,King)和花色(梅花,红桃,方块,黑桃)

import random

num1 = random.randint(1, 4)
num2 = random.randint(1, 13)

colour = ""

if num1 == 1:
    colour = "红桃"
    if num2 == 1:
        print(colour, "Ace")
    elif num2 == 2:
        print(colour, "2")
    elif num2 == 3:
        print(colour, "3")
    elif num2 == 4:
        print(colour, "4")
    elif num2 == 5:
        print(colour, "5")
    elif num2 == 6:
        print(colour, "6")
    elif num2 == 7:
        print(colour, "7")
    elif num2 == "8":
        print(colour, "8")
    elif num2 == 9:
        print(colour, "9")
    elif num2 == 10:
        print(colour, "10")
    elif num2 == 11:
        print(colour, "J")
    elif num2 == 12:
        print(colour, "Q")
    elif num2 == 13:
        print(colour, "K")
elif num1 == 2:
    colour = "梅花"
    if num2 == 1:
        print(colour, "Ace")
    elif num2 == 2:
        print(colour, "2")
    elif num2 == 3:
        print(colour, "3")
    elif num2 == 4:
        print(colour, "4")
    elif num2 == 5:
        print(colour, "5")
    elif num2 == 6:
        print(colour, "6")
    elif num2 == 7:
        print(colour, "7")
    elif num2 == 8:
        print(colour, "8")
    elif num2 == 9:
        print(colour, "9")
    elif num2 == 10:
        print(colour, "10")
    elif num2 == 11:
        print(colour, "J")
    elif num2 == 12:
        print(colour, "Q")
    elif num2 == 13:
        print(colour, "K")
elif num1 == 3:
    colour = "黑桃"
    if num2 == 1:
        print(colour, "Ace")
    elif num2 == 2:
        print(colour, "2")
    elif num2 == 3:
        print(colour, "3")
    elif num2 == 4:
        print(colour, "4")
    elif num2 == 5:
        print(colour, "5")
    elif num2 == 6:
        print(colour, "6")
    elif num2 == 7:
        print(colour, "7")
    elif num2 == 8:
        print(colour, "8")
    elif num2 == 9:
        print(colour, "9")
    elif num2 == 10:
        print(colour, "10")
    elif num2 == 11:
        print(colour, "J")
    elif num2 == 12:
        print(colour, "Q")
    elif num2 == 13:
        print(colour, "K")
elif num1 == 4:
    colour = "方块"
    if num2 == 1:
        print(colour, "Ace")
    elif num2 == 2:
        print(colour, "2")
    elif num2 == 3:
        print(colour, "3")
    elif num2 == 4:
        print(colour, "4")
    elif num2 == 5:
        print(colour, "5")
    elif num2 == 6:
        print(colour, "6")
    elif num2 == 7:
        print(colour, "7")
    elif num2 == 8:
        print(colour, "8")
    elif num2 == 9:
        print(colour, "9")
    elif num2 == 10:
        print(colour, "10")
    elif num2 == 11:
        print(colour, "J")
    elif num2 == 12:
        print(colour, "Q")
    elif num2 == 13:
        print(colour, "K")
        
"""

"""
4.25(几何问题:交点)行1上的两个点是(x1, y1)和(x2, y2),而行2上的点是(x3, y3)和(x4, y4)
这两条线的交点可以通过解下面的线性等式找出:<这道题不会做>
(y1- y2)*x-(x1- x2)*y=(y1- y2)*x1-(x1- x2)*y1
(y3- y4)*x-(x3- x4)*y=(y3- y4)*x3-(x3- x4)*y3
"""

"""
4.26(回文数)编写程序提示用户输入一个三位整数,然后决定他是否是一个回文数.如果一个数从左向右和从右向左读取时
是一样的.那么这个数就是回文数.


num = eval(input("请输入:"))
num1 = num // 10
num2 = num1 // 10
num3 = num1 % 10
num4 = num % 10

if num < 100:
    print("输入不正确,请重新输入...")
elif num2 == num4:
    print("原始数字顺序:num2,num3,num4:", num2, num3, num4)
    print("是回文数:", num4, num3, num2)
else:
    print("不是回文数:", num4, num3, num2)
"""

"""
4.27(几何问题:点在三角形内吗?)假设一个直角三角形被放在一个水平面上,直角的点是在(0,0)而另外两个点在(200,0)和(0,100)处,编写程序提示用户输入一个
带x坐标和y坐标的点,然后决定这个点是否在三角形内


import turtle

turtle.showturtle()
turtle.goto(200, 0)
turtle.goto(0, 100)
turtle.goto(0, 0)
turtle.penup()
x2, y2 = eval(input("Enter a point's x- and y-coordinates:"))
a = -y2
b = x2
c = 100
d = 200
e = 0
f = 20000
num = a * d - b * c
x = (e * d - b * f) / num
y = (a * f - e * c) / num
turtle.goto(x, y)
turtle.pendown()
turtle.dot(10, "black")

if x > x2 or y > y2:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")

turtle.done()


"""

"""
4.28-4.32的几何题不理解,需要有时间再去做
"""

"""
4.33(十进制转十六进制)编写一个程序提示用户输入一个0到15之间的整数,然后显示它对应的十六进制数
#第一种写法:
num = eval(input("num:"))
if num >= 0 and num <= 9:
    print(num)
elif num == 10:
    print("A")
elif num == 11:
    print("B")
elif num == 12:
    print("C")
elif num == 13:
    print("D")
elif num == 14:
    print("E")
elif num == 15:
    print("F")
else:
    print("输入错误")
    


# 第二种写法:
num = eval(input("num:"))  # strip() 用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
if num >= 0 and num <= 9:
    print("num:", num)
elif num >= 10 and num <= 15:
    num = hex(num)  # 通过hex函数把十进制的数字转换成十六进制
    num = num[2:]  # 把十六进制开头的0x去掉
    num = num.upper()  # 在小写字母转换成大写字母
    print("num:", num)
else:
    print("输入错误!")
    
    
"""

"""
4.34(十六进制转十进制)编写一个程序提示用户输入一个十六进制的字符,然后显示它对应的十进制整数

str = input("string:")
if str == "A":
    print(10)
elif str == "B":
    print(11)
elif str == "C":
    print(12)
elif str == "D":
    print(13)
elif str == "E":
    print(14)
    
elif str == "F":
    print(15)
else:
    print("输入的字符字符不是十六进制")
"""

"""
用while循环画出嵌套正方形

num = 1
step = 50
lenght = 100
while num < 5:
    import turtle
    turtle.showturtle()
    turtle.goto(lenght, lenght)
    turtle.goto(-1 * lenght, lenght)
    turtle.goto(-1 * lenght, -1 * lenght)
    turtle.goto(lenght, -1 * lenght)
    turtle.goto(lenght, lenght)
    lenght = lenght + step
    num += 1
else:
    print("out", num)
turtle.done()

"""

"""
用while循环画出嵌套矩形

step = 50
lenght1, lenght2 = 200, 100
num = 1
while num < 5:
    import turtle

    turtle.showturtle()
    turtle.penup()
    turtle.goto(lenght1, lenght2)
    turtle.pendown()
    turtle.goto(-1 * lenght1, lenght2)
    turtle.goto(-1 * lenght1, -1 * lenght2)
    turtle.goto(lenght1, -1 * lenght2)
    turtle.goto(lenght1, lenght2)
    lenght1 = lenght1 + step
    lenght2 = lenght2 + step
    num += 1
turtle.done()

"""
