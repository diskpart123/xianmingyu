# 求圆形的面积

R = input("请输入圆形的半径>:")

print(type(R))  # 查看R的数据类型,这个R字符串类型，需要把它转换成实数

R = eval(R)  # 字符串转化为实数
print(type(R))

Area = R * R * 3.1415926535
print("圆的面积是:>", Area)  # 得到结果：圆的面积是:> 314.15926535

# 检查点：
"""
显示下面的代码的打印输出
"""
width = 5.5
height = 2
print("area is", width * height)

"""
将下面的算法翻译成Python代码
第一步：使用一个名为miles初始值为100的变量
第二步：将miles乘以1.609并将它赋值给一个名为：kilometers的变量
第三步：显示kilometers的值
请  问：第三步之后kilometers是多少？
"""
miles = 100
kilometers = miles * 1.609
print(kilometers)
