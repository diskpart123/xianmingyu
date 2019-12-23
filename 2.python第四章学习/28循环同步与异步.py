import os
import time

while True:
    os.system("start notepad")  # 指令前面加上start为"异步模式",不加称为"同步模式"
    time.sleep(1)  # 暂停1秒
