# -*- coding: utf-8 -*-
# @Time    : 2020/01/26 10:43
# @Author  : xianming yu
# @File    : TXT文件操作.py

student_list = [{"name": "李四", "chinese": "65", "math": "65", "english": "65", "total": 195},
                {"name": "王五", "chinese": "65", "math": "65", "english": "65", "total": 195},
                {"name": "张三", "chinese": "65", "math": "65", "english": "65", "total": 195}]

while True:
    str_info = """*******************************************
    欢迎使用[学生信息管理系统]v1.0
    请选择你想要进行的操作
    1.新建学生信息
    2.显示全部信息
    3.查询学生信息
    4.删除学生信息
    5.修改学生信息
    
    0.退出系统
******************************************* """
    print(str_info)
    state=int(input("请输入需要操作的状态码:"))
    if state == 1:
        print("新建学生信息")
        name = input("请输入姓名:")
        chinese = eval(input("请输入语文成绩:"))
        math = eval(input("请输入数学成绩:"))
        english = eval(input("请输入英语成绩:"))
        total = chinese + math + english
        student_list.append({"name": name, "chinese": chinese, "math": math, "english": english, "total": total})
    # for i in student_list:
    #     print(i)
    elif state == 2:
        print("显示全部信息")
        print("姓名\t 语文\t 数学\t 英语\t 总分")
        for student in student_list:
            print(*student.values(), sep="      ")
    elif state == 3:
        print("查询学生信息")
        name = input("请输入要查询的信息:")
        for student in student_list:
            if student["name"] == name:
                print("姓名\t 语文\t 数学\t 英语\t 总分")
                print(*student.values(), sep="      ")
    elif state == 4:
        print("删除学生信息")
        name = input("请输入要删除的学生信息:")
        for student in student_list:
            if student["name"] == name:
                student_list.remove(student)
                print("*****已删除的学生信息如下*****")
                print("姓名\t 语文\t 数学\t 英语\t 总分")
                print(*student.values(), sep="      ")
    elif state == 5:
        print("修改学生信息")
        name = input("请输入要修改的信息")
        for student in student_list:
            if student["name"] == name:
                student["name"] == input("请输入名字:")
                student["chinese"] = eval(input("输入语文成绩:"))
                student["math"] = eval(input("输入数学成绩:"))
                student["english"] = eval(input("输入英语成绩:"))
                student["total"] = student["chinese"] + student["math"] + student["english"]
                print("*****已修改的学生信息如下*****")
                print("姓名\t 语文\t 数学\t 英语\t 总分")
                print(*student.values(), sep="      ")
    elif state == 0:
        print("退出学生管理系统...")
        break
