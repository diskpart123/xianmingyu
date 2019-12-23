"""
# 大小写字符转换
ch1 = "A"  # 这里需要把大写的A转换成小写a
ch1 = (chr(ord(ch1) + 32))
print(ch1)
"""

"""
# 字符串加密

ch2 = "python"
ch3 = ""
ch4 = ""
for i in ch2:
    ch3 = chr(ord(i) - 1)  # 把循环得到的字符编码减1
    ch4 = ch4 + ch3
print(ch4)

"""