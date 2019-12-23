import turtle

"""
turtle.showturtle()  # 显示画图界面的箭头方向
turtle.write("welcome to python")  # 在箭头的位置输入一个文本字符串
turtle.forward(100)  # 将箭头向前移动100像素
turtle.right(90)  # 将箭头向右90度
turtle.color("red")  # 将箭头颜色设置为红色
turtle.forward(50)  # 将箭头向前移动50像素
turtle.right(90)  # 将箭头向右90度
turtle.forward(100)  # 将箭头向前移动100像素
turtle.right(45)  # 将箭头向右45度
turtle.forward(80)  # 将箭头向前移动80像素

turtle.done()

"""

"""
turtle.goto(0, 50)  # 将笔从0,0移动到0,50的位置上
turtle.penup()  # 将笔抬起
turtle.goto(50, -50)  # 将笔移动到50(x),-50(y)位置上
turtle.pendown()  # 将笔落下
turtle.color("red")  # 设置箭头的颜色为红色
turtle.circle(100)  # 使用circle命令画一个半径为50的圆
turtle.done()

"""

"""
# 画奥运五环

turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(0, -25)
turtle.down()
turtle.color("black")
turtle.circle(45)

turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.color("red")
turtle.circle(45)

turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.color("yellow")
turtle.circle(45)

turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.color("green")
turtle.circle(45)
turtle.done()


"""

"""
# 画三角形
turtle.showturtle()
turtle.right(90)

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.color("blue")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(135)
turtle.forward(141)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

turtle.done()

"""

"""
# 绘制奥运环

turtle.showturtle()
turtle.color("blue")
turtle.circle(45)
turtle.penup()
turtle.goto(120, 0)
turtle.color("black")
turtle.pendown()
turtle.circle(45)
turtle.penup()
turtle.goto(240, 0)
turtle.color("red")
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(60, -50)
turtle.pendown()
turtle.color("black")
turtle.circle(45)

turtle.penup()
turtle.goto(180, -50)
turtle.pendown()
turtle.color("violet")
turtle.circle(45)
turtle.done()
"""


"""
奥运五环
import turtle
turtle.color("blue")  #改变箭头颜色为"蓝色"
turtle.circle(100)    #在原点画一个半径100的圆


turtle.penup()       #把笔抬起
turtle.goto(-200,0)  #把箭头往左移到-200的位置上
turtle.pendown()     #把笔放下
turtle.color("red") #改变箭头颜色为"红色"
turtle.circle(100)  #在原点画一个半径100的圆



turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.color("yellow")   #改变箭头颜色为"黄色"
turtle.circle(100)


turtle.penup()
turtle.goto(100,-200)
turtle.pendown()
turtle.color("black")   #改变箭头颜色为"黑色"
turtle.circle(100)


turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.color("green")   #改变箭头颜色为"绿色"
turtle.circle(100)

turtle.done()         #让程序继续运行
"""


"""

# 绘制五角星
turtle.showturtle()
turtle.forward(200)
turtle.right(180)
turtle.penup()
turtle.goto(100, 0)
turtle.left(90)
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.right(180)
# turtle.forward(200)
turtle.penup()
turtle.goto(0, 0)
turtle.right(135)
turtle.pendown()
turtle.forward(230)
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(230)
turtle.right(148.5)
turtle.forward(274)
turtle.right(153.5)
turtle.forward(274.3)
turtle.penup()
turtle.goto(290, 290)
turtle.pendown()
turtle.done()
"""

"""
#绘制立方图
turtle.showturtle()
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.left(45)
turtle.forward(143)
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.right(180)
turtle.forward(143)
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.forward(143)
turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.forward(143)
turtle.penup()
turtle.goto(0,230)
turtle.pendown()
turtle.done()

"""

"""
#绘制五星红旗

turtle.setup(1200, 800, 0, 0)
turtle.bgcolor("red")      # 背景颜色
turtle.color('yellow')     # 五角星颜色
turtle.speed(10)           # 设置画笔绘制速度
# 绘制最大的主五角星
turtle.begin_fill()        # 填充绘制的五角星
turtle.up()                # 抬笔不绘制
turtle.goto(-520, 240)     # 画笔设置到起始位置
turtle.down()              # 落笔进行绘制
for i in range(5):         # 循环5次
    turtle.forward(240)      # 向前移动150
    turtle.right(144)      # 以角度单位向右转动
turtle.end_fill()          # 结束填充
# 绘制第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-230,345)
turtle.setheading(305)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.left(144)
turtle.end_fill()

# 绘制第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-150,230)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()

# 绘制第3颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-155,130)
turtle.setheading(0)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()

# 绘制第4颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-230,68)
turtle.setheading(300)
turtle.down()
for i in range (5):
    turtle.forward(70)
    turtle.left(144)
turtle.end_fill()
turtle.hideturtle()  # 隐藏箭头
turtle.done()        # 开始循环防止窗口自动关闭

"""

