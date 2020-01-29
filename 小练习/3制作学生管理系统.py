# -*- coding: utf-8 -*-
# @Time    : 2020/01/26 11:01
# @Author  : xianming yu
# @File    : 3制作学生管理系统.py


student_list = [{"name": "李四", "chinese": "65", "math": "65", "english": "65", "total": 195},
                {"name": "王五", "chinese": "65", "math": "65", "english": "65", "total": 195},
                {"name": "张三", "chinese": "65", "math": "65", "english": "65", "total": 195}]

state = True
while state:
    str_info = """*******************************************
    欢迎使用[学生信息管理系统]v1.0
    请选择你想要进行的操作
    1.新建学生信息
    2.显示全部信息
    3.查询学生信息
    4.删除学生信息
    5.修改学生信息
    
    0.退出系统
******************************************* 
    """
    print(str_info)
    states = eval(input("请输入需要操作的状态码:"))
    if states == 1:
        print("新建学生信息")
        name = input("输入姓名:")
        chinese = eval(input("输入语文成绩:"))
        math = eval(input("输入数学成绩:"))
        english = eval(input("输入英语成绩:"))
        total = chinese + math + english
        student_list.append({"name": name, "chinese": chinese, "math": math, "english": english, "total": total})
    elif states == 2:
        print("显示全部学生信息")
        print("姓名\t\t语文\t数学\t英语\t总分")
        for i in student_list:
            print(*i.values(), sep="\t\t")  # 对字典进行解包操作
    elif states == 3:
        name = input("请输入要查询的信息:")
        for student in student_list:
            if student["name"] == name:
                print("姓名\t\t语文\t数学\t英语\t总分")
                print(*student.values(), sep="\t\t")
    elif states == 4:
        name=input("请输入要删除的信息:")
        for student in student_list:
            if student["name"]==name:
                student_list.remove(student)
                print(student)
        else:
            pass
    elif states == 5:
        name=input("请输入需要修改的信息:")
        for student in student_list:
            if student["name"]==name:
                student["name"]=input("请输入名字:")
                student["chinese"]=eval(input("请输入语文成绩:"))
                student["math"]=eval(input("请输入数学成绩:"))
                student["english"]=eval(input("请输入英语成绩:"))
                student["total"]=student["chinese"]+student["math"]+student["english"]
    elif states ==0:
        print("退出学生管理系统....")
        break
    else:
        print("你输入的{}编码不存在...".format(states))
