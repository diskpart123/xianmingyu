"""
使用ord函数找出1、A、B、a和b的ASII码，

print(ord("1")) #输出结果:49
print(ord("A")) #输出结果:65
print(ord("B")) #输出结果:66
print(ord("a")) #输出结果:97
"""

"""
使用 chr函数找出十进制数40,59,79,85和90所对应的字符

print(chr(40)) #输出结果:(
print(chr(59)) #输出结果:;
print(chr(79)) #输出结果:O
print(chr(85)) #输出结果:U
print(chr(90)) #输出结果:Z
"""

"""
如何显示字符\和"

print("\\")  # 输出结果:\
print("\"")  # 输出结果:"
"""

"""
如何用统一码编写一个字符,这里用"我"来做示例

str1 = "我"
print(ord(str1))  # 用ord函数取得字符编码后,再将字符编码的十进制转换成十六进制
print("\u6211")
"""

"""
假如运行下面程序的时候输入A,那么输出是什么?

x=input("Enter a character:")
ch=chr(ord(x)+3)
print(ch)   #输出结果:D

"""

"""
假如运行下面的程序的时候输入A和Z,那么输入什么?

x = input("Enter  a character:")
print(ord(x))  # 65
y = input("Enter  a character:")
print(ord(y))  # 90
print(ord(y) - ord(x))  # 输出结果:25
"""

"""
这个代码错在哪里:title="Chapter"+1

应改成:title="Chapter"+str(1)

"""

"""
显示下面代码的结果:
sum = 2 + 3
print(sum)  # 输出结果:5
s = "2" + "3"
print(s)  # 输出结果:23
"""