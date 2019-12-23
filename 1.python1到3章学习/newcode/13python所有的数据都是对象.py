# 在python中,所有的数据(包括数字和字符串)实际都是对象
"""
类:什么是类？这里简单来举例来说人类就是"类"
对象:喻先明就是人类实例化的对象
方法:比喻说喻先明这个对象,他可以吃饭,那么吃饭就是一个方法,也可以喝水,那么喝水也是一个方法

print("abc".upper())  #这里的"abc"就是str类型的对象,upper就是"abc"对象的方法,通过upper把"abc"全部转换成大写字母
print("abc".find("a")) #find也是"abc"对象的方法
"""

"""
当程序执行的时候,python会自动为对象的id赋一个独特的整数,在程序的执行过程当中,对象的id不会改变,然而,每当
执行程序时,python都可能会赋一个不同的id,python按照对象的值决定对象的类型

n1="abc"
print(id(n1)) #每当执行程序时,python都可能会赋一个不同的id,本质都是地址赋值
"""

# 检查点
"""
什么是类?什么是对象?什么是方法？
答:str是一个字符串类型(类型等价类),而"abc"是str类的对象,upper是"abc"对象的方法
"""

"""
如何找到一个对象的id?如何找到一个对象的类型?
a=123
print(id(a)) #查找对象的id
print(type(a)) # 查找对象的类型
"""

"""
下面哪种陈述是语句"n=3",最准确的含义?
1.n是一个拥有整型值3的变量
2.n是一个对象的引用,该对象的值为整数3   答案:2最准确
"""

"""
假如s是"\tGeorgia\n",那么s.lower()和s.upper()是什么?
s = "\tGeorgia\n"
print(s.lower()) #输入结果:   georgia
print(s.upper()) #输入结果:   GEORGIA
"""

"""
假如s是"\tGood\tMorning\n"
s = "\tGood\tMorning\n"
print(s.strip()) #输入结果:Good	Morning strip()方法是去除两边的空格
"""
