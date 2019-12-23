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