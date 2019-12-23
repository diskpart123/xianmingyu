# while猜数字游戏
import random
str1 = "同电脑猜数字游戏,数字范围是:0 between 100"
print(str1.center(20, "*"))
count=1
number = random.randint(0, 100)
while count<11:
    count+=1
    input_number = eval(input("请输入数字:"))
    if input_number < 0 or input_number > 100:
        print("输入错误...只能输入0到100之间的数字")
    else:
        if input_number == number:
            print("恭喜您,猜对了!")
            break
        elif input_number > number:
            print(count)
            print("数字猜大了,你还有"+str(11-count)+"次机会,加油!")


        elif input_number < number:
            print("数字猜大了,你还有" + str(11 - count) + "次机会,加油!")
        else:
            print("输入错误!")

