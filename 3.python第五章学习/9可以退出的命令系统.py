# 指令系统
import os

cmd = input("cmd:")
while cmd != "退出":
    if cmd == "记事本":
        os.system("notepad")
    if cmd == "系统进程":
        os.system("tasklist")
    else:
        print("其他指令")
    cmd = input("输入指令:")
