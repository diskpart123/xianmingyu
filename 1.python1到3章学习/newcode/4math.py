# 我们是不可能把所有的函数记住的，我们只需要记住如何来查询函数的使用方法即可

import math  # 导入数学包

"""
print(abs(-5))  # abs函数是求绝对值
print(max(1, 20, 10, 30, 20))  # 返回最大值
print(min(1, 20, 10, 30, 20))  # 返回最小值
print(pow(2, 4))  # 2的4次方=2*2*2*2
print(math.sqrt(9))  # 9的平方根
print(math.sin(3))  # 返回3弧度的正弦值(也称之为:三角函数)
"""

""" 
# 查询数学包里面的所有函数
print(dir(math))

#返回结果
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp',
 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt',
 'tan', 'tanh', 'tau', 'trunc']
"""
# 查询函数的用法
print(help(max))  # max输入全局函数,所以在查询用法的时候不需要引用math
print(help(math.sqrt))  # 如果是math数学包中的函数,在查询函数的用法的时候是需要引用math的
print(help(math.acosh))
