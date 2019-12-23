"""
#把bool类型转换成数值
print(int(True)) #得到结果:1
print(int(False)) #得到结果:0
"""

"""
#把数值转换成bool
print(bool(1))  # 得到结果:True
print(bool(0))  # 得到结果:False
print(bool(-1))  # 得到结果:True
"""

"""
#把字符或者字符串转换成bool
print(bool("a")) #得到结果:True
print(bool("ab"))#得到结果:True
"""

"""
#把None值转换成bool
print(bool(None)) #得到结果:False
"""

"""
#把""(空字符串)转换成bool

print(bool(""))  # 得到结果:False
"""

if " " : #if语句在执行的时候自动转换为bool类型
    print("xxx")

# 总结:在python中除了""(空字符串)和None和0转换成bool得到的结果是False,其他均为True

