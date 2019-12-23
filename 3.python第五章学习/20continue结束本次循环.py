
#查找数字
"""
num=eval(input("输入数字:"))
for i in range(1000):
    if num==i:
        print("Find")
        continue   #结束本次循环,继续下个循环
    print(i)
"""

"""
continue 主要筛选数据,请看下面示例:通过continue函数把奇数筛选并打印出来

for i in range(100):
    if i%2==0:
        continue
    print(i) 
"""


"""
continue 主要筛选数据,请看下面示例:通过continue函数把偶数筛选并打印出来

for i in range(100):
    if i%2==1:
        continue
    print(i)
"""