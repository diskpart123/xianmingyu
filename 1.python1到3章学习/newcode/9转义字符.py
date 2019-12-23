"""
import os

os.system("D:\Sublime Text 3\sublime_text.exe")  # 这里的打开会报错的,因为中间用空格

os.system("\"D:\Sublime Text 3\sublime_text.exe\"")  # 加入转义字符就会解决空格的问题,可以正常打开
"""

"""
# 案例1:在hello后面加入双引号
print("hello\"")

# 案例2:在hello后面加入双引号,在加入一个单引号
print("hello\"\'")

# 案例3:在hello中间换行
print("he\nllo")

"""