# 数字转换成字符串
num = 3
print(type(num))  # 得到结果：int类型

num = str(num)  # 把num的int类型转换成str类型
print(type(num))

# 把一个实数转换成整数
num = 4.5
num = int(num)  # 把4.5这个数字转换成4，记住：int用来取整数
print(type(num))

# 把一个字符串转换成数字

num = "4.5"
num = eval(num)
print(type(num))
