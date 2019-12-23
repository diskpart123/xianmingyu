# 检查点

# 4.1 列举六种比较运算符
# 答案:>\>=\<\<=\==\!=

# 4.2 下面的转换是允许的吗?如果允许,如果允许,给出转换后的结果
"""
i=int(True) #i=1
j=int(False) #j=0
b1=bool(4) #b1=True
b2=bool(0) #b2=False
print(i,j,b1,b2) #输出结果:1 0 True False
"""

# 4.3 怎样生成一个满足条件0<=i<20  #random.randrange(0,20)
# 4.4 怎样生成一个 满足条件10<=i<20  #random.randrange(10,20)
# 4.5 怎样生成一个满足条件10<=i<=50  #random.randint(10,50)
# 4.6 怎样生成一个值为0或者1的随机整数? #random.randint(0,1)

"""
#4.7 编写一条如果y大于零,将1赋值给x的if语句
if y>0:
    x=1
"""

"""
#4.8 编写一个如果score大于90,pay增长3%的if语句
if score>90:
    pay*(1+3%)
"""

"""
#4.9 编写一个如果score大于90,pay上涨3%,否则上涨1%的if语句
if score>90:
    pay*(1+3%)
else:
    pay*(1+1%)
"""

# 4.10 如果number分别是30和35,那么a中的代码和b中的代码的输出结果是什么?
"""
#a实例
if number%2==0:
    print(number,"is even")
print(number,"is odd")

# 如果a实例的number等于30,那么上面输出的结果如下:

# 30,is even
#30,is odd

# 如果a实例的number等于35,那么上面输出的结果如下:

#35,is odd


#b实例
number=30
if number%2==0:
    print(number,"is even")
else
    print(number,"is odd")

# b实例的代码不管number是什么都不会输入结果,因为else代码块中少了冒号

"""

"""
4.11 如果是下面的代码中,假设x=3而且y=2,显示它的结果.如果x=3而且y=4,那么结果是什么？如果x=2而且y=2，那么
结果是什么,(首先正确缩进语句)
#如果x=3,y=2
x,y=3,2
if x>2:
    if y>2:
        z=x+y
        print("z is ",z)
    else:
        print("x is ",x)  #输出结果:3


#如果x=3,y=4
x,y=3,4
if x>2:
    if y>2:
        z=x+y
        print("z is ",z) #输出结果:7
    else:
        print("x is ",x)


#如果x=2,y=2
x,y=2,2   #输出结果:不输出任何结果
if x>2:
    if y>2:
        z=x+y
        print("z is ",z) 
    else:
        print("x is ",x)        
"""

"""
4.12 如果下面的代码,假设x=2而且y=4，显示它的结果.如果x=3而且y=2,那么结果是什么?如果x=3而且y=3,
那么结果是什么?(首先正确缩进语句。)

#如果x=2,y=4  
x,y=2,4
if x>2:
    if y>2:
        z=x+y                                                       
        print("z is",z)
else:
    print("x is ",x) #输出结果:x is  2

#如果x=3,y=2
x,y =3,2  #输出结果:不输出任何结果
if x>2:
    if y>2:
        z=x+y
        print("z is",z)
else:
    print("x is ",x) 


#如果x=3,y=3  
x,y =3,3  
if x>2:
    if y>2:
        z=x+y
        print("z is",z) #输出结果:z is 6
else:
    print("x is ",x)
"""

"""
#4.13 下面的代码错在哪里？
下面的代码如果score输入的结果只要大于60结果都是grade="D",这个逻辑就错了
score=eval(input("输入分数:"))

if score>=60.0:
    grade="D"
elif score>=70.0:
    grade="C"
elif score>=80.0:
    grade="B"
elif score>=90.0:
    grade="A"
else:
    grade="F"
print(grade)

# 下面是修改后的代码
score = eval(input("输入分数:"))
if score >= 90.0:
    grade = "A"
elif score >= 80.0:
    grade = "B"
elif score >= 70.0:
    grade = "C"
elif score >= 60.0:
    grade = "D"
else:
    grade = "F"
print(grade)

"""

"""
#4.14 下面的代码那些是等价的?那些是正确缩进?
#a实例
if i>0:
    x=0
    y=1
else:
    y=0
    z=0
#在a实例当中代码都是正确缩进的,但不是等价的

#b实例
if i>0:
    x=0
  y=1
else:
    y=0
    z=0
#在b实例当中,y=1代码的缩进不正确

#c实例
if i>0:
    x=0
    y=1
else:
    y=0
    z=0
#在c实例当中,代码的缩进都是正确的,但不是等价

#d实例
if i>0:
    x=0
    y=1
else:
    y=0
  z=0
#在d实例当中,z=0代码的缩进不正确

"""

"""
# 4.15 使用一个布尔表达式改写下面的语句 (暂时没有想出方法)
count=15
if count%10==0:
    newLine=True
else:
    newLine=False


# 改写后代码如下:
count = 15
if bool(count % 10):
    newLine = True
    print(newLine)
else:
    newLine = False
    print("xxx")

"""


"""
# 4.16 下面的语句正确吗?那个更好

#a实例
if age<16:
    print("Cannot get a driver's license")
if age>=16:
    print("Can get a driver's license")


#b实例
if age<16:
    print("Cannot get a driver's license")
else:
    print("Can get a driver's license")

#在a和b的实例当中,代码都是正确的,其中a实例代码是等价的,b实例的代码是不等价的,更安全,效果更好
"""

"""
#4.17 如果number分别是14,15和30那么下面的代码的结果是什么?
#a实例

if number%2==0:
    print(number,"is even")
if number%5==0:
    print(number,"is multiple of 5")
#如果number=14 输出结果:14 is even
#如果number=15 输出结果:15 is multiple of 5
#如果number=30 输出结果:30 is even 和 30 is multiple of 5



#b实例
if number%2==0:
    print(number,"is even")
elif number%5==0:
    print(number,"is multiple of 5")

#如果number=14 输出结果:14 is even
#如果number=15 输出结果:15 is multiple of 5
#如果number=30 输出结果:30 is even

"""