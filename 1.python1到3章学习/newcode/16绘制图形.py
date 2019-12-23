import turtle

turtle.screensize(1024, 768)  # 显示窗口的大小
turtle.write("hello天朝", font=("华文琥珀", 20, "normal"))  # 设定字体大小,其中normal代表普通字体
turtle.showturtle

turtle.pensize(5)  # 画笔变粗
turtle.begin_fill()  # 开始填充颜色
turtle.circle(100, steps=5)  # 画一个边长为100的三角形,其中steps=3代表是三条边,如果steps=4就代表是四角形
turtle.color("blue")  # 填充颜色为蓝色
turtle.end_fill()  # 结束颜色填充
turtle.hideturtle()  # 隐藏箭头

turtle.reset()  # 重置掉上一个画面，开始画下一个画面

turtle.pensize(10)  # 画笔变粗
turtle.begin_fill()
turtle.circle(100, steps=4)
turtle.color("yellow")
turtle.end_fill()
turtle.hideturtle()  # 隐藏箭头

turtle.done()
