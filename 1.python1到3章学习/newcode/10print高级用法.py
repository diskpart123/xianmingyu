"""
print("a")
print("a")
print("a")
#上面的打印会输出三行,那如果不想换行,就需要在后面加上end=',',默认end是\n换行
print("a",end=',')
print("a",end=',')
print("a")

"""

print(1,2,3)
#上面的1,2,3中间我想输出的时候加个横线("-")分割,可以用sep来实现
print(1,2,3,sep="-")

