
bt1 = "ab备胎"
bt2 = "ac备胎"
bt3 = "aa备胎"

print(ord("a"))  # a在ASCLL码中的十进制的排序为97
print(ord("b"))  # b在ASCLL码中的十进制的排序为98
print(ord("c"))  # c在ASCLL码中的十进制的排序为99

"""
字符串也可以比较大小,主要用于文件的排序,其中排序的顺序是
按照ASCLL排序,如果第一个相等,就对比第二个,第二个相等对比
第三个,以此类推,注意Windows系统中的文件排序是不区分字母的
大小写,而在python中同一个字符比较大小是区分大小写的,比喻
小写的a和大写的A在ASCLL码中排序是不一样的
"""
print(bt1 > bt2)  # False
print(bt1 < bt2)  # True
print(bt1 > bt3)  # True
print(bt3 > bt1)  # False

print(bt1 != bt2)  # True  #判断字符不等,"不等"经常会用到输入的密码是否正确
print(bt1 == bt2)  # False #判断字符相等
