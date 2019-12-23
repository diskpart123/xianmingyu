"""
break 和 continue 双层使用
"""



"""
# break 案例使用
打印8行10列的数字表,记住规则:8行是放在外层的循环,10列是放在内层循环

for i in range(8):
    for j in range(10):
        print(j, end=" ")  #end="" 表示每一次的内部循环不换行
    print()


# 内循环每次打印到5就会停止

for i in range(8):
    for j in range(10):
        if j == 5:
            break  # 这里break表示每当内部循环j等于5时就停止内部循环
        print(j, end=" ")  # end="" 表示每一次的内部循环不换行
    print()


# break(双层) 外部循环每次打印到4就停止,同时内循环每次打印到5也会停止

for i in range(8):
    if i == 4:
        break  # 这里break表示每当外部循环i等于4时就停止外部循环
    for j in range(10):
        if j == 5:
            break  # 这里break表示每当内部循环j等于5时就停止内部循环
        print(j, end=" ")  # end="" 表示每一次的内部循环不换行

    print()
"""



"""
continue (双层)案例使用

for i in range(8):
    if i == 5:
        continue  # 这里continue表示每当外部循环i等于5时就跳过了外部的本次循环,继续下一个循环,本质上就是淘汰了5这一行
    print(i, end=" ")
    for j in range(10):
        if j == 4:
            continue # 这里continue表示本质上就是淘汰了4这一列
        print(j,end=" ")

    print()
"""