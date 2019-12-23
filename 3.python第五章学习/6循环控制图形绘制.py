# 利用while循环绘制矩形
import turtle
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("x1,y1,x2,y2,x3,y3,x4,y4:"))
count = 0
turtle.showturtle()
turtle.dot(10, "black")
while count < 4:
    count += 1
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2 * -1, y2)
    turtle.goto(x3 * -1, y3 * -1)
    turtle.goto(x4, y4 * -1)
    turtle.goto(x1, y1)
    x1 += 50
    y1 += 50
    x2 += 50
    y2 += 50
    x3 += 50
    y3 += 50
    x4 += 50
    y4 += 50
turtle.done()
