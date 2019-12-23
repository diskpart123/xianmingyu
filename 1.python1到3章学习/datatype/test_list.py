"""

# 提示用户输入一个十进制带小数点的数字:例如:11.56
amount = eval(input("输入是十进制带小数点数字:"))

# 将钱数(11.56)转换成分数
score = int(amount * 100)

# 将分数除以100得到美元的个数,使用分数%100得到余数即时剩余的分数
meiyuan_geshu = score // 100  # 美元个数
score = score % 100  # 剩余分数
# 将剩余的分数除以25得到两角五分硬币的个数。使用分数%25得到余数即是剩余的分数
liangjiaowufen_geshu = score // 25  #两角五分硬币的个数
score=score%25

# 将剩余的分数除以10得到一角硬币的个数。使用分数%10得到余数即是剩余的分数
yijiaoyingbi_geshu=score//10
score=score%10

# 将剩余的分数除以5得到五分硬币的个数。使用分数%5得到余数即是剩余的分数
wufenyingbi_geshu=score//5
score=score%5
# 剩余的分数就是一美分硬币个数
yimeifen_geshu=score


# 显示结果
print("\t","美元个数:",meiyuan_geshu,"\n",
      "\t","两角五分硬币的个数:",liangjiaowufen_geshu,"\n",
      "\t","一角硬币的个数:",yijiaoyingbi_geshu,"\n",
      "\t","五分硬币的个数:",wufenyingbi_geshu,"\n",
      "\t","一美分硬币个数:",yimeifen_geshu,"\n")
"""


import  turtle
turtle.showturtle()
turtle.begin_fill()
turtle.circle(100,steps=4)
turtle.penup()
turtle.goto(0,5)
turtle.pendown()
turtle.pencolor("blue")
turtle.write("niha",font=("Gungsuh",20))
turtle.color("red")
turtle.end_fill()
turtle.done()



