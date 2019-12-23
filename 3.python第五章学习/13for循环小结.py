"""
注意点:任何for循环都可以转换成while循环,但不是所有的while循环都可以转换成for循环
for 不能做的:不能处理死循环,不能处理实数(浮点数)
"""

"""
for 恰好即将跳出循环

for i in range(100): #for循环只适用整数
    print(i)
else:
    print(i)       #99恰好即将跳出循环
"""

"""
while 恰好跳出循环
count = 0
while count < 100:
    count += 1
    print(count)
else:
    print("ceshi:", count)  # 100恰好跳出循环
"""