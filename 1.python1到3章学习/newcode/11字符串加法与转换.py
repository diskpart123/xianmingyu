import os

"""
# str1 = "note"
# str2 = "pad"
# os.system(str1 + str2) #也可以用字符串相加的方式打开系统的记事本(字符串加法)
"""


"""
案例:假如桌面上有三个文本文件分别是:1.txt,2.txt,3.txt,怎么一次性打开三个文件,
这里我们就可以用到字符串拼接的放法来做到,但程序运行时打开了第一个文件,需要手动的
方式把第一个文件关闭掉第二个文件才会自动打开

count = 1
for i in range(0, 3):
    str3 = "C:\\Users\\Administrator\\Desktop\\" + str(count) + ".txt"
    os.system(str3)
    count = count + 1
"""

