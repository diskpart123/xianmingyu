"""
逻辑运算符:and
"""
"""
这里有一个案例:例如相亲网站要求相亲的条件是:
升高:177cm
颜值:90
存款:1000000
有一个人来相亲,此时需要比对这三项条件是否符合,我们用逻辑运算符and来实现
"""
rise1 = 177
score1 = 97
deposit1 = 1000000

rise = eval(input("输入升高:"))
score = eval(input("输入颜值:"))
deposit = eval(input("输入存款:"))

condition1 = (rise >= rise1)
condition2 = (score >= score1)
condition3 = (deposit >= deposit1)
print(condition1, condition2, condition3)

if (condition1 and condition2 and condition3):  #and逻辑运算符三个条件必须都为True,少一个都不行
    print("三项条件都符合,您过关了!恭喜")
else:
    print("您的条件不符合....")
