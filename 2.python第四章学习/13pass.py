# pass 空语句,什么都不执行

import os

cmd = input("输入关机指令:")
if cmd == "关机":
    os.system("shutdown -s -t 3600")  # shutdown -a 取消关机
else:
    pass
print("game over")
