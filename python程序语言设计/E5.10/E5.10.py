#data = input("Ente an integer (the input ends" + "if it is 0): \n")
#data = eval(data)
#sum = 0
#while data != 0:
#    sum += data
#    data = eval(input("Ente an integer (the input ends" + "if it is 0): \n"))

#print("The sum is",sum)
num = eval(input("请输入学生个数：\n"))
score = eval(input("请输入学生分数：\n"))
t = 0

while score != 0:
    if t < score:
        t = score
    else:
        pass
    score = eval(input("请输入学生分数：\n"))

print("最高分是:",t)
