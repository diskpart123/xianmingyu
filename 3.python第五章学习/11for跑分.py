
"""
总结:用for循环比while循环效率更高
"""

"""
场景:比喻测试电脑的性能,让电脑跑一下数字1到100000000需要用多长时间

import time
starttime = time.time()  # 开始时间

lastnum=0
count=0
while count<100000000:
    count += 1
    lastnum+=count
print(lastnum)
endtime = time.time()  # 结束时间
print(endtime-starttime) #时间差  #13.137591361999512
"""



"""
下面我们用for循环来改写跑分程序
"""
import time
starttime =time.time()  #开始时间
lastnum=0
for i in range(1,300000000):
    lastnum+=i
print(lastnum)
endtime = time.time()  #结束时间
print(endtime-starttime) #时差