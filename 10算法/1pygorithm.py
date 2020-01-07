# encoding: utf-8
"""
@author: xianming yu
@contact: 626563967@qq.com
@time: 2020/1/7 16:15
@file: 1pygorithm.py
"""

"""
pygorithm：一个用纯粹python编写的Python模块，用于纯粹的教育目的。只需导入所需的算法即可获取代码，
时间复杂度等等。开始学习Python编程的好方法。了解Python中所有主要算法的实现。不需要上网就可以获得所需的代码。
"""
#安装
"""
pip3 install pygorithm
"""
#常见函数
"""
斐波那契数列
from pygorithm.fibonacci import recursion
result = recursion.get_sequence(10)
print(result)       # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

code = recursion.get_code()     # 获取实现函数的算法
print(code)     
"""
"""
获取最小公倍数
from pygorithm.math import lcm
result = lcm.lcm([4,6])
print(result)       # 12

code = lcm.get_code()           # 获取实现函数的算法
print(code)
"""

"""
质数算法
from pygorithm.math import sieve_of_eratosthenes
result = sieve_of_eratosthenes.sieve_of_eratosthenes(10)    # 获取小于10的质数
print(result)       # [2,3,5,7]

code = lcm.get_code()           # 获取实现函数的算法
print(code)
"""

"""
阶乘
from pygorithm.math import factorial
result = factorial.factorial(5)     # 获取5的阶乘，即1*2*3*4*5
print(result)       # 120

code = factorial.get_code()     # 获取实现函数的算法
print(code)
"""

"""
十进制转二进制
from pygorithm.math import conversion
result = conversion.decimal_to_binary(3)    # 将3转换为二进制
print(result)       # 11
"""

"""
十进制转十六进制

from pygorithm.math import conversion
result = conversion.decimal_to_hex(15)      # 将15转换为十六进制数
print(result)       # F
"""

"""
十六进制转十进制
from pygorithm.math import conversion
result = conversion.hex_to_decimal("F")     # 将十六进制F转化为十进制数
print(result)       # 15
"""

"""
二分法搜索：效率高
from pygorithm.searching import binary_search
a = [9,4,5,1,7]
index = binary_search.search(a,5)      # 获取5在列表中的位置，找到返回下标，找不到返回False
print(index)

code = binary_search.get_code()  # 获取实现函数的算法
print(code)
"""

"""
线性搜索：速度慢，适用性广
from pygorithm.searching import linear_search
l = [9,4,5,1,7]
index = linear_search.search(l,5)       # 获取5在列表中的位置，找到返回下标，找不到返回False
print(index)

code = linear_search.get_code() # 获取实现函数的算法
print(code)
"""

"""
插值搜索：注意：列表必须先经过升序排序，否则将找不到
from pygorithm.searching import interpolation_search
l = [1,4,5,7,9]
index = interpolation_search.search(l,4)    # 获取5在列表中的位置，找到返回下标，找不到返回False
print(index)

code = interpolation.get_code() # 获取实现函数的算法
print(code)
"""

""""
冒泡排序
from pygorithm.sorting import bubble_sort
l = [9,4,5,1,7]
result = bubble_sort.sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = bubble_sort.get_code()   # 获取实现函数的算法
print(code)
"""

"""
改良冒泡排序
from pygorithm.sorting import bubble_sort
l = [9,4,5,1,7]
result = bubble_sort.improved_sort(l)
print(result)       # [1, 4, 5, 7, 9]
"""

"""
桶排序
from pygorithm.sorting import bucket_sort
l = [9,4,5,1,7]
result = bucket_sort.sort(l,5)  # 5为桶的大小，默认为5
print(result)       # [1, 4, 5, 7, 9]

code = bucket_sort.get_code()   # 获取实现函数的算法
print(code)
"""

"""
计数排序
from pygorithm.sorting import counting_sort
l = [9,4,5,1,7]
result = counting_sort.sort(l)  
print(result)       # [1, 4, 5, 7, 9]

code = counting_sort.get_code() # 获取实现函数的算法
print(code)
"""

"""
计数排序
from pygorithm.sorting import counting_sort
l = [9,4,5,1,7]
result = counting_sort.sort(l)  
print(result)       # [1, 4, 5, 7, 9]

code = counting_sort.get_code() # 获取实现函数的算法
print(code)
"""

"""
堆排序
from pygorithm.sorting import heap_sort
l = [9,4,5,1,7]
result = heap_sort.sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = heap_sort.get_code()     # 获取实现函数的算法
print(code)
"""

"""
插入排序
from pygorithm.sorting import insertion_sort
l = [9,4,5,1,7]
result = insertion_sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = insertion_sort.get_code()    # 获取实现函数的算法
print(code)
"""

"""
归并排序
from pygorithm.sorting import merge_sort
l = [9,4,5,1,7]
result = merge_sort.sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = merge_sort.get_code()        # 获取实现函数的算法
print(code)
"""

"""
快速排序
from pygorithm.sorting import quick_sort
l = [9,4,5,1,7]
result = quick_sort.sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = quick_sort.get_code()        # 获取实现函数的算法
print(code)
"""

"""
选择排序
from pygorithm.sorting import selection_sort
l = [9,4,5,1,7]
result = selection_sort.sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = selection_sort.get_code()    # 获取实现函数的算法
print(code)
"""

"""
希尔排序
from pygorithm.sorting import shell_sort
l = [9,4,5,1,7]
result = shell_sort.sort(l)
print(result)       # [1, 4, 5, 7, 9]

code = shell_sort.get_code()        # 获取实现函数的算法
print(code)
"""


