import os, time
wenben="谊品大仓异常日志查询"
print(wenben.center(50,"*"))
str1 = ""
wenjian = input("输入日志路径:")
path = os.listdir(wenjian)
txt_input = input("输入要查找的日志名称:")
for i in path:
    if txt_input in i:
        path = wenjian + "\\" + i
file = open(path, encoding="utf-8")
file_lines = file.readlines()
for i in file_lines:
    str1 = str1 + str(i)
test = input("请输入搜索关键字:")
if test in str1:
    a = str1[str1.index(test) - 292:str1.index(test) + 1690]
    print(a)
else:
    print("未找到关键字", test)
time.sleep(100)
file.close()