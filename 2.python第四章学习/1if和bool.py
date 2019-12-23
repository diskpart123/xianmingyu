# if 简单编写

import os

"""
cmd = input("cmd:")
if cmd == "notepad":
    os.system("notepad")
"""

# if 加 bool编写

cmd = input("cmd:")
isrun = (cmd == "notepad")  # cmd == "notepad" 是逻辑表达式,返回真 或者 返回假
print(isrun)
if isrun:
    os.system("notepad")
