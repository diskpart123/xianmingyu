# 竖向画图

import turtle

"""
for x in range(0,300,100):   
    for y in range(0,400,100):
       turtle.goto(x,y)    #i的结果是控制列(也就是最多显示3列,因为0,300,步长是100,返回的次数是3次,所以说是3列)
       turtle.write(str(x)+","+str(y))
turtle.done()


#横向画图
for i in range(0,300,100):
    for j in range(0,400,100):
       turtle.goto(j,i)  # 把i和j的顺序调整一下就是横向画图
       turtle.write(str(i)+","+str(j)) #i的结果是控制行(也就是最多显示3行,因为0,300,步长是100,返回的次数是3次,所以说是3行)
turtle.done()

"""

# 画横线去掉中间的连接线
for i in range(0, 300, 40):
    for j in range(0, 400, 100):
        turtle.goto(j, i)
        turtle.pendown()
        turtle.write(str(j) + "," + str(i))
    turtle.penup()
turtle.done()




