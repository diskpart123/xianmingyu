num = eval(input("请输入学生个数：\n"))
score = eval(input("请输入学生分数：\n"))
t = 0
a = 1

while num != 1:
    if t < score:
        b = t
        t = score
        score = b
    else:
        pass
    if a < t:
        pass
    else:
        a = t
    if a > score:
        pass
    else:
        a = score
    score = eval(input("请输入学生分数：\n"))
    num -= 1

print("最高分是:",t)
print("次高分是:",a)
