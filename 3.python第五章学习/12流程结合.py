"""
有一个需求:5秒钟的时候打开记事本,10秒钟的时候关闭记事本进程
"""
import time
import os
num=0
while True:
    time.sleep(1)
    num+=1
    print("第"+str(num)+"秒")
    if num==5:
        os.system("start notepad")
    elif num==10:
        os.system("taskkill /f /im notepad.exe")  #关闭记事本进程
        break


