# -*- coding: utf-8 -*-
# @Time    : 2020/02/22 9:01
# @Author  : xianming yu
# @File    : 20面向对象_校园IT系统.py

import time


#  课程类
class Course:
    def __init__(self, name, price, which_volume):
        # 课程名称
        self.name = name
        # 课程价格
        self.price = price
        # 第几期学费
        self.which_volume = which_volume
        # 交费原因
        self.fee_cause = None


# 学员类
class Personnel:
    def __init__(self, name):
        self.name = name


# 部门类
class DepartMent:
    def __init__(self, dept_name, time, position):
        # 部门名称
        self.dept_name = dept_name
        # 入职时间
        self.time = time
        # 职位
        self.position = position


# 班级类
class Class_grade:
    count = 0

    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.student_list = []
        self.course_list1 = {}

    def show(self, personnel, course):
        self.student_list.append(personnel.name)
        self.course_list1[personnel.name] = [course.name, course.price]
        Class_grade.count += 1

    def __str__(self):
        return ("班级:[%s]\n班级人数:%d\n学生列表:%s\n课程列表:%s" % (
            self.name, Class_grade.count, self.student_list, self.course_list1))


#  总部类
class Head_School:
    count = 0
    total_sum = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def branch_show1(self, class_grade, personnel, course):
        Head_School.total_sum += course.price

    def branch_show2(self, deparment, personnel):
        print("校区[%s]的[%s]部门在[%s]入职一名新同事[%s],职位是[%s]"
              % (self.name, deparment.dept_name, deparment.time, personnel.name, deparment.position))
        Head_School.count += 1

    #  打印学费总金额
    def gross_amount(self):
        print("Total balance:", Head_School.total_sum)

    # 打印总部员工人数
    def personnels(self):
        print("[%s]员工总人数:%d" % (self.name, Head_School.count))


# 北京分校类
class Branch_school_bj(Head_School):
    total_sum_bj = 0
    personnel_count = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fee_cause = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def branch_show2(self, deparment, personnel):
        print("校区[%s]的[%s]部门在[%s]入职一名新同事[%s],职位是[%s]"
              % (self.name, deparment.dept_name, deparment.time,
                 personnel.name, deparment.position))

    # 打印班级,课程,开班日期
    def class_course(self, classes, course):
        print("校区[%s]开设了[%s]课程第[%s]班,开班日期[%s]..." %
              (self.name, course.name, classes.name, classes.time))
        Branch_school_bj.personnel_count += 1

    # 打印学员姓名,课程价格,交费原因
    def branch_show3(self, personnel, course):
        course.fee_cause = "[%s-%s-%s]" % (self.name, course.name, course.which_volume)
        print("%s 校区[%s]收到[%s]转账[%d],交费原因%s..." % (self.fee_cause, self.name,
                                                   personnel.name, course.price, course.fee_cause))
        Branch_school_bj.total_sum_bj += course.price
        Head_School.total_sum += course.price

    def total_sum(self):
        print("[%s]账户余额:%d" % (self.name, Branch_school_bj.total_sum_bj))

    def personnels(self):
        print("[%s]员工总人数:%d" % (self.name, Branch_school_bj.personnel_count))


# 深圳分校类
class Branch_school_sz(Head_School):
    total_sum_sz = 0
    personnel_count = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fee_cause = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def branch_show2(self, deparment, personnel):
        print("校区[%s]的[%s]部门在[%s]入职一名新同事[%s],职位是[%s]"
              % (self.name, deparment.dept_name,
                 deparment.time, personnel.name, deparment.position))
        Branch_school_sz.personnel_count += 1

    # 打印班级,课程,开班日期
    def class_course(self, classes, course):
        print("校区[%s]开设了[%s]课程第[%s]班,开班日期[%s]..." %
              (self.name, course.name, classes.name, classes.time))

    # 打印学员姓名,课程价格,交费原因
    def branch_show3(self, personnel, course):
        course.fee_cause = "[%s-%s-%s]" % (self.name, course.name, course.which_volume)
        print("%s 校区[%s]收到[%s]转账[%d],交费原因%s..."
              % (self.fee_cause, self.name, personnel.name, course.price, course.fee_cause))
        Branch_school_sz.total_sum_sz += course.price
        Head_School.total_sum += course.price

    def total_sum(self):
        print("[%s]账户余额:%d" % (self.name, Branch_school_sz.total_sum_sz))

    def personnels(self):
        print("[%s]员工总人数:%d" % (self.name, Branch_school_sz.personnel_count))


# 上海分校1类
class Branch_school_sh(Head_School):
    total_sum_sh = 0
    personnel_count = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fee_cause = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.personnel_message = []

    def branch_show2(self, deparment, personnel):
        print("校区[%s]的[%s]部门在[%s]入职一名新同事[%s],职位是[%s]"
              % (self.name, deparment.dept_name, deparment.time, personnel.name, deparment.position))
        Branch_school_sh.personnel_count += 1

    # 打印班级,课程,开班日期
    def class_course(self, classes, course):
        print("校区[%s]开设了[%s]课程第[%s]班,开班日期[%s]..." %
              (self.name, course.name, classes.name, classes.time))

    # 打印学员姓名,课程价格,交费原因
    def branch_show3(self, personnel, course):
        course.fee_cause = "[%s-%s-%s]" % (self.name, course.name, course.which_volume)
        print("%s 校区[%s]收到[%s]转账[%d],交费原因%s..."
              % (self.fee_cause, self.name, personnel.name, course.price, course.fee_cause))
        Branch_school_sh.total_sum_sh += course.price
        Head_School.total_sum += course.price

    # 打印分校人员信息
    def branch_show4(self, personnel, course):
        course.fee_cause = "%s-%s-%s" % (self.name, course.name, course.which_volume)
        name = "学生:%s,班级:%s" % (personnel.name, course.fee_cause)
        self.personnel_message.append(name)

    def __str__(self):
        return "%s" % self.personnel_message

    def total_sum(self):
        print("[%s]账户余额:%d" % (self.name, Branch_school_sh.total_sum_sh))

    def personnels(self):
        print("[%s]员工总人数:%d" % (self.name, Branch_school_sh.personnel_count))


# 上海分校2类
class Branch_school_sh2(Head_School):
    total_sum_sh2 = 0
    personnel_count = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fee_cause = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.personnel_message = []

    def branch_show2(self, deparment, personnel):
        print("校区[%s]的[%s]部门在[%s]入职一名新同事[%s],职位是[%s]"
              % (self.name, deparment.dept_name, deparment.time, personnel.name, deparment.position))
        Branch_school_sh2.personnel_count += 1

    # 打印班级,课程,开班日期
    def class_course(self, classes, course):
        print("校区[%s]开设了[%s]课程第[%s]班,开班日期[%s]..." %
              (self.name, course.name, classes.name, classes.time))

    # 打印学员姓名,课程价格,交费原因
    def branch_show3(self, personnel, course):
        course.fee_cause = "[%s-%s-%s]" % (self.name, course.name, course.which_volume)
        print("%s 校区[%s]收到[%s]转账[%d],交费原因%s..."
              % (self.fee_cause, self.name, personnel.name, course.price, course.fee_cause))
        Branch_school_sh.total_sum_sh2 += course.price
        Head_School.total_sum += course.price

    # 打印分校人员信息
    def branch_show4(self, personnel, course):
        course.fee_cause = "%s-%s-%s" % (self.name, course.name, course.which_volume)
        name = "学生:%s,班级:%s" % (personnel.name, course.fee_cause)
        self.personnel_message.append(name)

    def __str__(self):
        return "%s" % self.personnel_message

    def total_sum(self):
        print("[%s]账户余额:%d" % (self.name, Branch_school_sh2.total_sum_sh2))

    def personnels(self):
        print("[%s]员工总人数:%d" % (self.name, Branch_school_sh2.personnel_count))


# 1.实例化课程类
python = Course("Python开发", 21800, "s21期学费")
yunwei = Course("Linux云计算运维", 19800, "s4期学费")
go = Course("GO开发", 9800, "s11期学费")

# 2.实例化学员类
alex = Personnel("Alex")
zhouxiaoyue = Personnel("周小月")
mjj = Personnel("mjj")
yjdw = Personnel("银角大王")
ytr = Personnel("苑天日")

blackgri = Personnel("blackgri")
lixiaohu = Personnel("李晓虎")
linaigen = Personnel("林爱根")
liuqingzheng = Personnel("刘清蒸")

# 4.实例化部门
zongjinban = DepartMent("总经办", "2015-05-22", "CEO")
hr = DepartMent("HR", "2017-03-12", "HR")
jiaoyanbu_bj = DepartMent("教研部", "2018-02-26", "前端开发工程师")
jiaoyanbu_sz = DepartMent("教研部", "2016-07-14", "Python讲师")
jiaoyanbu_sh = DepartMent("教研部", "2018-07-14", "Java讲师")

# 5. 实例化班级类
class_grade_bj_f = Class_grade("21", "2019-04-16")
class_grade_sz_f = Class_grade("4", "2019-04-16")
class_grade_sh_f = Class_grade("11", "2019-06-21")

# 6.实例化总校
beijing_school = Head_School("小猿圈北京总部", "成华区双林路215号")

# 7.实例化分校
beijing_fenxiao_school = Branch_school_bj("小猿圈北京分校", "石景山路124")
shenzheng_fenxiao_school = Branch_school_sz("深圳南山大学城分校", "南山科技园1号楼")
shanghai_fenxiao_school = Branch_school_sh("小猿圈上海1分校", "上海浦东1路39号")
shanghai_fenxiao_school2 = Branch_school_sh2("小猿圈上海分校2", "金融界33号")

# 打印各分校部门,人员,职位
beijing_school.branch_show2(zongjinban, alex)
beijing_school.branch_show2(hr, zhouxiaoyue)
beijing_fenxiao_school.branch_show2(jiaoyanbu_bj, mjj)
shenzheng_fenxiao_school.branch_show2(jiaoyanbu_sz, yjdw)
shanghai_fenxiao_school.branch_show2(jiaoyanbu_sh, ytr)

# 打印各分校课程
beijing_fenxiao_school.class_course(class_grade_bj_f, python)
shenzheng_fenxiao_school.class_course(class_grade_sz_f, yunwei)
shanghai_fenxiao_school.class_course(class_grade_sh_f, go)

# 打印分校,人员,课程价格
beijing_fenxiao_school.branch_show3(blackgri, python, )
shenzheng_fenxiao_school.branch_show3(lixiaohu, yunwei)
shanghai_fenxiao_school.branch_show3(linaigen, go)
shanghai_fenxiao_school.branch_show3(liuqingzheng, go)
shanghai_fenxiao_school.branch_show4(linaigen, go)
shanghai_fenxiao_school.branch_show4(liuqingzheng, go)

print(shanghai_fenxiao_school)
beijing_fenxiao_school.total_sum()
shanghai_fenxiao_school.total_sum()
shanghai_fenxiao_school2.total_sum()
shenzheng_fenxiao_school.total_sum()
beijing_school.gross_amount()
beijing_fenxiao_school.personnels()
shanghai_fenxiao_school.personnels()
shanghai_fenxiao_school2.personnels()
shenzheng_fenxiao_school.personnels()

beijing_school.personnels()
