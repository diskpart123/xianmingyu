"""
高考成绩录取判断题
大于750输出"输入错误"
等于小于0输出"输入错误"
大于等于700 且 小于等于750 输出:"清北"
大于等于600 且 小于700 输出:"985"
大于等于580 且 小于600 输出:"211"
大于等于550 且 小于580 输出:"一本"
大于等于500 且 小于550 输出:"二本"
大于等于450 且 小于500 输出:"三本"
大于等于350 且 小于450 输出:"大专"
否则输出:"学历到此为止,蓝翔等着你...."
"""

"""
第一种嵌套写法:
score = eval(input("输入分数:"))
if score > 750:
    print("输入错误")
else:
    if score < 0:
        print("输入错误")
    else:
        if score >= 700 and score <= 750:
            print("清北")
        else:
            if score >= 600 and score < 700:
                print("985")
            else:
                if score >= 580 and score < 600:
                    print("211")
                else:
                    if score >= 550 and score < 580:
                        print("一本")
                    else:
                        if score >= 500 and score < 550:
                            print("二本")
                        else:
                            if score >= 450 and score < 500:
                                print("三本")
                            else:
                                if score >= 350 and score < 450:
                                    print("大专")
                                else:
                                    print("学历到此为止,蓝翔等着你....")
"""

"""
第二种写法:
改良上面的if嵌套语句用elif来改写

score = eval(input("输入分数:"))
if score > 750:
    print("输入错误")
elif score <= 0:
    print("输入错误")
elif score >= 700 and score <= 750:
    print("清北")
elif score >= 600 and score < 700:
    print("985")
elif score >= 580 and score < 600:
    print("211")
elif score >= 550 and score < 580:
    print("一本")
elif score >= 500 and score < 550:
    print("二本")
elif score >= 450 and score < 500:
    print("三本")
elif score >= 350 and score < 450:
    print("大专")
else:
    print("学历到此为止,蓝翔等着你....")
"""

"""
第三种写法:
再次改写上面的elif写法,用隐含条件来实现

score = eval(input("输入分数:"))
if score > 750 or score <= 0:
    print("输入错误")
elif score >= 700:
    print("清北")
elif score >= 600:
    print("985")
elif score >= 580:
    print("211")
elif score >= 550:
    print("一本")
elif score >= 500:
    print("二本")
elif score >= 450:
    print("三本")
elif score >= 350:
    print("大专")
else:
    print("学历到此为止,蓝翔等着你....")
"""

"""
总结:上面elif的第二种写法不是按照顺序的方式来编写,所以在编写的时候需要加上区域判断
第三种写法是按照顺序的来编写,条件是隐含的
"""
