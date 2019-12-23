
#range()的参数必须为整数,不能为实数(浮点数)
#range(min,max,step) #参数 例如:range(1,100,2) #不包含max,当min<max循环下去,否则不会循环
#range(max,min,step) #参数 例如:range(100,2,-2) #不包含min,当max>min循环下去,否则不会循环


#for i in range(100) #输出100次,从0到99
#for i in range(2,100,2) #2到100每次步长为2


"""
在将for循环之前,我们先来做一个案例,怎么用while循环输出1到100之间的数字

count = 1
while count < 100:
    print(count)
    count += 1
"""

"""
那么如果用for循环来输出1到100之间的数字的数字该怎么实现呢
for i in range(0, 100): #1<=i<100
    print(i)
"""

"""
怎么输出1到100偶数数字
第一种方法:

for i in range(1, 100):
    if i%2==0:
        print(i)

#第二种方法
for i in range(2,100,2): #最后一个2是步长
    print(i)
"""

"""
怎么输出1到100之间的奇数
第一种方法
for i in range(1,100):
    if i%2!=0:
        print(i)

第二种方法

for i in range(1,100,2):
    print(i)
"""

"""
怎么输出100到1之间的数字,也就是从大到小

for i in range(100,0,-1):
    print(i)
"""