import win32con
import win32gui
import time



# 做这个记事本1秒钟显示和隐藏的测试,必须先建立一个记事本然后把记事本打开,其他程序也是一样的操作

notepad = win32gui.FindWindow("Notepad", "新建文本文档 - 记事本")  # "Notepad"为类名,"新建文本文档 - 记事本"为标题
for i in range(120):
    time.sleep(1)  #表示停顿1秒钟
    if i % 2 == 0:
        win32gui.ShowWindow(notepad, win32con.SW_HIDE)   #SW_HIDE 表示隐藏
    else:
        win32gui.ShowWindow(notepad, win32con.SW_SHOW)   #SW_SHOW 表示显示
