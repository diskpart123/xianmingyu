# 猜游戏,如果猜到了3次，提示是否还继续猜游戏
import random

"""
a = random.randint(0, 9)
print(a)

count = 0
youxi = False
while not youxi:
    number = int(input("input number:"))
    if number == a:
        print("答案对了...游戏结束!")
        break
    else:
        print("答案不正确...")
        count += 1
    if count == 3:
        print("是否继续游戏,是(Y),否(N)")
        jixu = input(":")
        if jixu == "Y":
            count = 0
        elif jixu == "N":
            break
        else:
            jixu != "N"
            print("请重新输入!")
            while not youxi:
                jixu = input(":")
                if jixu == "N":
                    youxi = True
                else:
                    print("请重新输入！")
                    continue
"""
import  os
import time
import datetime
path=input("请输入文件路径:")
for root,dirs,files in os.walk(path):
    for file in files:
        a=os.path.join(root,file)
        b = time.localtime(os.stat(a).st_ctime)
        b = time.strftime("%Y%m%d", b)
        today = datetime.datetime.now()
        offset = datetime.timedelta(days=-7)
        re_date = (today + offset).strftime('%Y%m%d')
        if re_date>=b:
            os.remove(a)
        else:
            pass

       




