import os

cmd = input("请输入指令:")
if cmd == "记事本":
    os.system("notepad")
elif cmd == "计算器":
    os.system("calc")
elif cmd == "进程":
    os.system("tasklist")
elif cmd == "ip地址":
    os.system("ipconfig")
elif cmd == "防火墙":
    os.system("wf.msc")
elif cmd == "时间":
    os.system("timedate.cpl")

elif cmd == "重启电脑":
    os.system("shutdown -r -t 200")
elif cmd == "电脑关机":
    os.system("shutdown -s -t 200")
else:
    print("其他指令,还没有翻译!")
